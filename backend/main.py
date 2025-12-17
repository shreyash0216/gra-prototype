from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
# StaticFiles not needed for this setup
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uvicorn
import os
from datetime import datetime

from database.models import Base, engine, get_db
from database.crud import ClimateAdaptationCRUD
from agents.climate_analyzer import ClimateAnalyzer
from agents.crop_advisor import CropAdvisor
from agents.market_analyzer import MarketAnalyzer
from agents.scheme_finder import SchemeFinder
from utils.svg_generator import SVGGenerator

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Climate Adaptation System", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files will be served by the frontend directly

# Initialize components
climate_analyzer = ClimateAnalyzer()
crop_advisor = CropAdvisor()
market_analyzer = MarketAnalyzer()
scheme_finder = SchemeFinder()
svg_generator = SVGGenerator()

# Pydantic models
class FarmDetails(BaseModel):
    location: str
    farm_size: float
    soil_type: str
    water_source: str
    current_crops: List[str]
    budget: float
    experience_level: str

class ClimateAdaptationRequest(BaseModel):
    farm_details: FarmDetails
    climate_concerns: List[str]
    adaptation_goals: List[str]

class NearbyFarmQuery(BaseModel):
    location: str
    radius_km: float = 10.0

@app.get("/")
async def root():
    return {"message": "Climate Adaptation System API", "version": "1.0.0"}

@app.post("/analyze-climate")
async def analyze_climate_adaptation(
    request: ClimateAdaptationRequest,
    db = Depends(get_db)
):
    """Generate comprehensive climate adaptation plan for a farm"""
    try:
        crud = ClimateAdaptationCRUD(db)
        
        # Step 1: Climate Risk Analysis
        climate_analysis = await climate_analyzer.analyze_risks(
            location=request.farm_details.location,
            concerns=request.climate_concerns
        )
        
        # Step 2: Crop Recommendations
        crop_recommendations = await crop_advisor.recommend_crops(
            farm_details=request.farm_details.dict(),
            climate_risks=climate_analysis["risks"]
        )
        
        # Step 3: Market Analysis
        market_analysis = await market_analyzer.analyze_market_potential(
            crops=crop_recommendations["recommended_crops"],
            location=request.farm_details.location
        )
        
        # Step 4: Government Schemes
        available_schemes = await scheme_finder.find_relevant_schemes(
            farm_details=request.farm_details.dict(),
            adaptation_goals=request.adaptation_goals
        )
        
        # Step 5: Generate Farm Layout
        farm_layout = svg_generator.generate_farm_layout(
            farm_size=request.farm_details.farm_size,
            recommended_crops=crop_recommendations["recommended_crops"],
            water_source=request.farm_details.water_source
        )
        
        # Compile comprehensive plan
        adaptation_plan = {
            "farm_id": f"farm_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "climate_analysis": climate_analysis,
            "crop_recommendations": crop_recommendations,
            "market_analysis": market_analysis,
            "government_schemes": available_schemes,
            "farm_layout_svg": farm_layout,
            "implementation_timeline": _generate_timeline(
                crop_recommendations, climate_analysis
            ),
            "estimated_costs": _calculate_costs(
                crop_recommendations, available_schemes
            ),
            "expected_benefits": _calculate_benefits(
                crop_recommendations, market_analysis
            )
        }
        
        # Save to database
        saved_plan = crud.create_adaptation_plan(
            farm_details=request.farm_details.dict(),
            adaptation_plan=adaptation_plan
        )
        
        return {
            "success": True,
            "plan_id": saved_plan.id,
            "adaptation_plan": adaptation_plan
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/nearby-farms")
async def get_nearby_farm_plans(
    query: NearbyFarmQuery,
    db = Depends(get_db)
):
    """Find adaptation plans from nearby farms"""
    try:
        crud = ClimateAdaptationCRUD(db)
        
        nearby_plans = crud.get_nearby_plans(
            location=query.location,
            radius_km=query.radius_km
        )
        
        return {
            "success": True,
            "nearby_plans": nearby_plans,
            "count": len(nearby_plans)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/plan/{plan_id}")
async def get_adaptation_plan(plan_id: int, db = Depends(get_db)):
    """Retrieve a specific adaptation plan"""
    try:
        crud = ClimateAdaptationCRUD(db)
        plan = crud.get_plan_by_id(plan_id)
        
        if not plan:
            raise HTTPException(status_code=404, detail="Plan not found")
        
        return {
            "success": True,
            "plan": plan
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/crops")
async def get_crop_database():
    """Get available crops database"""
    try:
        from data.knowledge_base import get_crops_data
        crops = get_crops_data()
        return {"success": True, "crops": crops}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/schemes")
async def get_government_schemes():
    """Get available government schemes"""
    try:
        from data.knowledge_base import get_schemes_data
        schemes = get_schemes_data()
        return {"success": True, "schemes": schemes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def _generate_timeline(crop_recommendations: Dict, climate_analysis: Dict) -> List[Dict]:
    """Generate implementation timeline"""
    timeline = []
    
    # Immediate actions (0-3 months)
    timeline.append({
        "phase": "Immediate (0-3 months)",
        "actions": [
            "Soil testing and preparation",
            "Water source assessment",
            "Seed procurement for recommended crops"
        ]
    })
    
    # Short-term (3-12 months)
    timeline.append({
        "phase": "Short-term (3-12 months)",
        "actions": [
            "Plant climate-resilient crops",
            "Install water conservation systems",
            "Apply for government schemes"
        ]
    })
    
    # Long-term (1-3 years)
    timeline.append({
        "phase": "Long-term (1-3 years)",
        "actions": [
            "Establish perennial crops",
            "Build climate-resilient infrastructure",
            "Diversify income sources"
        ]
    })
    
    return timeline

def _calculate_costs(crop_recommendations: Dict, schemes: Dict) -> Dict:
    """Calculate estimated implementation costs"""
    base_cost = len(crop_recommendations.get("recommended_crops", [])) * 15000
    
    return {
        "total_estimated_cost": base_cost,
        "government_subsidy": base_cost * 0.4,
        "farmer_contribution": base_cost * 0.6,
        "breakdown": {
            "seeds_and_inputs": base_cost * 0.3,
            "infrastructure": base_cost * 0.5,
            "training_and_support": base_cost * 0.2
        }
    }

def _calculate_benefits(crop_recommendations: Dict, market_analysis: Dict) -> Dict:
    """Calculate expected benefits"""
    return {
        "increased_yield": "25-40%",
        "reduced_risk": "60%",
        "income_improvement": "30-50%",
        "sustainability_score": "85%",
        "climate_resilience": "High"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)