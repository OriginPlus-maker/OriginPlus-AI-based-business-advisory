"""
ORIGIN - Explainable AI Advisory Engine
Generates structured, explainable natural-language recommendations based on
hyper-local market intelligence and immutable deterministic financial results.

IMPORTANT:
- AI NEVER overrides or calculates financial parameters.
- AI explains why the opportunity is viable, key rural risks, and concrete next steps.
"""

from typing import Dict, Any, List
import os


def generate_ai_advisory(
    market_data: Dict[str, Any],
    financial_data: Dict[str, Any],
    language: str = "en"
) -> Dict[str, Any]:
    """
    Synthesizes structured advisory. Accepts immutable financial structure from the
    financial rule engine and market findings from the local data engine.
    """
    biz = market_data["business"]
    biz_key = biz["key"]
    biz_title = biz["title"]
    location = market_data["location"]
    village = location["village"]
    block = location["block"]
    district = location["district"]
    metrics = market_data["metrics"]
    scheme_info = financial_data["scheme"]
    project_cost = financial_data["project_cost"]
    eligible_loan = scheme_info["eligible_loan"]
    scheme_name = scheme_info["scheme_name"]
    confidence_score = market_data["viability_score"]

    # Multilingual advisory templates for English, Hindi, and Marathi
    if language == "mr":  # Marathi
        headline = f"{village} ({block}) साठी {biz_title} हा अत्यंत अनुकूल व्यवसाय पर्याय आहे."
        why_points = [
            f"स्थानिक मागणी अनुकूल आहे (अंदाजे {metrics['target_customers']:,} संभाव्य ग्राहक)",
            f"{metrics['market_reach']} परिघात नियंत्रित स्पर्धा आणि सहज पोहोच",
            f"उपलब्ध भांडवलानुसार ₹{project_cost:,.0f} चा व्यवहार्य प्रकल्प खर्च",
            f"'{scheme_name}' अंतर्गत ₹{eligible_loan:,.0f} चे सवलतीचे कर्ज उपलब्ध"
        ]
        risk_text = market_data["key_risk"]
        action_text = (
            "व्यवसाय मर्यादित स्वरूपात सुरू करा आणि विस्तारापूर्वी स्थानिक दुग्ध संस्था/ग्राहकांशी "
            "नियमित खरेदी करार स्थापित करा."
        )
        executive_summary = (
            f"ORIGIN कृत्रिम बुद्धिमत्ता विश्लेषणाद्वारे {village} मधील स्थानिक बाजाराचा अभ्यास करण्यात आला. "
            f"येथील ग्राहकांची संख्या ({metrics['target_customers']:,}) आणि ₹{financial_data['available_margin']:,.0f} च्या "
            f"मार्जिन रकमेसह, {biz_title} प्रकल्प आर्थिक व व्यावसायिकदृष्ट्या फायदेशीर ठरू शकतो."
        )

    elif language == "hi":  # Hindi
        headline = f"{village} ({district}) के लिए {biz_title} एक उपयुक्त और व्यावहारिक व्यवसाय विकल्प है।"
        why_points = [
            f"अनुकूल स्थानीय मांग ({metrics['target_customers']:,} लक्षित ग्राहकों का आधार)",
            f"{metrics['market_reach']} के दायरे में संतुलित स्थानीय प्रतिस्पर्धा",
            f"उपलब्ध पूंजी के अनुसार ₹{project_cost:,.0f} का संतुलित परियोजना आकार",
            f"'{scheme_name}' के तहत ₹{eligible_loan:,.0f} का संस्थागत ऋण समर्थन"
        ]
        risk_text = market_data["key_risk"]
        action_text = (
            "व्यवसाय को एक नियंत्रित स्तर पर शुरू करें और विस्तार करने से पहले स्थानीय आपूर्तिकर्ताओं "
            "और नियमित खरीदारों के साथ मजबूत संबंध बनाएं।"
        )
        executive_summary = (
            f"ORIGIN एआई विश्लेषण के अनुसार, {village} में {biz_title} व्यवसाय के लिए स्थानीय बाजार की स्थिति "
            f"सकारात्मक है। आपकी उपलब्ध मार्जिन पूंजी (₹{financial_data['available_margin']:,.0f}) और {scheme_name} "
            f"के माध्यम से ₹{eligible_loan:,.0f} का ऋण लेकर इस व्यवसाय को सुदृढ़ रूप से स्थापित किया जा सकता है।"
        )

    else:  # Default: English
        headline = f"{biz_title} is a suitable business option for this location and investment capacity."
        why_points = [
            f"Favorable local demand ({metrics['target_customers']:,} target customer catchment)",
            f"Manageable competition density within {metrics['market_reach']} radius",
            f"Suitable investment level: ₹{project_cost:,.0f} total project sizing matches rural absorption",
            f"Accessible financing: Routed directly to '{scheme_name}' for ₹{eligible_loan:,.0f} credit support"
        ]
        risk_text = market_data["key_risk"]
        action_text = (
            "Start at a manageable scale and establish local supplier and customer relationships before expanding."
        )
        executive_summary = (
            f"ORIGIN hyper-local analysis confirms that {village} presents strong feasibility for {biz_title}. "
            f"With your available margin capital of ₹{financial_data['available_margin']:,.0f}, you can construct a "
            f"viable ₹{project_cost:,.0f} project supported by ₹{eligible_loan:,.0f} under the {scheme_name} at "
            f"{scheme_info['interest_rate_pct']}% interest with a {scheme_info['moratorium_months']}-month operational moratorium."
        )

    return {
        "heading": "ORIGIN AI Recommendation",
        "headline": headline,
        "confidence_pct": confidence_score,
        "why": why_points,
        "risk": risk_text,
        "action": action_text,
        "executive_summary": executive_summary,
        "is_explainable": True,
        "financial_summary_explained": {
            "project_cost": project_cost,
            "own_margin": financial_data["own_contribution"],
            "eligible_loan": eligible_loan,
            "scheme_name": scheme_name,
            "monthly_emi": scheme_info["monthly_emi"],
            "interest_rate": scheme_info["interest_rate_pct"],
            "tenure_years": scheme_info["tenure_years"],
            "moratorium_months": scheme_info["moratorium_months"]
        }
    }

