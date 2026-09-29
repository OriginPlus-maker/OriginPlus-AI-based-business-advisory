"""
ORIGIN - Deterministic Financial Engine
Implements deterministic banking, project-cost, loan sizing, scheme routing,
reducing-balance EMI calculation, and working capital estimations.

IMPORTANT: LLMs MUST NOT calculate or modify these numbers.
"""

from typing import Dict, Any, Optional
import math


def calculate_project_cost(margin_capital: float) -> float:
    """
    Calculates total viable project cost based on available margin capital.
    Rule: Project Cost = Available Margin / 10%
    """
    if margin_capital <= 0:
        raise ValueError("Margin capital must be strictly positive (> 0)")
    return round(margin_capital / 0.10, 2)


def calculate_reducing_balance_emi(principal: float, annual_rate_pct: float, tenure_years: int) -> float:
    """
    Calculates monthly EMI using the standard reducing-balance formula:
    EMI = P * [r * (1 + r)^n] / [(1 + r)^n - 1]
    where:
      P = Principal loan amount
      r = Monthly interest rate (annual_rate / 12 / 100)
      n = Total number of monthly installments (tenure_years * 12)
    """
    if principal <= 0:
        return 0.0
    if tenure_years <= 0:
        return principal

    monthly_rate = annual_rate_pct / (12 * 100)
    total_months = tenure_years * 12

    if monthly_rate == 0:
        return round(principal / total_months, 2)

    compound_factor = math.pow(1 + monthly_rate, total_months)
    emi = principal * (monthly_rate * compound_factor) / (compound_factor - 1)
    return round(emi, 2)


def route_scheme_and_loan(project_cost: float, margin_capital: float) -> Dict[str, Any]:
    """
    Determines scheme eligibility, loan amount, interest rate, tenure, and moratorium.
    Strictly enforces official scheme caps and prevents theoretical over-borrowing.

    MICRO FINANCE SCHEME:
      - Project Cost: Up to ₹1.40 lakh (<= 140,000)
      - Maximum Loan: ₹1.25 lakh (125,000)
      - Interest: 6.5% p.a.
      - Tenure: 3 years
      - Moratorium: 3 months
      - Example check: At ₹1.40L project cost, 90% = ₹1.26L, but loan is capped at ₹1.25L.

    TERM LOAN SCHEME:
      - Project Cost: Above ₹1.40 lakh up to ₹50 lakh (> 140,000 and <= 5,000,000)
      - Maximum Loan: ₹45 lakh (4,500,000)
      - Interest: 8.0% p.a.
      - Tenure: 7 years
      - Moratorium: 6 months

    OUTSIDE SCHEME:
      - Project Cost > ₹50 lakh (Margin > ₹5 lakh)
    """
    theoretical_loan = round(project_cost * 0.90, 2)

    if project_cost <= 140000.0:
        scheme_name = "Micro Finance Scheme"
        interest_rate = 6.5
        tenure_years = 3
        moratorium_months = 3
        max_loan_cap = 125000.0
        eligible_loan = min(theoretical_loan, max_loan_cap)
        status = "Eligible - Micro Finance"
        is_supported = True
        notes = (
            "Eligible under Micro-Enterprise Credit Facility with concessionary 6.5% p.a. rate "
            "and 3-month initial operational moratorium."
        )

    elif project_cost <= 5000000.0:
        scheme_name = "Term Loan Scheme"
        interest_rate = 8.0
        tenure_years = 7
        moratorium_months = 6
        max_loan_cap = 4500000.0
        eligible_loan = min(theoretical_loan, max_loan_cap)
        status = "Eligible - Term Loan"
        is_supported = True
        notes = (
            "Eligible under Rural Term Loan Facility with competitive 8.0% p.a. rate "
            "and 6-month capital gestation moratorium."
        )

    else:
        scheme_name = "Outside supported scheme range"
        interest_rate = 0.0
        tenure_years = 0
        moratorium_months = 0
        max_loan_cap = 0.0
        eligible_loan = 0.0
        status = "Outside supported scheme range"
        is_supported = False
        notes = (
            "The proposed project cost exceeds the ₹50.00 Lakh threshold for automatic rural micro/term loan routing. "
            "Requires specialized consortium financing or direct NABARD/SIDBI large project appraisal."
        )

    # Calculate EMI and repayment details if supported
    if is_supported and eligible_loan > 0:
        emi = calculate_reducing_balance_emi(eligible_loan, interest_rate, tenure_years)
        total_months = tenure_years * 12
        total_repayment = round(emi * total_months, 2)
        total_interest = round(total_repayment - eligible_loan, 2)
    else:
        emi = 0.0
        total_repayment = 0.0
        total_interest = 0.0

    return {
        "scheme_name": scheme_name,
        "is_supported": is_supported,
        "status": status,
        "interest_rate_pct": interest_rate,
        "tenure_years": tenure_years,
        "moratorium_months": moratorium_months,
        "max_loan_cap": max_loan_cap,
        "theoretical_loan": theoretical_loan,
        "eligible_loan": eligible_loan,
        "monthly_emi": emi,
        "total_repayment": total_repayment,
        "total_interest": total_interest,
        "notes": notes
    }


def estimate_working_capital(project_cost: float, business_category: str = "dairy") -> Dict[str, Any]:
    """
    Provides an illustrative breakdown of estimated working capital requirements (~20% of project cost).
    """
    category_lower = business_category.lower()
    
    if "dairy" in category_lower:
        pct = 0.20
        breakdown = {
            "Cattle Feed & Nutrition": 0.45,
            "Veterinary & Medicine Reserve": 0.15,
            "Chilling & Transport Fuel": 0.20,
            "Utility & Power Expenses": 0.10,
            "Emergency Operating Buffer": 0.10
        }
    elif "kirana" in category_lower or "retail" in category_lower:
        pct = 0.25
        breakdown = {
            "Fast-Moving Inventory Replenishment": 0.55,
            "Supplier Credit Advance": 0.15,
            "Freight & Local Haulage": 0.15,
            "Store Utilities & Packaging": 0.15
        }
    elif "poultry" in category_lower:
        pct = 0.22
        breakdown = {
            "Feed & Grain Procurement": 0.50,
            "Vaccination & Bio-security": 0.20,
            "Litter & Bedding Management": 0.10,
            "Power & Heating Reserve": 0.20
        }
    elif "food" in category_lower or "processing" in category_lower:
        pct = 0.22
        breakdown = {
            "Seasonal Agri Raw Materials": 0.50,
            "Food-Grade Packaging Material": 0.20,
            "Processing Energy & Fuel": 0.15,
            "Hygiene & Quality Compliance": 0.15
        }
    else:
        pct = 0.20
        breakdown = {
            "Raw Materials & Inventory": 0.50,
            "Transportation & Logistics": 0.20,
            "Utilities & Power": 0.15,
            "Emergency Buffer": 0.15
        }

    total_working_capital = round(project_cost * pct, 2)
    itemized = {k: round(total_working_capital * weight, 2) for k, weight in breakdown.items()}

    return {
        "percentage_of_project": round(pct * 100, 1),
        "estimated_amount": total_working_capital,
        "is_illustrative": True,
        "itemized_breakdown": itemized,
        "disclaimer": "Illustrative working capital estimate based on sector benchmarks. Actual working capital limit determined during formal bank appraisal."
    }


def compute_financial_structure(margin_capital: float, business_category: str = "dairy") -> Dict[str, Any]:
    """
    Master function: accepts available margin capital and produces the complete
    deterministic financial structure conforming to SIH26091 rules.
    """
    project_cost = calculate_project_cost(margin_capital)
    scheme_result = route_scheme_and_loan(project_cost, margin_capital)
    working_capital = estimate_working_capital(project_cost, business_category)

    # Own contribution is either the full margin or margin capital
    own_contribution = margin_capital

    return {
        "available_margin": margin_capital,
        "project_cost": project_cost,
        "own_contribution": own_contribution,
        "margin_percentage": 10.0,
        "scheme": scheme_result,
        "working_capital": working_capital,
        "is_deterministic": True,
        "disclaimer": "Illustrative EMI — final repayment terms subject to applicable scheme rules."
    }

