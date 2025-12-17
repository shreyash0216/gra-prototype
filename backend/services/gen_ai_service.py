"""
Gen AI Service for Climate Adaptation Analysis
Supports OpenAI GPT and Anthropic Claude
"""

import os
import json
from typing import Dict, Optional
import asyncio

# Try to import AI libraries
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

class GenAIService:
    """Service for generating AI-powered climate adaptation recommendations"""
    
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        
        # Determine which AI service to use
        self.use_openai = OPENAI_AVAILABLE and self.openai_api_key
        self.use_anthropic = ANTHROPIC_AVAILABLE and self.anthropic_api_key
        
        if self.use_openai:
            openai.api_key = self.openai_api_key
            self.model = "gpt-3.5-turbo-16k"  # Use 16k context model for detailed responses
        elif self.use_anthropic:
            self.anthropic_client = anthropic.Anthropic(api_key=self.anthropic_api_key)
            self.model = "claude-3-haiku-20240307"
    
    def is_available(self) -> bool:
        """Check if any AI service is available"""
        return self.use_openai or self.use_anthropic
    
    async def generate_climate_analysis(self, farm_details: Dict, climate_concerns: list, adaptation_goals: list) -> str:
        """Generate comprehensive climate adaptation analysis using Gen AI"""
        
        prompt = self._build_analysis_prompt(farm_details, climate_concerns, adaptation_goals)
        
        if self.use_openai:
            return await self._generate_with_openai(prompt)
        elif self.use_anthropic:
            return await self._generate_with_anthropic(prompt)
        else:
            return None
    
    async def generate_crop_recommendations(self, farm_details: Dict, climate_risks: list) -> str:
        """Generate AI-powered crop recommendations"""
        
        prompt = f"""As an agricultural AI expert, provide detailed crop recommendations for this farm:

Location: {farm_details.get('location')}
Farm Size: {farm_details.get('farm_size')} acres
Soil Type: {farm_details.get('soil_type')}
Water Source: {farm_details.get('water_source')}
Budget: ₹{farm_details.get('budget')}
Current Crops: {', '.join(farm_details.get('current_crops', []))}
Climate Risks: {', '.join(climate_risks)}

Provide:
1. Top 5 climate-resilient crops with specific reasons
2. Crop rotation strategy
3. Expected yields and income projections
4. Planting calendar
5. Risk mitigation strategies

Format as detailed JSON with all recommendations."""

        if self.use_openai:
            return await self._generate_with_openai(prompt)
        elif self.use_anthropic:
            return await self._generate_with_anthropic(prompt)
        else:
            return None
    
    async def generate_market_analysis(self, crops: list, location: str) -> str:
        """Generate AI-powered market analysis"""
        
        prompt = f"""As a market intelligence expert, analyze the market potential for these crops in {location}:

Crops: {', '.join(crops)}

Provide detailed analysis including:
1. Current market prices and trends
2. Demand-supply dynamics
3. Best selling strategies
4. Price volatility assessment
5. Export opportunities
6. Marketing recommendations

Format as detailed JSON with actionable insights."""

        if self.use_openai:
            return await self._generate_with_openai(prompt)
        elif self.use_anthropic:
            return await self._generate_with_anthropic(prompt)
        else:
            return None
    
    async def generate_chat_response(self, message: str, context: Dict) -> str:
        """Generate AI chat response"""
        
        context_str = ""
        if context.get('location'):
            context_str = f"\n\nUser's Farm Context:"
            context_str += f"\n- Location: {context.get('location')}"
            if context.get('farm_size'):
                context_str += f"\n- Farm Size: {context.get('farm_size')} acres"
            if context.get('soil_type'):
                context_str += f"\n- Soil Type: {context.get('soil_type')}"
            if context.get('water_source'):
                context_str += f"\n- Water Source: {context.get('water_source')}"
            if context.get('current_crops'):
                context_str += f"\n- Current Crops: {', '.join(context.get('current_crops', []))}"
            if context.get('climate_concerns'):
                context_str += f"\n- Climate Concerns: {', '.join(context.get('climate_concerns', []))}"
        
        prompt = f"""You are GRA (Generative Resilience Agent), an expert AI agricultural advisor specializing in climate adaptation and sustainable farming practices for Indian farmers.

Your expertise includes:
- Climate-resilient crop selection and rotation
- Water management and irrigation optimization
- Soil health and organic farming
- Government schemes and subsidies (PM-KISAN, PMKSY, NMSA, etc.)
- Market intelligence and pricing strategies
- Pest and disease management
- Modern farming technologies

User Question: {message}
{context_str}

Instructions:
1. Provide detailed, actionable advice specific to the user's context
2. Include specific numbers, costs, and timelines where relevant
3. Mention relevant government schemes with subsidy amounts
4. Give practical implementation steps
5. Consider local Indian farming conditions and practices
6. Use simple language that farmers can understand
7. Include examples and success stories when relevant
8. Format response with clear sections using bullet points

Provide a comprehensive, practical response (200-300 words)."""

        if self.use_openai:
            return await self._generate_with_openai(prompt, max_tokens=800)
        elif self.use_anthropic:
            return await self._generate_with_anthropic(prompt, max_tokens=800)
        else:
            return None
    
    def _build_analysis_prompt(self, farm_details: Dict, climate_concerns: list, adaptation_goals: list) -> str:
        """Build comprehensive analysis prompt"""
        
        return f"""You are an expert agricultural AI system specializing in climate adaptation for Indian farmers. Analyze this farm and provide comprehensive, actionable recommendations.

FARM PROFILE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Location: {farm_details.get('location')}
Farm Size: {farm_details.get('farm_size')} acres
Soil Type: {farm_details.get('soil_type')}
Water Source: {farm_details.get('water_source')}
Current Crops: {', '.join(farm_details.get('current_crops', []))}
Available Budget: ₹{farm_details.get('budget'):,}
Farmer Experience: {farm_details.get('experience_level')}

CLIMATE CHALLENGES:
{chr(10).join(f'• {concern}' for concern in climate_concerns)}

FARMER'S GOALS:
{chr(10).join(f'• {goal}' for goal in adaptation_goals)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REQUIRED ANALYSIS (Provide in JSON format):

{{
  "climate_analysis": {{
    "risks": ["list of specific climate risks for this location"],
    "severity_scores": {{"risk_name": 0.0-1.0}},
    "urgency_level": "Low/Medium/High",
    "climate_trends": "Detailed description of climate patterns in this region",
    "adaptation_strategies": [
      {{
        "strategy": "Strategy name",
        "actions": ["specific action 1", "specific action 2"],
        "priority": "High/Medium/Low",
        "cost_estimate": "₹X,XXX",
        "timeline": "X months"
      }}
    ]
  }},
  
  "crop_recommendations": {{
    "recommended_crops": ["crop1", "crop2", "crop3", "crop4", "crop5"],
    "detailed_recommendations": [
      {{
        "name": "Crop name",
        "suitability_score": 0-100,
        "reason": "Detailed explanation why this crop is recommended",
        "climate_resilience": "High/Medium/Low to specific risks",
        "water_requirement": "X liters per acre",
        "expected_yield": "X kg per acre",
        "market_price": "₹X per kg",
        "gross_income": "₹X,XXX per acre",
        "input_cost": "₹X,XXX per acre",
        "net_profit": "₹X,XXX per acre",
        "growth_duration": "X days",
        "best_planting_time": "Month names"
      }}
    ],
    "crop_rotation_plan": {{
      "kharif_season": ["crops for June-October"],
      "rabi_season": ["crops for November-March"],
      "summer_season": ["crops for April-May"],
      "rotation_benefits": ["benefit 1", "benefit 2"]
    }},
    "seasonal_calendar": {{
      "january": [{{"crop": "name", "activity": "planting/harvesting"}}],
      "february": [],
      ...
    }}
  }},
  
  "market_analysis": {{
    "crop_market_analysis": {{
      "crop_name": {{
        "current_price": "₹X per kg",
        "price_trend": "increasing/stable/decreasing",
        "demand_level": "high/medium/low",
        "market_accessibility": "Description of local markets",
        "best_selling_strategy": "Direct/FPO/Contract farming",
        "export_potential": "high/medium/low"
      }}
    }},
    "market_insights": [
      "Specific insight about market conditions",
      "Price volatility warnings",
      "Demand-supply dynamics"
    ],
    "marketing_recommendations": [
      {{
        "strategy": "Strategy name",
        "description": "How to implement",
        "expected_benefit": "X% better price"
      }}
    ]
  }},
  
  "government_schemes": {{
    "recommended_schemes": [
      {{
        "name": "Scheme full name",
        "description": "What it provides",
        "subsidy": {{
          "amount": "₹X,XXX",
          "percentage": "X%"
        }},
        "eligibility": "Who can apply",
        "application_process": "How to apply",
        "documents_required": ["doc1", "doc2"],
        "timeline": "When to apply"
      }}
    ],
    "total_potential_subsidy": {{
      "total_subsidy_amount": "₹X,XXX",
      "farmer_contribution": "₹X,XXX"
    }}
  }},
  
  "water_management": {{
    "irrigation_recommendations": [
      {{
        "system": "Drip/Sprinkler/Flood",
        "suitability": "For which crops",
        "water_savings": "X%",
        "cost": "₹X,XXX",
        "subsidy_available": "₹X,XXX",
        "payback_period": "X years"
      }}
    ],
    "water_conservation": [
      "Specific technique 1 with implementation details",
      "Specific technique 2 with cost and benefits"
    ]
  }},
  
  "soil_management": {{
    "soil_health_recommendations": [
      "Specific recommendation with quantities and timing"
    ],
    "fertilization_plan": {{
      "organic": "X tons compost per acre",
      "npk_ratio": "N:P:K ratio",
      "micronutrients": ["Zinc", "Boron", etc.]
    }},
    "soil_conservation": [
      "Practice 1 with implementation steps"
    ]
  }},
  
  "implementation_timeline": [
    {{
      "phase": "Immediate (0-3 months)",
      "actions": [
        "Specific action 1 with cost ₹X,XXX",
        "Specific action 2 with timeline"
      ],
      "total_cost": "₹X,XXX",
      "expected_outcome": "What will be achieved"
    }},
    {{
      "phase": "Short-term (3-12 months)",
      "actions": ["..."],
      "total_cost": "₹X,XXX",
      "expected_outcome": "..."
    }},
    {{
      "phase": "Long-term (1-3 years)",
      "actions": ["..."],
      "total_cost": "₹X,XXX",
      "expected_outcome": "..."
    }}
  ],
  
  "cost_analysis": {{
    "total_estimated_cost": "₹X,XXX",
    "government_subsidy": "₹X,XXX",
    "farmer_contribution": "₹X,XXX",
    "breakdown": {{
      "seeds_and_inputs": "₹X,XXX",
      "infrastructure": "₹X,XXX",
      "irrigation": "₹X,XXX",
      "training": "₹X,XXX"
    }},
    "roi_projection": {{
      "year_1": "₹X,XXX profit",
      "year_2": "₹X,XXX profit",
      "year_3": "₹X,XXX profit",
      "payback_period": "X years"
    }}
  }},
  
  "expected_benefits": {{
    "yield_improvement": "X%",
    "income_increase": "₹X,XXX per year",
    "water_savings": "X%",
    "climate_resilience": "High/Medium/Low",
    "sustainability_score": "X/10",
    "risk_reduction": "X%"
  }}
}}

IMPORTANT INSTRUCTIONS:
1. All costs must be in Indian Rupees (₹)
2. Consider local Indian farming practices and conditions
3. Include specific government schemes available in India
4. Provide realistic yield and income projections
5. Consider the farmer's budget constraints
6. Give priority to climate-resilient and water-efficient solutions
7. Include both traditional and modern farming techniques
8. Provide actionable steps with clear timelines
9. Consider the farmer's experience level
10. Return ONLY valid JSON, no additional text

Generate comprehensive, detailed, and practical recommendations."""
    
    async def _generate_with_openai(self, prompt: str, max_tokens: int = 4000) -> str:
        """Generate response using OpenAI"""
        try:
            response = await asyncio.to_thread(
                openai.ChatCompletion.create,
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert agricultural AI assistant specializing in climate adaptation and sustainable farming for Indian farmers. You provide detailed, practical, and actionable advice with specific numbers, costs, and timelines."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return None
    
    async def _generate_with_anthropic(self, prompt: str, max_tokens: int = 2000) -> str:
        """Generate response using Anthropic Claude"""
        try:
            response = await asyncio.to_thread(
                self.anthropic_client.messages.create,
                model=self.model,
                max_tokens=max_tokens,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            print(f"Anthropic API error: {e}")
            return None

# Global instance
gen_ai_service = GenAIService()