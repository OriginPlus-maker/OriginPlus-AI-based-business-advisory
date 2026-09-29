"""
ORIGIN - Feasibility Report Generator Service
Builds comprehensive, presentation-ready advisory reports formatted for
government/fintech standards and printable/PDF export.
"""

from typing import Dict, Any
from datetime import datetime


def generate_report_payload(
    market_data: Dict[str, Any],
    financial_data: Dict[str, Any],
    advisory_data: Dict[str, Any],
    language: str = "en"
) -> Dict[str, Any]:
    """
    Compiles all analysis layers into a unified formal report object.
    """
    now = datetime.now()
    report_id = f"ORIGIN-SIH-{now.strftime('%Y%m%d')}-{abs(hash(market_data['location']['village'])) % 100000:05d}"
    formatted_date = now.strftime("%d %B %Y, %I:%M %p")

    disclaimer = (
        "This prototype uses illustrative/demo data where live local data is unavailable. "
        "Financial and scheme outputs are indicative and must be verified against current official "
        "guidelines before formal credit appraisal and disbursement decisions."
    )

    return {
        "report_id": report_id,
        "generated_at": formatted_date,
        "platform": {
            "name": "ORIGIN",
            "tagline": "Your Business Idea. Your Local Market. Your Financial Plan.",
            "sub_title": "AI-Driven Hyper-Local Business Advisory and Financial Structuring Assistant",
            "sih_code": "SIH26091",
            "theme": "Agriculture, FoodTech & Rural Development"
        },
        "user_profile": {
            "state": market_data["location"]["state"],
            "district": market_data["location"]["district"],
            "block": market_data["location"]["block"],
            "village": market_data["location"]["village"],
            "coordinates": {
                "lat": market_data["location"]["lat"],
                "lng": market_data["location"]["lng"]
            },
            "available_margin_capital": financial_data["available_margin"],
            "business_selected": market_data["business"]["title"],
            "language": language
        },
        "feasibility": {
            "score": market_data["viability_score"],
            "status": market_data["status"],
            "confidence": market_data["confidence"],
            "data_updated": market_data["last_updated"],
            "is_demo_data": True,
            "metrics": market_data["metrics"]
        },
        "market_intelligence": {
            "summary": market_data["insights"]["summary"],
            "target_segment": market_data["insights"]["target_segment"],
            "demand_indicator": market_data["insights"]["demand_indicator"],
            "purchasing_pattern": market_data["insights"]["purchasing_pattern"],
            "market_opportunity": market_data["insights"]["market_opportunity"],
            "service_gap": market_data["insights"]["service_gap"],
            "population_funnel": market_data["population_funnel"],
            "competitors_count": len(market_data["map_data"]["competitors"]),
            "competitors_summary": [
                {"name": c["name"], "distance": f"{c['distance_km']} km", "scale": c["scale"]}
                for c in market_data["map_data"]["competitors"]
            ],
            "key_pois": [
                {"name": p["name"], "type": p["type"], "distance": f"{p['distance_km']} km"}
                for p in market_data["map_data"]["pois"]
            ]
        },
        "swot_analysis": market_data["swot"],
        "ai_advisory": advisory_data,
        "financial_structure": {
            "project_cost": financial_data["project_cost"],
            "own_contribution": financial_data["own_contribution"],
            "margin_pct": 10.0,
            "scheme_name": financial_data["scheme"]["scheme_name"],
            "eligible_loan": financial_data["scheme"]["eligible_loan"],
            "max_loan_cap": financial_data["scheme"]["max_loan_cap"],
            "interest_rate_pct": financial_data["scheme"]["interest_rate_pct"],
            "tenure_years": financial_data["scheme"]["tenure_years"],
            "moratorium_months": financial_data["scheme"]["moratorium_months"],
            "monthly_emi": financial_data["scheme"]["monthly_emi"],
            "total_repayment": financial_data["scheme"]["total_repayment"],
            "total_interest": financial_data["scheme"]["total_interest"],
            "scheme_notes": financial_data["scheme"]["notes"],
            "working_capital": financial_data["working_capital"]
        },
        "action_plan": market_data["action_plan"],
        "disclaimer": disclaimer
    }

