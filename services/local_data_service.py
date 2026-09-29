"""
ORIGIN - Hyper-Local Market Data Service
Provides localized demographic indicators, competitor mapping POIs,
demand estimates, and data confidence ratings.
All values clearly flagged with DEMO / PROTOTYPE DATA attributes.
"""

from typing import Dict, Any, List, Optional
import math
import random
from data.local_market_data import LOCATIONS_DATABASE, BUSINESS_PROFILES


def get_curated_locations() -> List[Dict[str, Any]]:
    """Returns list of curated locations with hierarchical levels."""
    return LOCATIONS_DATABASE


def get_supported_business_categories() -> List[Dict[str, Any]]:
    """Returns list of supported business categories with icons and descriptions."""
    categories = []
    for key, val in BUSINESS_PROFILES.items():
        categories.append({
            "id": key,
            "title": val["title"],
            "icon": val["icon"],
            "target_audience": val["target_audience"],
            "default_reach": val["default_reach"]
        })
    return categories


def resolve_location_metadata(
    state: str,
    district: str,
    block: str,
    village: str
) -> Dict[str, Any]:
    """
    Finds exact matching location in curated database or generates realistic
    synthetic demographics for any custom Indian village entered by the user.
    """
    state_clean = state.strip().lower()
    district_clean = district.strip().lower()
    village_clean = village.strip().lower()

    for item in LOCATIONS_DATABASE:
        if (
            village_clean in item["village"].lower()
            and (not district_clean or district_clean in item["district"].lower())
        ):
            return {
                "matched": True,
                "state": item["state"],
                "district": item["district"],
                "block": item["block"],
                "village": item["village"],
                "lat": item["lat"],
                "lng": item["lng"],
                "population": item["population"],
                "households": item["households"],
                "nearest_mandi": item["nearest_mandi"],
                "weekly_haat_day": item["weekly_haat_day"],
                "rural_tier": item["rural_tier"],
                "confidence": item["confidence"],
                "last_updated": item["last_updated"],
                "is_demo_data": True
            }

    # For user-typed custom village, provide coherent geo-demographics
    # Default around central Maharashtra / India coordinate anchor
    base_lat = 18.5204 + (len(village) % 5) * 0.12 - 0.25
    base_lng = 73.8567 + (len(district) % 5) * 0.15 - 0.30
    synth_pop = 22000 + (len(village) * 1150) % 25000
    synth_households = int(synth_pop / 4.8)

    return {
        "matched": False,
        "state": state,
        "district": district,
        "block": block,
        "village": village,
        "lat": round(base_lat, 4),
        "lng": round(base_lng, 4),
        "population": synth_pop,
        "households": synth_households,
        "nearest_mandi": f"{block or district} Central Krishi Mandi (4.5 km)",
        "weekly_haat_day": "Weekly Sunday Haat",
        "rural_tier": "R2 - Agrarian Commercial Corridor",
        "confidence": "Medium",
        "last_updated": "August 2026 (Synthesized Rural Demographic Profile)",
        "is_demo_data": True
    }


def generate_competitors_and_pois(
    lat: float,
    lng: float,
    business_key: str,
    village_name: str
) -> Dict[str, Any]:
    """
    Generates realistic competitor pins and local market points of interest (POIs)
    around the proposed enterprise location for Leaflet map rendering.
    """
    biz_info = BUSINESS_PROFILES.get(business_key, BUSINESS_PROFILES["dairy"])

    # Specific realistic competitor names based on sector
    if business_key == "dairy":
        comp_templates = [
            {"name": "Krishna Chilling Center", "scale": "Medium / 650 L/day", "dist": 1.8, "dx": 0.012, "dy": 0.009},
            {"name": "Mauli Milk Collection Point", "scale": "Small / 200 L/day", "dist": 3.2, "dx": -0.018, "dy": 0.015},
            {"name": "Gokul Sahakari Dairy Counter", "scale": "Medium / 800 L/day", "dist": 4.6, "dx": 0.024, "dy": -0.021},
            {"name": "Prabhat Bulk Milk Depot", "scale": "Large / 1,400 L/day", "dist": 6.1, "dx": -0.031, "dy": -0.019},
        ]
    elif business_key == "kirana":
        comp_templates = [
            {"name": "Shree Ganesh General Store", "scale": "Mini-Mart / 450 sq.ft", "dist": 0.8, "dx": 0.005, "dy": 0.004},
            {"name": "Balaji Daily Needs & Provisions", "scale": "Corner Store / 300 sq.ft", "dist": 1.4, "dx": -0.008, "dy": 0.007},
            {"name": "Ambika Kirana Bajar", "scale": "Wholesale Kirana / 700 sq.ft", "dist": 2.6, "dx": 0.015, "dy": -0.012},
        ]
    elif business_key == "food_processing":
        comp_templates = [
            {"name": "Kisan Flour & Spice Mill", "scale": "Atta Chakki / 20 HP", "dist": 2.4, "dx": 0.016, "dy": 0.011},
            {"name": "Sahyadri Oil Expeller Unit", "scale": "Cold Press / 30 HP", "dist": 5.8, "dx": -0.035, "dy": 0.022},
        ]
    elif business_key == "agri_input":
        comp_templates = [
            {"name": "Krishi Seva Kendra", "scale": "Govt Authorized Dealer", "dist": 1.9, "dx": 0.011, "dy": 0.014},
            {"name": "Kisan Beej & Khad Bhandar", "scale": "Private Stockist", "dist": 3.7, "dx": -0.022, "dy": -0.016},
        ]
    elif business_key == "poultry":
        comp_templates = [
            {"name": "Sai Broiler Farm Unit A", "scale": "Capacity 3,500 birds", "dist": 3.1, "dx": 0.021, "dy": -0.017},
            {"name": "Green Valley Layer Farm", "scale": "Capacity 5,000 birds", "dist": 6.4, "dx": -0.038, "dy": 0.029},
        ]
    else:
        comp_templates = [
            {"name": f"{village_name} Local Enterprise 1", "scale": "Small Unit", "dist": 1.5, "dx": 0.010, "dy": 0.008},
            {"name": f"{village_name} Local Enterprise 2", "scale": "Medium Unit", "dist": 3.8, "dx": -0.020, "dy": 0.016},
        ]

    competitors = []
    for c in comp_templates:
        competitors.append({
            "id": f"comp_{random.randint(1000, 9999)}",
            "name": c["name"],
            "scale": c["scale"],
            "distance_km": c["dist"],
            "lat": round(lat + c["dx"], 5),
            "lng": round(lng + c["dy"], 5),
            "status": "Operational",
            "threat_level": "Moderate" if c["dist"] < 3.0 else "Low"
        })

    # Local Points of Interest (Panchayat, Mandi, Weekly Haat)
    pois = [
        {
            "name": f"{village_name} Gram Panchayat & Digital Seva",
            "type": "Administrative / CSC",
            "distance_km": 0.6,
            "lat": round(lat + 0.003, 5),
            "lng": round(lng - 0.002, 5),
            "icon": "🏛️"
        },
        {
            "name": f"{village_name} Weekly Haat / Market Yard",
            "type": "Market Hub",
            "distance_km": 1.2,
            "lat": round(lat - 0.007, 5),
            "lng": round(lng + 0.006, 5),
            "icon": "🎪"
        },
        {
            "name": f"Regional Cooperative APMC Sub-Yard",
            "type": "Procurement / Mandi",
            "distance_km": 3.8,
            "lat": round(lat + 0.021, 5),
            "lng": round(lng + 0.018, 5),
            "icon": "🌾"
        }
    ]

    return {
        "competitors": competitors,
        "pois": pois,
        "center": {"lat": lat, "lng": lng},
        "catchment_radius_km": [5, 10]
    }


def get_hyper_local_market_analysis(
    state: str,
    district: str,
    block: str,
    village: str,
    business_category: str
) -> Dict[str, Any]:
    """
    Main aggregator for hyper-local feasibility intelligence.
    """
    biz_key = business_category.lower()
    if biz_key not in BUSINESS_PROFILES:
        biz_key = "dairy"

    biz_meta = BUSINESS_PROFILES[biz_key]
    loc_meta = resolve_location_metadata(state, district, block, village)
    map_geo = generate_competitors_and_pois(
        loc_meta["lat"],
        loc_meta["lng"],
        biz_key,
        loc_meta["village"]
    )

    # Calculate realistic population funnel
    total_pop = loc_meta["population"]
    # Dairy demo scenario target: 12,400 customers
    if biz_key == "dairy" and loc_meta["village"].lower() == "shirwal":
        target_customers = 12400
        daily_buyers = 3850
        viability_score = 78
        status = "GOOD POTENTIAL"
        demand_level = "HIGH"
        competition_level = "MODERATE"
    else:
        # Segment calculation
        if biz_key == "dairy":
            target_customers = int(total_pop * 0.295)
            daily_buyers = int(target_customers * 0.31)
            viability_score = 78
            status = "GOOD POTENTIAL"
            demand_level = "HIGH"
            competition_level = "MODERATE"
        elif biz_key == "kirana":
            target_customers = int(total_pop * 0.45)
            daily_buyers = int(target_customers * 0.22)
            viability_score = 72
            status = "MODERATE POTENTIAL"
            demand_level = "HIGH"
            competition_level = "HIGH"
        elif biz_key == "food_processing":
            target_customers = int(total_pop * 0.18)
            daily_buyers = int(target_customers * 0.15)
            viability_score = 84
            status = "VERY HIGH POTENTIAL"
            demand_level = "VERY HIGH"
            competition_level = "LOW"
        else:
            target_customers = int(total_pop * 0.25)
            daily_buyers = int(target_customers * 0.20)
            viability_score = 75
            status = "GOOD POTENTIAL"
            demand_level = biz_meta["default_demand"]
            competition_level = biz_meta["default_competition"]

    insights = {
        "summary": f"Demand appears favorable for {biz_meta['title'].lower()} within the selected market area.",
        "target_segment": biz_meta["target_audience"],
        "demand_indicator": (
            f"Strong recurrent demand supported by {target_customers:,} potential consumers "
            f"and active commercial transit along {loc_meta['block']} block."
        ),
        "purchasing_pattern": (
            "Daily morning and evening household procurement routines; predominant UPI and cash settlement; "
            "weekly surge corresponding with the local Thursday / Sunday haat."
        ),
        "market_opportunity": (
            f"Under-served catchment radius of {biz_meta['default_reach']} with an estimated addressable base "
            f"of {daily_buyers:,} regular buyers."
        ),
        "service_gap": (
            f"High customer preference for fresh, adulteration-free, locally procured supply "
            f"over packaged commercial alternatives transported from distant district centers."
        )
    }

    return {
        "location": loc_meta,
        "business": {
            "key": biz_key,
            "title": biz_meta["title"],
            "icon": biz_meta["icon"]
        },
        "viability_score": viability_score,
        "status": status,
        "metrics": {
            "target_customers": target_customers,
            "target_customers_formatted": f"{target_customers:,}",
            "market_reach": biz_meta["default_reach"],
            "local_demand": demand_level,
            "competition": competition_level
        },
        "confidence": loc_meta["confidence"],
        "last_updated": loc_meta["last_updated"],
        "is_demo_data": True,
        "demo_label": "Prototype / Demo Data",
        "insights": insights,
        "map_data": map_geo,
        "population_funnel": {
            "total_population": total_pop,
            "target_customers": target_customers,
            "addressable_daily_buyers": daily_buyers
        },
        "swot": biz_meta["swot"],
        "key_risk": biz_meta["key_risk"],
        "action_plan": biz_meta["action_plan"]
    }

