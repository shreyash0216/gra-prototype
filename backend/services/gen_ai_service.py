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
            self.model = "gpt-3.5-turbo"
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
            context_str = f"\nUser's farm context: Location: {context.get('location')}, Farm size: {context.get('farm_size')} acres"
        
        prompt = f"""You are GRA (Generative Resilience Agent), an AI assistant helping farmers with climate adaptation.

User question: {message}
{context_str}

Provide a helpful, practical response with specific recommendations. Be concise but informative."""

        if self.use_openai:
            return await self._generate_with_openai(prompt, max_tokens=500)
        elif self.use_anthropic:
            return await self._generate_with_anthropic(prompt, max_tokens=500)
        else:
            return None
    
    def _build_analysis_prompt(self, farm_details: Dict, climate_concerns: list, adaptation_goals: list) -> str:
        """Build comprehensive analysis prompt"""
        
        return f"""You are an expert agricultural AI system specializing in climate adaptation. Analyze this farm and provide comprehensive recommendations:

FARM DETAILS:
- Location: {farm_details.get('location')}
- Farm Size: {farm_details.get('farm_size')} acres
- Soil Type: {farm_details.get('soil_type')}
- Water Source: {farm_details.get('water_source')}
- Current Crops: {', '.join(farm_details.get('current_crops', []))}
- Budget: ₹{farm_details.get('budget')}
- Experience Level: {farm_details.get('experience_level')}

CLIMATE CONCERNS:
{', '.join(climate_concerns)}

ADAPTATION GOALS:
{', '.join(adaptation_goals)}

Provide a comprehensive analysis in JSON format with these sections:

1. climate_analysis:
   - Identified risks with severity scores
   - Climate trends for the region
   - Urgency level assessment
   - Specific adaptation strategies

2. crop_recommendations:
   - Top 5 climate-resilient crops with detailed reasoning
   - Crop rotation plan
   - Seasonal calendar
   - Expected yields and income

3. water_management:
   - Irrigation recommendations
   - Water conservation strategies
   - Cost-benefit analysis

4. soil_management:
   - Soil improvement strategies
   - Fertilization recommendations
   - Organic matter management

5. implementation_timeline:
   - Immediate actions (0-3 months)
   - Short-term (3-12 months)
   - Long-term (1-3 years)

6. cost_analysis:
   - Total estimated costs
   - Government subsidies available
   - Farmer contribution
   - ROI projections

Provide detailed, actionable recommendations specific to this farm's conditions."""
    
    async def _generate_with_openai(self, prompt: str, max_tokens: int = 2000) -> str:
        """Generate response using OpenAI"""
        try:
            response = await asyncio.to_thread(
                openai.ChatCompletion.create,
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert agricultural AI assistant specializing in climate adaptation and sustainable farming."},
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