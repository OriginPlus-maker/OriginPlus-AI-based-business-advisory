"""
ORIGIN - Hyper-Local Rural Market Dataset & Demo Benchmarks
Contains realistic village, block, district benchmarks, competitor coordinates,
and market catchment statistics.
"""

from typing import Dict, Any, List


# Structured curated locations across prominent Indian states
LOCATIONS_DATABASE = [
    {
        "state": "Maharashtra",
        "district": "Satara",
        "block": "Khandala",
        "village": "Shirwal",
        "lat": 18.1328,
        "lng": 73.9822,
        "population": 42000,
        "households": 8600,
        "nearest_mandi": "Shirwal APMC Sub-Yard (1.5 km)",
        "weekly_haat_day": "Thursday",
        "rural_tier": "R2 - Developing Rural Industrial Corridor",
        "confidence": "High",
        "last_updated": "August 2026"
    },
    {
        "state": "Maharashtra",
        "district": "Pune",
        "block": "Baramati",
        "village": "Malegaon Budruk",
        "lat": 18.1534,
        "lng": 74.5778,
        "population": 36500,
        "households": 7400,
        "nearest_mandi": "Baramati Krishi Utpanna Bajar Samiti (6.2 km)",
        "weekly_haat_day": "Sunday",
        "rural_tier": "R1 - Progressive Agri-Cooperative Hub",
        "confidence": "High",
        "last_updated": "July 2026"
    },
    {
        "state": "Maharashtra",
        "district": "Kolhapur",
        "block": "Karveer",
        "village": "Shiroli",
        "lat": 16.7410,
        "lng": 74.2820,
        "population": 29800,
        "households": 6100,
        "nearest_mandi": "Kolhapur Shahu Market Yard (8.0 km)",
        "weekly_haat_day": "Wednesday",
        "rural_tier": "R2 - Peri-Urban Rural Hub",
        "confidence": "High",
        "last_updated": "August 2026"
    },
    {
        "state": "Uttar Pradesh",
        "district": "Chandauli",
        "block": "Niyamatabad",
        "village": "Tara Jivanpur",
        "lat": 25.2630,
        "lng": 83.1510,
        "population": 24000,
        "households": 4900,
        "nearest_mandi": "Mughalsarai Grain Mandi (5.4 km)",
        "weekly_haat_day": "Saturday",
        "rural_tier": "R3 - Traditional Agrarian Block",
        "confidence": "High",
        "last_updated": "August 2026"
    },
    {
        "state": "Bihar",
        "district": "Muzaffarpur",
        "block": "Kanti",
        "village": "Damodarpur",
        "lat": 26.1520,
        "lng": 85.3400,
        "population": 31000,
        "households": 6200,
        "nearest_mandi": "Kanti Krishi Mandi (3.8 km)",
        "weekly_haat_day": "Friday",
        "rural_tier": "R3 - Agri-Intensive Belt",
        "confidence": "Medium",
        "last_updated": "July 2026"
    },
    {
        "state": "Gujarat",
        "district": "Anand",
        "block": "Anand",
        "village": "Mogar",
        "lat": 22.5280,
        "lng": 72.9810,
        "population": 38000,
        "households": 7800,
        "nearest_mandi": "Anand APMC yard (7.1 km)",
        "weekly_haat_day": "Monday",
        "rural_tier": "R1 - Dairy Cooperative Capital",
        "confidence": "High",
        "last_updated": "August 2026"
    }
]

# Business categories benchmark profiles
BUSINESS_PROFILES = {
    "dairy": {
        "title": "Dairy & Milk Production",
        "icon": "🐄",
        "target_audience": "Rural and semi-urban households, local tea stalls, halwais, cooperative dairy collection points",
        "default_reach": "5–10 km",
        "default_demand": "HIGH",
        "default_competition": "MODERATE",
        "base_viability": 78,
        "swot": {
            "strengths": [
                "Continuous daily cash-flow with high recurring consumption",
                "Essential staple food product with price-inelastic rural demand",
                "Supportive cooperative procurement networks and bulk chilling points"
            ],
            "weaknesses": [
                "Perishable commodity requiring strict cold-chain and hygiene",
                "High dependency on continuous cattle feed quality and water supply",
                "Initial capital needed for quality milch cattle breeds"
            ],
            "opportunities": [
                "Value addition into curd (Dahi), paneer, ghee, and buttermilk with 30-45% higher margins",
                "Institutional bulk supply to nearby schools, hostels, and highway dhabas",
                "Organic cow dung manure & vermicompost monetization as agri-byproduct"
            ],
            "threats": [
                "Unseasonal green fodder shortages and feed-cost volatility",
                "Bovine disease risks and seasonal milk yield fluctuations",
                "Informal competition from unorganized local milk vendors"
            ]
        },
        "key_risk": "Feed-cost volatility & disease susceptibility during monsoon/summer transitions",
        "action_plan": [
            {"step": 1, "title": "Start at Manageable Scale", "desc": "Begin with 4-6 high-yielding milch animals (Gir/Murrah) in hygienic shed housing to stabilize initial operations."},
            {"step": 2, "title": "Establish Feed & Fodder Linkage", "desc": "Secure multi-cut green fodder tie-ups and wholesale silage storage to buffer against dry-season price spikes."},
            {"step": 3, "title": "Lock Direct Customer & Cooperative Routes", "desc": "Establish dual off-take: 50% direct retail (higher margin) and 50% dairy cooperative society (guaranteed liquidity)."},
            {"step": 4, "title": "Introduce Value-Added Products", "desc": "Deploy batch separator for daily curd, buttermilk, and weekly ghee to absorb surplus evening milk."},
            {"step": 5, "title": "Scale with Institutional Credit", "desc": "Utilize verified loan track record and banking discipline to expand herd size under supported scheme capital."}
        ]
    },
    "kirana": {
        "title": "Kirana & Provision Store",
        "icon": "🛒",
        "target_audience": "Village households, farm workers, passing rural traffic, school students",
        "default_reach": "2–5 km",
        "default_demand": "HIGH",
        "default_competition": "HIGH",
        "base_viability": 72,
        "swot": {
            "strengths": [
                "High inventory turn-around for essential grocery items",
                "Strong word-of-mouth trust and community relationship base",
                "Daily footfall driving steady operating revenue"
            ],
            "weaknesses": [
                "Working capital lockup in credit extended to local villagers (Udhaar)",
                "Tight profit margins on branded packaged FMCG commodities",
                "Limited shelf life on seasonal confectionery and bakery goods"
            ],
            "opportunities": [
                "Digitization via UPI, micro-ATM, bill payments, and recharge point",
                "Stocking agro-poultry essentials and bulk festival packages",
                "Direct tie-up with regional wholesale distributors for 3-5% margin bonus"
            ],
            "threats": [
                "Proliferation of mini-stores within the same village mohalla",
                "Bad debt risk from unrecovered agricultural credit during lean crop cycles",
                "Rising transport logistics cost from taluka mandi"
            ]
        },
        "key_risk": "Working capital depletion due to unmanaged local customer credit cycles",
        "action_plan": [
            {"step": 1, "title": "Prime Location & Store Layout", "desc": "Secure a prominent spot near village chowk or bus stop with clear visibility and clean shelving."},
            {"step": 2, "title": "Curate High-Turnover Inventory", "desc": "Stock top 80 fast-moving staple SKUs (flour, oil, pulses, spices, soaps) before expanding."},
            {"step": 3, "title": "Deploy Digital Ledger & Payments", "desc": "Enforce strict credit limits (<15% of working capital) using digital khatabook and UPI QR displays."},
            {"step": 4, "title": "Add High-Margin Value Services", "desc": "Introduce Xerox, mobile top-ups, and daily eggs/dairy packets to multiply daily footfalls."},
            {"step": 5, "title": "Bulk Sourcing Advantage", "desc": "Join local merchant purchasing groups to unlock volume tier discounts from district wholesalers."}
        ]
    },
    "food_processing": {
        "title": "Food Processing & Milling Unit",
        "icon": "🍱",
        "target_audience": "Local farmers seeking primary processing, regional sweet shops, weekly haat vendors, urban packaged food buyers",
        "default_reach": "10–20 km",
        "default_demand": "VERY HIGH",
        "default_competition": "LOW",
        "base_viability": 84,
        "swot": {
            "strengths": [
                "Immediate proximity to raw crop produce at farm-gate prices",
                "Significant value-addition multiplier (40% to 70% gross margins)",
                "High eligibility for central and state agro-processing subsidies (PMFME)"
            ],
            "weaknesses": [
                "Requires stable three-phase rural electricity and water infrastructure",
                "Seasonal raw material availability necessitating storage planning",
                "FSSAI and quality packaging standard compliance requirements"
            ],
            "opportunities": [
                "Primary processing: flour milling, cold-press oil, pulse grading, turmeric grinding",
                "Contract packaging for regional retail brands and Farmer Producer Orgs (FPOs)",
                "Supplying processed ingredients to taluka bakeries and catering operators"
            ],
            "threats": [
                "Severe crop yield shocks caused by unseasonal monsoon disruptions",
                "Power tariff fluctuations and rural load-shedding schedules",
                "Adulteration enforcement and stringent perishable inspection"
            ]
        },
        "key_risk": "Seasonal crop supply variation and unbuffered electricity outages",
        "action_plan": [
            {"step": 1, "title": "Verify Power Infrastructure", "desc": "Ensure dedicated rural three-phase supply line and backup diesel generator capacity."},
            {"step": 2, "title": "Contract Local Farmer Supply", "desc": "Sign pre-harvest supply agreements with local farmers for raw mustard, grains, or spices."},
            {"step": 3, "title": "Acquire Quality Food Certification", "desc": "Complete basic FSSAI registration and install stainless-steel processing machinery."},
            {"step": 4, "title": "Build Regional B2B Channels", "desc": "Partner with 15-20 kirana stores and weekly markets in neighbouring blocks."},
            {"step": 5, "title": "Leverage Government Processing Subsidy", "desc": "Submit DPR under PMFME for 35% credit-linked capital subsidy."}
        ]
    },
    "agri_input": {
        "title": "Agri Input & Seed Fertilizer Store",
        "icon": "🌾",
        "target_audience": "Smallholder farmers, progressive horticulturists, polyhouse operators",
        "default_reach": "10–15 km",
        "default_demand": "HIGH",
        "default_competition": "MODERATE",
        "base_viability": 81,
        "swot": {
            "strengths": [
                "Inelastic demand during Kharif and Rabi sowing seasons",
                "High ticket size per farmer transaction during sowing window",
                "Strong government emphasis on certified seeds and soil nutrients"
            ],
            "weaknesses": [
                "Mandatory statutory licensing requirements (Agriculture Department)",
                "Severe revenue seasonality concentrated in 4-5 key agricultural months",
                "High working capital required for pre-season inventory stockpiling"
            ],
            "opportunities": [
                "Advisory-led sales: soil testing kits, micro-nutrients, organic bio-fertilizers",
                "Drip irrigation fittings, solar pump spares, and spray equipment rentals",
                "Tie-ups with leading seed companies (Kaveri, Mahyco, Rasi) for dealership rights"
            ],
            "threats": [
                "Monsoon delays depressing overall sowing acreage",
                "Spurious product liabilities and strict state seed inspection inspections",
                "Delayed subsidy disbursements on regulated urea/DAP fertilizers"
            ]
        },
        "key_risk": "Inventory obsolescence if monsoon failure postpones targeted sowing cycles",
        "action_plan": [
            {"step": 1, "title": "Secure Necessary Dealer Licenses", "desc": "Obtain mandatory seed, fertilizer, and pesticide dealership clearance from District Krishi Bhavan."},
            {"step": 2, "title": "Setup Balanced Seasonal Inventory", "desc": "Procure certified hybrid seeds and fast-acting micronutrient boosters 45 days ahead of monsoon."},
            {"step": 3, "title": "Provide Agronomic Advisory", "desc": "Offer free guidance on soil health and pest management to build lasting farmer loyalty."},
            {"step": 4, "title": "Diversify into Non-Seasonal Gear", "desc": "Stock spray pumps, tarpaulins, mulching sheets, and pruning tools to sustain year-round cash flow."},
            {"step": 5, "title": "Digitize Farmer Records", "desc": "Maintain Aadhaar-linked inventory ledgers to ensure smooth government compliance."}
        ]
    },
    "poultry": {
        "title": "Poultry & Broiler Farming",
        "icon": "🐔",
        "target_audience": "Rural and semi-urban chicken retailers, highway dhabas, local egg consumers",
        "default_reach": "10–25 km",
        "default_demand": "HIGH",
        "default_competition": "MODERATE",
        "base_viability": 76,
        "swot": {
            "strengths": [
                "Short production lifecycle (broiler birds mature in 35-42 days)",
                "High protein demand across rural and semi-urban demographics",
                "Predictable turnkey contract farming models available from integrators"
            ],
            "weaknesses": [
                "Extremely vulnerable to avian influenza and heat-wave bird mortality",
                "High feed costs representing up to 70% of operational expenditure",
                "Heavy odor and waste management requiring isolated shed land"
            ],
            "opportunities": [
                "Contract farming with established integrators (Suguna, Venky's) minimizing price risk",
                "Monetizing deep-litter poultry manure as rich organic nitrogen fertilizer",
                "Local direct retail counter eliminating middleman commission"
            ],
            "threats": [
                "Epidemic disease outbreaks and sudden bird flu rumors",
                "Surge in soy meal and maize commodity prices",
                "Intense summer temperatures causing high bird mortality without climate control"
            ]
        },
        "key_risk": "Summer heat stress and feed-grain price spikes",
        "action_plan": [
            {"step": 1, "title": "Construct Biosecure Poultry Shed", "desc": "Build an elevated, well-ventilated shed with foggers and curtains situated 500m from residences."},
            {"step": 2, "title": "Choose Operational Model", "desc": "Evaluate contract integration (zero market risk) vs independent farming (higher upside)."},
            {"step": 3, "title": "Establish Stringent Biosecurity", "desc": "Enforce strict vaccination protocols, footbaths, and controlled entry to prevent disease spread."},
            {"step": 4, "title": "Optimize Feed Conversion Ratio (FCR)", "desc": "Monitor daily weight gain aiming for FCR under 1.6 kg feed per kg live bird."},
            {"step": 5, "title": "Diversify Revenue Channels", "desc": "Package and sell dry bird manure to nearby grape/sugarcane orchards for extra income."}
        ]
    },
    "rural_retail": {
        "title": "Rural Retail & Hardware Store",
        "icon": "🏪",
        "target_audience": "Village residents, local masonry workers, farmers, plumbers, electricians",
        "default_reach": "5–12 km",
        "default_demand": "MODERATE",
        "default_competition": "LOW",
        "base_viability": 75,
        "swot": {
            "strengths": [
                "High customer loyalty due to distance to district headquarters",
                "Attractive gross profit margins on construction hardware and fittings (25-35%)",
                "Consistent demand driven by rural housing schemes (PMAY-Gramin)"
            ],
            "weaknesses": [
                "Slower inventory turnover compared to daily grocery staples",
                "Substantial initial capital tied up in bulky hardware and plumbing inventory",
                "Requires adequate secure storage space for cement, steel, and PVC pipes"
            ],
            "opportunities": [
                "PMAY housing boom creating continuous demand for cement, sanitaryware, and paints",
                "Agricultural plumbing essentials: PVC pipes, submersible fittings, drip repair kits",
                "Tie-ups with local village masons and contractors through trade incentives"
            ],
            "threats": [
                "Competition from larger hardware suppliers at taluka town centers",
                "Price volatility in steel and cement manufacturer rates",
                "Working capital strain from delayed payments on large construction orders"
            ]
        },
        "key_risk": "Capital lockup in slow-moving non-standard hardware items",
        "action_plan": [
            {"step": 1, "title": "Focus on High-Demand Essentials", "desc": "Stock fast-moving plumbing fixtures, electrical switches, cement bags, and standard fasteners."},
            {"step": 2, "title": "Partner with Local Tradespeople", "desc": "Engage village electricians, plumbers, and masons as referral champions with small volume discounts."},
            {"step": 3, "title": "Negotiate Consignment Credit", "desc": "Obtain 30-day supplier credit terms from regional distributors for pipe and paint lines."},
            {"step": 4, "title": "Add Tool Rental Service", "desc": "Rent out drills, concrete mixers, and sprayers for extra daily rental cash flow."},
            {"step": 5, "title": "Maintain Transparent Pricing", "desc": "Display clear price boards to eliminate haggling and build long-term trustworthiness."}
        ]
    }
}

