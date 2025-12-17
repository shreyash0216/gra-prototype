"""
Knowledge base for climate adaptation system
Contains crop data, market information, and government schemes
"""

def get_crops_data():
    """Get comprehensive crop database"""
    return [
        {
            "name": "Rice",
            "category": "food_grain",
            "climate_zones": ["tropical", "subtropical"],
            "soil_types": ["clay", "loamy"],
            "water_requirement": "high",
            "season": "kharif",
            "planting_months": ["june", "july"],
            "growth_duration_days": 120,
            "yield_per_acre_kg": 2500,
            "market_price_per_kg": 22,
            "input_cost_per_acre": 25000,
            "risk_tolerance": {
                "drought": "low",
                "flooding": "high",
                "heat_waves": "medium",
                "irregular_rainfall": "medium"
            }
        },
        {
            "name": "Wheat",
            "category": "food_grain",
            "climate_zones": ["temperate", "subtropical"],
            "soil_types": ["loamy", "sandy"],
            "water_requirement": "medium",
            "season": "rabi",
            "planting_months": ["november", "december"],
            "growth_duration_days": 150,
            "yield_per_acre_kg": 2000,
            "market_price_per_kg": 20,
            "input_cost_per_acre": 20000,
            "risk_tolerance": {
                "drought": "medium",
                "flooding": "low",
                "heat_waves": "low",
                "temperature_fluctuations": "high"
            }
        },
        {
            "name": "Cotton",
            "category": "cash_crop",
            "climate_zones": ["tropical", "subtropical"],
            "soil_types": ["black", "loamy"],
            "water_requirement": "medium",
            "season": "kharif",
            "planting_months": ["may", "june"],
            "growth_duration_days": 180,
            "yield_per_acre_kg": 500,
            "market_price_per_kg": 55,
            "input_cost_per_acre": 30000,
            "risk_tolerance": {
                "drought": "high",
                "heat_waves": "high",
                "irregular_rainfall": "high",
                "pest_attacks": "medium"
            }
        },
        {
            "name": "Sugarcane",
            "category": "cash_crop",
            "climate_zones": ["tropical", "subtropical"],
            "soil_types": ["loamy", "clay"],
            "water_requirement": "high",
            "season": "both",
            "planting_months": ["february", "march", "october"],
            "growth_duration_days": 365,
            "yield_per_acre_kg": 50000,
            "market_price_per_kg": 3,
            "input_cost_per_acre": 40000,
            "risk_tolerance": {
                "drought": "low",
                "flooding": "medium",
                "heat_waves": "medium",
                "water_scarcity": "low"
            }
        },
        {
            "name": "Soybean",
            "category": "oilseed",
            "climate_zones": ["tropical", "subtropical"],
            "soil_types": ["black", "loamy"],
            "water_requirement": "medium",
            "season": "kharif",
            "planting_months": ["june", "july"],
            "growth_duration_days": 100,
            "yield_per_acre_kg": 1200,
            "market_price_per_kg": 45,
            "input_cost_per_acre": 18000,
            "risk_tolerance": {
                "drought": "high",
                "irregular_rainfall": "high",
                "heat_waves": "medium",
                "soil_degradation": "low"
            }
        },
        {
            "name": "Maize",
            "category": "food_grain",
            "climate_zones": ["tropical", "temperate"],
            "soil_types": ["loamy", "sandy"],
            "water_requirement": "medium",
            "season": "both",
            "planting_months": ["june", "november"],
            "growth_duration_days": 90,
            "yield_per_acre_kg": 2200,
            "market_price_per_kg": 18,
            "input_cost_per_acre": 15000,
            "risk_tolerance": {
                "drought": "medium",
                "heat_waves": "high",
                "irregular_rainfall": "medium",
                "temperature_fluctuations": "high"
            }
        },
        {
            "name": "Tomato",
            "category": "vegetable",
            "climate_zones": ["tropical", "subtropical"],
            "soil_types": ["loamy", "sandy"],
            "water_requirement": "high",
            "season": "both",
            "planting_months": ["june", "november"],
            "growth_duration_days": 75,
            "yield_per_acre_kg": 15000,
            "market_price_per_kg": 35,
            "input_cost_per_acre": 35000,
            "risk_tolerance": {
                "heat_waves": "low",
                "irregular_rainfall": "low",
                "pest_attacks": "low",
                "flooding": "low"
            }
        },
        {
            "name": "Onion",
            "category": "vegetable",
            "climate_zones": ["tropical", "subtropical"],
            "soil_types": ["loamy", "sandy"],
            "water_requirement": "medium",
            "season": "both",
            "planting_months": ["june", "november"],
            "growth_duration_days": 120,
            "yield_per_acre_kg": 8000,
            "market_price_per_kg": 28,
            "input_cost_per_acre": 25000,
            "risk_tolerance": {
                "drought": "medium",
                "heat_waves": "medium",
                "irregular_rainfall": "medium",
                "flooding": "low"
            }
        },
        {
            "name": "Millets",
            "category": "food_grain",
            "climate_zones": ["arid", "semi_arid"],
            "soil_types": ["sandy", "loamy"],
            "water_requirement": "low",
            "season": "kharif",
            "planting_months": ["june", "july"],
            "growth_duration_days": 75,
            "yield_per_acre_kg": 800,
            "market_price_per_kg": 35,
            "input_cost_per_acre": 8000,
            "risk_tolerance": {
                "drought": "very_high",
                "heat_waves": "very_high",
                "irregular_rainfall": "very_high",
                "water_scarcity": "very_high"
            }
        },
        {
            "name": "Groundnut",
            "category": "oilseed",
            "climate_zones": ["tropical", "subtropical"],
            "soil_types": ["sandy", "loamy"],
            "water_requirement": "medium",
            "season": "both",
            "planting_months": ["june", "november"],
            "growth_duration_days": 110,
            "yield_per_acre_kg": 1500,
            "market_price_per_kg": 50,
            "input_cost_per_acre": 20000,
            "risk_tolerance": {
                "drought": "high",
                "heat_waves": "high",
                "irregular_rainfall": "high",
                "soil_degradation": "medium"
            }
        }
    ]

def get_market_data():
    """Get market data for crops"""
    return {
        "price_trends": {
            "rice": {"current": 22, "trend": "stable", "volatility": "low"},
            "wheat": {"current": 20, "trend": "increasing", "volatility": "low"},
            "cotton": {"current": 55, "trend": "volatile", "volatility": "high"},
            "soybean": {"current": 45, "trend": "increasing", "volatility": "medium"}
        },
        "demand_patterns": {
            "food_grains": "consistent_high",
            "cash_crops": "market_dependent",
            "vegetables": "seasonal_high",
            "oilseeds": "increasing"
        }
    }

def get_schemes_data():
    """Get government schemes database"""
    return [
        {
            "name": "Pradhan Mantri Krishi Sinchai Yojana (PMKSY)",
            "description": "Irrigation infrastructure development and water conservation",
            "categories": ["water_management", "infrastructure"],
            "objectives": [
                "Expand cultivated area under assured irrigation",
                "Improve water use efficiency",
                "Promote precision irrigation"
            ],
            "subsidy": {
                "amount": 75000,
                "percentage": 75,
                "max_limit": 200000
            },
            "eligibility": {
                "farm_size": {"min": 0.5, "max": 10},
                "states": []  # National scheme
            },
            "application": {
                "period": "April-September",
                "complexity": "medium",
                "processing_days": 45
            },
            "required_documents": [
                "Land Records (7/12, 8A)",
                "Aadhaar Card",
                "Bank Account Details",
                "Water Source Certificate"
            ]
        },
        {
            "name": "Soil Health Management Scheme",
            "description": "Soil testing and health improvement initiatives",
            "categories": ["soil_management", "crop_development"],
            "objectives": [
                "Promote soil health through soil health cards",
                "Encourage balanced use of fertilizers",
                "Improve soil organic content"
            ],
            "subsidy": {
                "amount": 15000,
                "percentage": 100,
                "max_limit": 25000
            },
            "eligibility": {
                "farm_size": {"min": 0, "max": float('inf')},
                "states": []
            },
            "application": {
                "period": "Year-round",
                "complexity": "easy",
                "processing_days": 15
            },
            "required_documents": [
                "Land Records",
                "Aadhaar Card",
                "Soil Health Card"
            ]
        },
        {
            "name": "National Mission for Sustainable Agriculture (NMSA)",
            "description": "Climate resilient agriculture and sustainable farming practices",
            "categories": ["climate_adaptation", "sustainable_farming"],
            "objectives": [
                "Promote climate resilient agriculture",
                "Enhance soil health and water conservation",
                "Mainstream rainfed area development"
            ],
            "subsidy": {
                "amount": 50000,
                "percentage": 60,
                "max_limit": 100000
            },
            "eligibility": {
                "farm_size": {"min": 1, "max": 20},
                "states": []
            },
            "application": {
                "period": "March-August",
                "complexity": "medium",
                "processing_days": 60
            },
            "required_documents": [
                "Land Records",
                "Aadhaar Card",
                "Bank Account Details",
                "Project Proposal"
            ]
        },
        {
            "name": "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
            "description": "Crop insurance scheme for risk mitigation",
            "categories": ["insurance", "risk_management"],
            "objectives": [
                "Provide insurance coverage for crops",
                "Stabilize income of farmers",
                "Encourage adoption of innovative practices"
            ],
            "subsidy": {
                "amount": 20000,
                "percentage": 95,
                "max_limit": 50000
            },
            "eligibility": {
                "farm_size": {"min": 0, "max": float('inf')},
                "states": []
            },
            "application": {
                "period": "Before sowing season",
                "complexity": "easy",
                "processing_days": 7
            },
            "required_documents": [
                "Land Records",
                "Aadhaar Card",
                "Bank Account Details",
                "Sowing Certificate"
            ]
        },
        {
            "name": "Kisan Credit Card (KCC)",
            "description": "Credit support for agricultural activities",
            "categories": ["credit_support", "finance"],
            "objectives": [
                "Provide adequate and timely credit",
                "Meet consumption requirements",
                "Support post-harvest expenses"
            ],
            "loan": {
                "amount": 300000,
                "interest_rate": 7,
                "tenure_years": 5
            },
            "eligibility": {
                "farm_size": {"min": 0, "max": float('inf')},
                "states": []
            },
            "application": {
                "period": "Year-round",
                "complexity": "easy",
                "processing_days": 15
            },
            "required_documents": [
                "Land Records",
                "Aadhaar Card",
                "Bank Account Details",
                "Income Certificate"
            ]
        },
        {
            "name": "Sub-Mission on Agricultural Mechanization (SMAM)",
            "description": "Promote farm mechanization for efficient farming",
            "categories": ["mechanization", "technology"],
            "objectives": [
                "Increase reach of farm mechanization",
                "Promote custom hiring centers",
                "Create awareness on farm machinery"
            ],
            "subsidy": {
                "amount": 80000,
                "percentage": 50,
                "max_limit": 150000
            },
            "eligibility": {
                "farm_size": {"min": 2, "max": 50},
                "states": []
            },
            "application": {
                "period": "April-October",
                "complexity": "medium",
                "processing_days": 30
            },
            "required_documents": [
                "Land Records",
                "Aadhaar Card",
                "Bank Account Details",
                "Machinery Quotation"
            ]
        }
    ]