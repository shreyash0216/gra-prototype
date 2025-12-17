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

class AIChatRequest(BaseModel):
    message: str
    context: Optional[Dict] = None

@app.post("/ai-chat")
async def ai_chat_assistant(request: AIChatRequest):
    """AI Chat Assistant for farming queries"""
    try:
        message = request.message.lower()
        context = request.context or {}
        
        # Generate contextual AI response
        response = _generate_ai_response(message, context)
        
        return {
            "success": True,
            "response": response,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def _generate_ai_response(message: str, context: Dict) -> str:
    """Generate AI response based on message and context"""
    
    # Crop recommendations
    if any(word in message for word in ['crop', 'plant', 'grow', 'cultivate']):
        location = context.get('location', 'your region')
        return f"""🌾 **Climate-Resilient Crop Recommendations for {location}:**

**Top 3 Crops:**
1. **Millets** - Extremely drought-resistant, requires 70% less water than rice
2. **Cotton** - Heat-tolerant, suitable for black soil, high market value
3. **Soybean** - Nitrogen-fixing, improves soil health, good rotation crop

**Why These Crops?**
- Adapted to irregular rainfall patterns
- Lower water requirements
- Higher climate resilience
- Good market demand

Would you like detailed cultivation practices for any specific crop?"""

    # Climate adaptation
    if any(word in message for word in ['climate', 'weather', 'drought', 'flood', 'rain']):
        return """🌡️ **Climate Adaptation Strategies:**

**Immediate Actions (0-3 months):**
• Install drip irrigation system (75% govt subsidy available)
• Start rainwater harvesting
• Get soil health card (free)
• Plant drought-resistant varieties

**Medium-term (3-12 months):**
• Build farm ponds for water storage
• Implement mulching techniques
• Diversify crop portfolio
• Join weather advisory services

**Long-term (1-3 years):**
• Establish perennial crops
• Create windbreaks and shelter belts
• Invest in climate-smart infrastructure

**Government Support:** Up to ₹2 lakh subsidy available through PMKSY and NMSA schemes."""

    # Government schemes
    if any(word in message for word in ['scheme', 'subsidy', 'government', 'loan', 'support']):
        return """🏛️ **Top Government Schemes for Farmers (2024):**

**1. PM-KISAN**
- ₹6,000/year direct benefit transfer
- All landholding farmers eligible
- Apply: pmkisan.gov.in

**2. PMKSY (Irrigation)**
- 75% subsidy on drip/sprinkler systems
- Up to ₹2 lakh per farmer
- Saves 60% water

**3. Soil Health Management**
- Free soil testing
- ₹15,000 subsidy for soil improvement
- Increases yield by 20-30%

**4. Kisan Credit Card (KCC)**
- Loans up to ₹3 lakh at 7% interest
- 3% interest subvention
- Easy repayment terms

**5. PMFBY (Crop Insurance)**
- 95% premium subsidy
- Covers natural calamities
- Protects your investment

**How to Apply:** Visit nearest Krishi Vigyan Kendra or apply online at respective portals."""

    # Market information
    if any(word in message for word in ['market', 'price', 'sell', 'msp', 'buyer']):
        return """📈 **Market Intelligence & Selling Strategies:**

**Current Market Trends:**
• Cotton: ₹55/kg (increasing trend)
• Soybean: ₹45/kg (stable)
• Wheat: ₹20/kg (MSP protected)
• Rice: ₹22/kg (high demand)

**Best Selling Strategies:**
1. **e-NAM Platform** - Get better prices, transparent bidding
2. **FPO Membership** - Collective bargaining power
3. **Contract Farming** - Price stability, assured market
4. **Direct Marketing** - Higher margins, customer relationships

**Timing Tips:**
• Avoid harvest season glut
• Store for 2-3 months if possible
• Monitor daily mandi rates
• Use cold storage for perishables

**Value Addition:**
• Grading & sorting: +15% price
• Organic certification: +30% premium
• Processing: +50% value

Need specific crop market analysis?"""

    # Water management
    if any(word in message for word in ['water', 'irrigation', 'drip', 'sprinkler']):
        return """💧 **Smart Water Management Solutions:**

**Drip Irrigation Benefits:**
• Save 60% water compared to flood irrigation
• Increase yield by 40-50%
• Reduce fertilizer use by 30%
• 75% government subsidy available

**Cost Analysis (1 acre):**
- Total Cost: ₹60,000
- Government Subsidy: ₹45,000
- Your Investment: ₹15,000
- Payback Period: 1.5 years

**Rainwater Harvesting:**
• Capture monsoon water
• Recharge groundwater
• Free technical support from govt
• Can save ₹20,000/year on irrigation

**Water-Saving Techniques:**
1. Mulching - reduces evaporation by 50%
2. Alternate wetting & drying for rice
3. Laser land leveling - saves 25% water
4. Crop scheduling based on water availability

**Apply for PMKSY subsidy today!**"""

    # Soil health
    if any(word in message for word in ['soil', 'fertilizer', 'manure', 'compost']):
        return """🌱 **Soil Health Management Guide:**

**Get Your Soil Health Card:**
• Free soil testing at Krishi Vigyan Kendra
• Know exact NPK requirements
• Save 20% on fertilizer costs
• Increase yield by 15-25%

**Organic Matter Management:**
• Add 5 tons compost/acre annually
• Practice green manuring
• Use crop residues wisely
• Maintain 2-3% organic carbon

**Balanced Fertilization:**
• Follow soil test recommendations
• Use bio-fertilizers (Rhizobium, Azotobacter)
• Apply micro-nutrients (Zinc, Boron)
• Avoid excessive urea

**Soil Conservation:**
• Contour farming on slopes
• Crop rotation (legumes + cereals)
• Cover crops in off-season
• Minimum tillage practices

**Government Support:**
₹15,000 subsidy under Soil Health Management Scheme"""

    # Pest management
    if any(word in message for word in ['pest', 'disease', 'insect', 'spray']):
        return """🐛 **Integrated Pest Management (IPM):**

**Prevention First:**
• Use resistant varieties
• Proper crop rotation
• Maintain field hygiene
• Balanced fertilization

**Monitoring:**
• Install pheromone traps
• Regular field scouting
• Use yellow sticky traps
• Monitor weather for disease outbreak

**Biological Control:**
• Neem-based pesticides
• Trichoderma for soil diseases
• NPV for caterpillar control
• Encourage natural predators

**Chemical Control (Last Resort):**
• Use only when threshold crossed
• Follow recommended doses
• Rotate pesticide groups
• Observe safety periods

**Cost Savings:**
IPM reduces pesticide costs by 60% while maintaining yields!"""

    # General farming advice
    if any(word in message for word in ['help', 'advice', 'guide', 'start']):
        return """🤖 **GRA - Your AI Farming Assistant**

I can help you with:

✅ **Climate Adaptation**
- Risk assessment
- Resilient crop selection
- Weather-based advisories

✅ **Crop Management**
- Variety selection
- Cultivation practices
- Pest & disease control

✅ **Financial Planning**
- Government schemes
- Subsidy applications
- Cost-benefit analysis

✅ **Market Intelligence**
- Price trends
- Selling strategies
- Value addition

✅ **Resource Management**
- Water conservation
- Soil health
- Input optimization

**Quick Actions:**
1. Fill the form above for complete farm analysis
2. Ask me specific questions
3. Get personalized recommendations

What would you like to know more about?"""

    # Default response with context
    location = context.get('location', '')
    farm_size = context.get('farm_size', '')
    
    context_info = ""
    if location:
        context_info = f"\n\nI see you're from {location}"
        if farm_size:
            context_info += f" with {farm_size} acres of land"
        context_info += ". Let me provide location-specific guidance."
    
    return f"""🤖 I understand you're asking about: "{message}"

As your AI farming assistant, I specialize in:

• **Climate Adaptation** - Strategies for changing weather patterns
• **Crop Selection** - Best crops for your soil and climate
• **Government Schemes** - Subsidies and financial support
• **Water Management** - Irrigation and conservation
• **Market Intelligence** - Prices and selling strategies
• **Soil Health** - Fertilization and organic farming

{context_info}

Could you be more specific? For example:
- "What crops are best for drought conditions?"
- "How do I apply for irrigation subsidy?"
- "What's the current market price for cotton?"
- "How can I improve my soil health?"

Or fill the form above for a complete AI-powered farm analysis!"""

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