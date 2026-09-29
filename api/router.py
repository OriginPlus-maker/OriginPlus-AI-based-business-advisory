"""
ORIGIN - API Router
Exposes REST endpoints for Location, Market Data, Financial Calculation,
AI Advisory, Full Feasibility Analysis, and Report Generation.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Any, Optional

from models.schemas import (
    AnalyzeRequest,
    FinancialCalculateRequest,
    AdvisoryRequest,
    ReportRequest
)
from rules.financial_engine import (
    compute_financial_structure,
    route_scheme_and_loan
)
from services.local_data_service import (
    get_curated_locations,
    get_supported_business_categories,
    get_hyper_local_market_analysis
)
from services.ai_advisory_service import generate_ai_advisory
from services.report_generator import generate_report_payload

api_router = APIRouter()


@api_router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ORIGIN Rural Business Feasibility API",
        "version": "1.0.0",
        "problem_statement": "SIH26091",
        "category": "Agriculture, FoodTech & Rural Development"
    }


@api_router.get("/location")
def get_locations(search: Optional[str] = None):
    """
    Returns curated Indian rural village & district benchmarks.
    """
    locations = get_curated_locations()
    if search:
        s = search.lower()
        locations = [
            loc for loc in locations
            if s in loc["village"].lower()
            or s in loc["district"].lower()
            or s in loc["state"].lower()
        ]
    return {
        "count": len(locations),
        "locations": locations
    }


@api_router.get("/business-categories")
def get_business_categories():
    """
    Returns supported micro-enterprise categories with benchmark defaults.
    """
    return {
        "categories": get_supported_business_categories()
    }


@api_router.get("/schemes")
def get_schemes():
    """
    Returns official government credit schemes referenced by the rule engine.
    """
    return {
        "schemes": [
            {
                "scheme_name": "Micro Finance Scheme",
                "target": "Rural micro-entrepreneurs & first-time credit seekers",
                "max_project_cost": 140000.0,
                "max_loan_cap": 125000.0,
                "financing_ratio": "90% of project cost (capped at ₹1.25L)",
                "own_margin_required": "10%",
                "interest_rate_pct": 6.5,
                "tenure_years": 3,
                "moratorium_months": 3,
                "description": "Concessionary micro-enterprise loan with 3 months operational moratorium."
            },
            {
                "scheme_name": "Term Loan Scheme",
                "target": "Expanding rural enterprises & agro-allied processing",
                "min_project_cost": 140001.0,
                "max_project_cost": 5000000.0,
                "max_loan_cap": 4500000.0,
                "financing_ratio": "90% of project cost (capped at ₹45L)",
                "own_margin_required": "10%",
                "interest_rate_pct": 8.0,
                "tenure_years": 7,
                "moratorium_months": 6,
                "description": "Medium-term capital financing with 6 months gestation moratorium."
            }
        ],
        "disclaimer": "Scheme terms reflect benchmark national guidelines; actual sanction terms subject to credit score and local bank branch discretion."
    }


@api_router.get("/market")
def get_market(
    state: str = Query(..., min_length=2),
    district: str = Query(..., min_length=2),
    block: str = Query("", min_length=0),
    village: str = Query(..., min_length=2),
    business: str = Query("dairy")
):
    """
    Returns hyper-local market intelligence, competitor map POIs, and demand indicators.
    """
    analysis = get_hyper_local_market_analysis(
        state=state,
        district=district,
        block=block,
        village=village,
        business_category=business
    )
    return analysis


@api_router.post("/financial/calculate")
def calculate_financials(payload: FinancialCalculateRequest):
    """
    Dedicated endpoint for the deterministic financial engine.
    LLM is never involved in this endpoint.
    """
    try:
        structure = compute_financial_structure(payload.capital, payload.business or "dairy")
        return structure
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@api_router.post("/advisory")
def get_advisory(payload: AdvisoryRequest):
    """
    Generates explainable AI recommendation based on market intelligence and financial sizing.
    """
    market_data = get_hyper_local_market_analysis(
        state=payload.state,
        district=payload.district,
        block=payload.block or "",
        village=payload.village,
        business_category=payload.business
    )
    financial_data = compute_financial_structure(payload.capital, payload.business)
    advisory = generate_ai_advisory(market_data, financial_data, payload.language or "en")
    return advisory


@api_router.post("/analyze")
def analyze_business(payload: AnalyzeRequest):
    """
    Master unified endpoint:
    Location + Capital + Business + Language
    -> Hyper-local data
    -> Deterministic financial calculation
    -> Scheme routing
    -> Explainable AI advisory
    -> Report payload
    """
    try:
        # 1. Hyper-local market data
        market_data = get_hyper_local_market_analysis(
            state=payload.state,
            district=payload.district,
            block=payload.block or "",
            village=payload.village,
            business_category=payload.business
        )

        # 2. Deterministic financial structure
        financial_data = compute_financial_structure(
            margin_capital=payload.capital,
            business_category=payload.business
        )

        # 3. AI advisory synthesis
        advisory_data = generate_ai_advisory(
            market_data=market_data,
            financial_data=financial_data,
            language=payload.language or "en"
        )

        # 4. Generate structured report
        report_data = generate_report_payload(
            market_data=market_data,
            financial_data=financial_data,
            advisory_data=advisory_data,
            language=payload.language or "en"
        )

        return {
            "viability_score": market_data["viability_score"],
            "status": market_data["status"],
            "demand": market_data["metrics"]["local_demand"],
            "competition": market_data["metrics"]["competition"],
            "market_reach": market_data["metrics"]["market_reach"],
            "target_customers": market_data["metrics"]["target_customers"],
            "recommendation": advisory_data["headline"],
            "market": market_data,
            "financial": financial_data,
            "advisory": advisory_data,
            "report": report_data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@api_router.post("/report")
def export_report(payload: ReportRequest):
    """
    Generates downloadable report format from an analysis payload.
    """
    try:
        p = payload.analysis_payload
        # If already formatted report is passed
        if "report" in p:
            return p["report"]
        return p
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

