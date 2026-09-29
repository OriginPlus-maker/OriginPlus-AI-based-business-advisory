"""
Unit tests for ORIGIN Deterministic Financial Engine
"""

import sys
import os

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rules.financial_engine import (
    calculate_project_cost,
    calculate_reducing_balance_emi,
    route_scheme_and_loan,
    compute_financial_structure
)


def test_demo_scenario():
    """Verify exact SIH Demo specifications: Margin ₹50,000"""
    margin = 50000.0
    structure = compute_financial_structure(margin, "dairy")
    
    assert structure["project_cost"] == 500000.0, f"Expected 5,00,000, got {structure['project_cost']}"
    assert structure["scheme"]["scheme_name"] == "Term Loan Scheme"
    assert structure["scheme"]["eligible_loan"] == 450000.0, f"Expected 4,50,000, got {structure['scheme']['eligible_loan']}"
    assert structure["scheme"]["interest_rate_pct"] == 8.0
    assert structure["scheme"]["tenure_years"] == 7
    assert structure["scheme"]["moratorium_months"] == 6
    assert structure["scheme"]["monthly_emi"] > 0
    print(f"[PASS] Demo Scenario: Project Cost=Rs.{structure['project_cost']}, Loan=Rs.{structure['scheme']['eligible_loan']}, EMI=Rs.{structure['scheme']['monthly_emi']}/mo")


def test_micro_finance_cap_enforcement():
    """
    CRITICAL SIH TEST:
    Project Cost = Rs. 1.40 Lakh (Margin = Rs. 14,000)
    90% theoretical loan = Rs. 1.26 Lakh.
    MAX Micro Finance loan = Rs. 1.25 Lakh.
    The system MUST return Rs. 1.25 Lakh, NOT Rs. 1.26 Lakh.
    """
    margin = 14000.0
    structure = compute_financial_structure(margin, "kirana")
    
    assert structure["project_cost"] == 140000.0
    assert structure["scheme"]["scheme_name"] == "Micro Finance Scheme"
    assert structure["scheme"]["theoretical_loan"] == 126000.0
    assert structure["scheme"]["eligible_loan"] == 125000.0, f"Expected strictly 1,25,000 cap, got {structure['scheme']['eligible_loan']}"
    assert structure["scheme"]["interest_rate_pct"] == 6.5
    assert structure["scheme"]["tenure_years"] == 3
    assert structure["scheme"]["moratorium_months"] == 3
    print(f"[PASS] Micro Finance Cap Test: Theoretical Rs. 1.26L capped at strictly Rs.{structure['scheme']['eligible_loan']}")


def test_micro_finance_below_cap():
    """Project Cost Rs. 1.00 Lakh (Margin = Rs. 10,000) -> 90% = Rs. 90,000 (Below Rs. 1.25L cap)"""
    margin = 10000.0
    structure = compute_financial_structure(margin, "poultry")
    
    assert structure["project_cost"] == 100000.0
    assert structure["scheme"]["eligible_loan"] == 90000.0
    assert structure["scheme"]["scheme_name"] == "Micro Finance Scheme"
    print(f"[PASS] Below Cap Test: Rs. 90,000 eligible loan approved at 6.5% for 3 years.")


def test_outside_scheme_range():
    """Margin Rs. 6.00 Lakh -> Project Cost Rs. 60.00 Lakh (> 50 Lakh limit)"""
    margin = 600000.0
    structure = compute_financial_structure(margin, "food processing")
    
    assert structure["project_cost"] == 6000000.0
    assert structure["scheme"]["is_supported"] is False
    assert structure["scheme"]["scheme_name"] == "Outside supported scheme range"
    print(f"[PASS] Outside Limit Test: Handled gracefully without crash.")


if __name__ == "__main__":
    print("Running Financial Rule Engine verification suite...")
    test_demo_scenario()
    test_micro_finance_cap_enforcement()
    test_micro_finance_below_cap()
    test_outside_scheme_range()
    print("ALL FINANCIAL ENGINE TESTS PASSED!")

