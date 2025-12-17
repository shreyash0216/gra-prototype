from typing import Dict, List
import asyncio
from data.knowledge_base import get_market_data

class MarketAnalyzer:
    """AI agent for market analysis and price predictions"""
    
    def __init__(self):
        self.market_data = get_market_data()
    
    async def analyze_market_potential(self, crops: List[str], location: str) -> Dict:
        """Analyze market potential for recommended crops"""
        
        # Simulate AI processing
        await asyncio.sleep(0.1)
        
        market_analysis = {}
        
        for crop in crops:
            crop_market_data = self._get_crop_market_data(crop, location)
            market_analysis[crop] = {
                "current_price": crop_market_data["current_price"],
                "price_trend": crop_market_data["price_trend"],
                "demand_level": crop_market_data["demand_level"],
                "market_accessibility": self._assess_market_accessibility(crop, location),
                "price_volatility": crop_market_data["volatility"],
                "seasonal_patterns": crop_market_data["seasonal_patterns"],
                "export_potential": crop_market_data["export_potential"],
                "local_demand": crop_market_data["local_demand"]
            }
        
        # Overall market insights
        overall_insights = self._generate_market_insights(market_analysis, location)
        
        return {
            "crop_market_analysis": market_analysis,
            "market_insights": overall_insights,
            "pricing_strategy": self._generate_pricing_strategy(market_analysis),
            "marketing_recommendations": self._generate_marketing_recommendations(crops, location),
            "risk_assessment": self._assess_market_risks(market_analysis)
        }
    
    def _get_crop_market_data(self, crop: str, location: str) -> Dict:
        """Get market data for a specific crop"""
        
        # Default market data structure
        default_data = {
            "current_price": 25,
            "price_trend": "stable",
            "demand_level": "medium",
            "volatility": "medium",
            "seasonal_patterns": {"peak_months": ["march", "april"], "low_months": ["july", "august"]},
            "export_potential": "medium",
            "local_demand": "high"
        }
        
        # Crop-specific market data
        crop_market_data = {
            "rice": {
                "current_price": 22,
                "price_trend": "increasing",
                "demand_level": "high",
                "volatility": "low",
                "seasonal_patterns": {"peak_months": ["october", "november"], "low_months": ["june", "july"]},
                "export_potential": "high",
                "local_demand": "very_high"
            },
            "wheat": {
                "current_price": 20,
                "price_trend": "stable",
                "demand_level": "high",
                "volatility": "low",
                "seasonal_patterns": {"peak_months": ["april", "may"], "low_months": ["december", "january"]},
                "export_potential": "medium",
                "local_demand": "very_high"
            },
            "cotton": {
                "current_price": 55,
                "price_trend": "increasing",
                "demand_level": "high",
                "volatility": "high",
                "seasonal_patterns": {"peak_months": ["december", "january"], "low_months": ["june", "july"]},
                "export_potential": "very_high",
                "local_demand": "medium"
            },
            "sugarcane": {
                "current_price": 3,
                "price_trend": "stable",
                "demand_level": "high",
                "volatility": "low",
                "seasonal_patterns": {"peak_months": ["february", "march"], "low_months": ["august", "september"]},
                "export_potential": "low",
                "local_demand": "very_high"
            },
            "soybean": {
                "current_price": 45,
                "price_trend": "increasing",
                "demand_level": "high",
                "volatility": "medium",
                "seasonal_patterns": {"peak_months": ["november", "december"], "low_months": ["july", "august"]},
                "export_potential": "high",
                "local_demand": "high"
            },
            "maize": {
                "current_price": 18,
                "price_trend": "stable",
                "demand_level": "medium",
                "volatility": "medium",
                "seasonal_patterns": {"peak_months": ["january", "february"], "low_months": ["september", "october"]},
                "export_potential": "medium",
                "local_demand": "high"
            },
            "tomato": {
                "current_price": 35,
                "price_trend": "volatile",
                "demand_level": "high",
                "volatility": "very_high",
                "seasonal_patterns": {"peak_months": ["december", "january"], "low_months": ["june", "july"]},
                "export_potential": "low",
                "local_demand": "very_high"
            },
            "onion": {
                "current_price": 28,
                "price_trend": "increasing",
                "demand_level": "high",
                "volatility": "high",
                "seasonal_patterns": {"peak_months": ["may", "june"], "low_months": ["november", "december"]},
                "export_potential": "medium",
                "local_demand": "very_high"
            }
        }
        
        return crop_market_data.get(crop.lower(), default_data)
    
    def _assess_market_accessibility(self, crop: str, location: str) -> Dict:
        """Assess market accessibility for the crop"""
        
        # Simulate market accessibility analysis
        location_lower = location.lower()
        
        # Urban areas have better market access
        urban_indicators = ["mumbai", "delhi", "bangalore", "chennai", "kolkata", "hyderabad", "pune"]
        is_urban = any(city in location_lower for city in urban_indicators)
        
        accessibility_score = 7 if is_urban else 5
        
        return {
            "accessibility_score": accessibility_score,
            "nearest_market_km": 15 if is_urban else 35,
            "transportation_cost": "low" if is_urban else "medium",
            "market_infrastructure": "good" if is_urban else "fair",
            "cold_storage_availability": "high" if is_urban else "medium"
        }
    
    def _generate_market_insights(self, market_analysis: Dict, location: str) -> List[str]:
        """Generate overall market insights"""
        insights = []
        
        # High-value crops
        high_value_crops = [crop for crop, data in market_analysis.items() 
                           if data["current_price"] > 40]
        if high_value_crops:
            insights.append(f"High-value crops identified: {', '.join(high_value_crops)}")
        
        # Stable demand crops
        stable_crops = [crop for crop, data in market_analysis.items() 
                       if data["demand_level"] in ["high", "very_high"]]
        if stable_crops:
            insights.append(f"Crops with stable demand: {', '.join(stable_crops)}")
        
        # Export potential
        export_crops = [crop for crop, data in market_analysis.items() 
                       if data["export_potential"] in ["high", "very_high"]]
        if export_crops:
            insights.append(f"Export potential crops: {', '.join(export_crops)}")
        
        # Price volatility warning
        volatile_crops = [crop for crop, data in market_analysis.items() 
                         if data["price_volatility"] in ["high", "very_high"]]
        if volatile_crops:
            insights.append(f"Monitor price volatility for: {', '.join(volatile_crops)}")
        
        return insights
    
    def _generate_pricing_strategy(self, market_analysis: Dict) -> Dict:
        """Generate pricing strategy recommendations"""
        return {
            "direct_selling": {
                "recommended_for": [crop for crop, data in market_analysis.items() 
                                  if data["local_demand"] in ["high", "very_high"]],
                "benefits": ["Higher margins", "Direct customer relationship", "Reduced middleman costs"]
            },
            "contract_farming": {
                "recommended_for": [crop for crop, data in market_analysis.items() 
                                  if data["price_volatility"] in ["high", "very_high"]],
                "benefits": ["Price stability", "Assured market", "Input support"]
            },
            "cooperative_selling": {
                "recommended_for": [crop for crop, data in market_analysis.items() 
                                  if data["export_potential"] in ["high", "very_high"]],
                "benefits": ["Better negotiation power", "Bulk selling advantages", "Shared logistics"]
            }
        }
    
    def _generate_marketing_recommendations(self, crops: List[str], location: str) -> List[Dict]:
        """Generate marketing recommendations"""
        recommendations = []
        
        recommendations.append({
            "strategy": "Digital Marketing",
            "description": "Use online platforms to reach customers directly",
            "applicable_crops": crops,
            "implementation": [
                "Create social media presence",
                "List on agricultural marketplaces",
                "Use WhatsApp for customer communication"
            ]
        })
        
        recommendations.append({
            "strategy": "Value Addition",
            "description": "Process crops to increase market value",
            "applicable_crops": [crop for crop in crops if crop in ["rice", "wheat", "maize"]],
            "implementation": [
                "Basic processing (cleaning, grading)",
                "Packaging and branding",
                "Organic certification"
            ]
        })
        
        recommendations.append({
            "strategy": "Farmer Producer Organizations (FPO)",
            "description": "Join or form FPOs for collective marketing",
            "applicable_crops": crops,
            "implementation": [
                "Join existing FPOs in the area",
                "Participate in collective bargaining",
                "Share transportation and storage costs"
            ]
        })
        
        return recommendations
    
    def _assess_market_risks(self, market_analysis: Dict) -> Dict:
        """Assess market risks for the crop portfolio"""
        
        risks = []
        mitigation_strategies = []
        
        # Price volatility risk
        volatile_crops = [crop for crop, data in market_analysis.items() 
                         if data["price_volatility"] in ["high", "very_high"]]
        if volatile_crops:
            risks.append(f"High price volatility in {', '.join(volatile_crops)}")
            mitigation_strategies.append("Consider contract farming for volatile crops")
        
        # Market concentration risk
        if len(market_analysis) < 3:
            risks.append("Limited crop diversification increases market risk")
            mitigation_strategies.append("Diversify crop portfolio to spread market risk")
        
        # Seasonal demand risk
        risks.append("Seasonal demand fluctuations may affect prices")
        mitigation_strategies.append("Plan harvest timing to avoid market gluts")
        
        return {
            "identified_risks": risks,
            "mitigation_strategies": mitigation_strategies,
            "overall_risk_level": "Medium",
            "risk_score": 6.5  # Out of 10
        }