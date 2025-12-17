from typing import Dict, List
import asyncio
from data.knowledge_base import get_crops_data

class CropAdvisor:
    """AI agent for crop recommendations based on climate and farm conditions"""
    
    def __init__(self):
        self.crops_database = get_crops_data()
    
    async def recommend_crops(self, farm_details: Dict, climate_risks: List[str]) -> Dict:
        """Recommend suitable crops based on farm conditions and climate risks"""
        
        # Simulate AI processing
        await asyncio.sleep(0.1)
        
        location = farm_details.get("location", "").lower()
        soil_type = farm_details.get("soil_type", "").lower()
        water_source = farm_details.get("water_source", "").lower()
        farm_size = farm_details.get("farm_size", 0)
        budget = farm_details.get("budget", 0)
        
        # Filter crops based on conditions
        suitable_crops = self._filter_crops_by_conditions(
            location, soil_type, water_source, climate_risks
        )
        
        # Rank crops by suitability
        ranked_crops = self._rank_crops(suitable_crops, farm_details, climate_risks)
        
        # Generate crop rotation plan
        rotation_plan = self._generate_rotation_plan(ranked_crops[:5])
        
        # Calculate expected yields
        yield_estimates = self._calculate_yield_estimates(ranked_crops[:5], farm_size)
        
        return {
            "recommended_crops": [crop["name"] for crop in ranked_crops[:5]],
            "detailed_recommendations": ranked_crops[:5],
            "crop_rotation_plan": rotation_plan,
            "yield_estimates": yield_estimates,
            "diversification_strategy": self._generate_diversification_strategy(ranked_crops),
            "seasonal_calendar": self._generate_seasonal_calendar(ranked_crops[:5])
        }
    
    def _filter_crops_by_conditions(self, location: str, soil_type: str, 
                                   water_source: str, climate_risks: List[str]) -> List[Dict]:
        """Filter crops based on farm conditions"""
        suitable_crops = []
        
        for crop in self.crops_database:
            # Check climate suitability
            if self._is_climate_suitable(crop, location, climate_risks):
                # Check soil compatibility
                if self._is_soil_suitable(crop, soil_type):
                    # Check water requirements
                    if self._is_water_suitable(crop, water_source):
                        suitable_crops.append(crop)
        
        return suitable_crops
    
    def _is_climate_suitable(self, crop: Dict, location: str, climate_risks: List[str]) -> bool:
        """Check if crop is suitable for the climate"""
        crop_climate = crop.get("climate_zones", [])
        
        # Regional suitability
        if any(zone in location for zone in crop_climate):
            return True
        
        # Risk tolerance
        crop_tolerance = crop.get("risk_tolerance", {})
        for risk in climate_risks:
            if risk in crop_tolerance and crop_tolerance[risk] == "high":
                return True
        
        return len(crop_climate) == 0  # Default crops
    
    def _is_soil_suitable(self, crop: Dict, soil_type: str) -> bool:
        """Check soil compatibility"""
        suitable_soils = crop.get("soil_types", [])
        return not suitable_soils or any(soil in soil_type for soil in suitable_soils)
    
    def _is_water_suitable(self, crop: Dict, water_source: str) -> bool:
        """Check water requirement compatibility"""
        water_req = crop.get("water_requirement", "medium")
        
        if "bore" in water_source or "well" in water_source:
            return water_req in ["low", "medium"]
        elif "river" in water_source or "canal" in water_source:
            return True  # All water requirements can be met
        else:
            return water_req == "low"  # Rain-fed farming
    
    def _rank_crops(self, crops: List[Dict], farm_details: Dict, climate_risks: List[str]) -> List[Dict]:
        """Rank crops by suitability score"""
        scored_crops = []
        
        for crop in crops:
            score = self._calculate_suitability_score(crop, farm_details, climate_risks)
            crop_with_score = crop.copy()
            crop_with_score["suitability_score"] = score
            crop_with_score["recommendation_reason"] = self._generate_recommendation_reason(
                crop, farm_details, climate_risks
            )
            scored_crops.append(crop_with_score)
        
        return sorted(scored_crops, key=lambda x: x["suitability_score"], reverse=True)
    
    def _calculate_suitability_score(self, crop: Dict, farm_details: Dict, climate_risks: List[str]) -> float:
        """Calculate suitability score (0-100)"""
        score = 50  # Base score
        
        # Climate resilience bonus
        crop_tolerance = crop.get("risk_tolerance", {})
        for risk in climate_risks:
            if risk in crop_tolerance:
                if crop_tolerance[risk] == "high":
                    score += 15
                elif crop_tolerance[risk] == "medium":
                    score += 5
        
        # Market value bonus
        market_price = crop.get("market_price_per_kg", 0)
        if market_price > 50:
            score += 10
        elif market_price > 20:
            score += 5
        
        # Growth duration consideration
        growth_days = crop.get("growth_duration_days", 120)
        if growth_days < 90:
            score += 10  # Quick returns
        elif growth_days > 180:
            score -= 5   # Long commitment
        
        # Budget compatibility
        input_cost = crop.get("input_cost_per_acre", 0)
        budget_per_acre = farm_details.get("budget", 0) / max(farm_details.get("farm_size", 1), 1)
        if input_cost <= budget_per_acre * 0.7:
            score += 15
        elif input_cost <= budget_per_acre:
            score += 5
        else:
            score -= 10
        
        return min(100, max(0, score))
    
    def _generate_recommendation_reason(self, crop: Dict, farm_details: Dict, climate_risks: List[str]) -> str:
        """Generate explanation for crop recommendation"""
        reasons = []
        
        # Climate resilience
        crop_tolerance = crop.get("risk_tolerance", {})
        resilient_to = [risk for risk in climate_risks if crop_tolerance.get(risk) == "high"]
        if resilient_to:
            reasons.append(f"Highly resilient to {', '.join(resilient_to)}")
        
        # Market potential
        market_price = crop.get("market_price_per_kg", 0)
        if market_price > 50:
            reasons.append("High market value")
        
        # Quick returns
        growth_days = crop.get("growth_duration_days", 120)
        if growth_days < 90:
            reasons.append("Quick harvest cycle")
        
        # Budget friendly
        input_cost = crop.get("input_cost_per_acre", 0)
        budget_per_acre = farm_details.get("budget", 0) / max(farm_details.get("farm_size", 1), 1)
        if input_cost <= budget_per_acre * 0.7:
            reasons.append("Budget-friendly")
        
        return "; ".join(reasons) if reasons else "Suitable for your farm conditions"
    
    def _generate_rotation_plan(self, crops: List[Dict]) -> Dict:
        """Generate crop rotation plan"""
        return {
            "kharif_season": [crop["name"] for crop in crops if crop.get("season") in ["kharif", "both"]][:2],
            "rabi_season": [crop["name"] for crop in crops if crop.get("season") in ["rabi", "both"]][:2],
            "summer_season": [crop["name"] for crop in crops if crop.get("season") in ["summer", "both"]][:1],
            "rotation_benefits": [
                "Improved soil health",
                "Reduced pest and disease pressure",
                "Better nutrient management",
                "Risk diversification"
            ]
        }
    
    def _calculate_yield_estimates(self, crops: List[Dict], farm_size: float) -> Dict:
        """Calculate expected yields and income"""
        estimates = {}
        
        for crop in crops:
            yield_per_acre = crop.get("yield_per_acre_kg", 1000)
            market_price = crop.get("market_price_per_kg", 20)
            input_cost_per_acre = crop.get("input_cost_per_acre", 15000)
            
            total_yield = yield_per_acre * farm_size
            gross_income = total_yield * market_price
            total_input_cost = input_cost_per_acre * farm_size
            net_income = gross_income - total_input_cost
            
            estimates[crop["name"]] = {
                "yield_kg": total_yield,
                "gross_income": gross_income,
                "input_cost": total_input_cost,
                "net_income": net_income,
                "profit_margin": (net_income / gross_income * 100) if gross_income > 0 else 0
            }
        
        return estimates
    
    def _generate_diversification_strategy(self, crops: List[Dict]) -> Dict:
        """Generate crop diversification strategy"""
        return {
            "primary_crops": [crop["name"] for crop in crops[:2]],
            "secondary_crops": [crop["name"] for crop in crops[2:4]],
            "cash_crops": [crop["name"] for crop in crops if crop.get("market_price_per_kg", 0) > 50][:2],
            "food_security_crops": [crop["name"] for crop in crops if crop.get("category") == "food_grain"][:2],
            "diversification_benefits": [
                "Reduced market risk",
                "Stable income throughout year",
                "Better resource utilization",
                "Enhanced food security"
            ]
        }
    
    def _generate_seasonal_calendar(self, crops: List[Dict]) -> Dict:
        """Generate seasonal planting calendar"""
        calendar = {
            "january": [], "february": [], "march": [], "april": [],
            "may": [], "june": [], "july": [], "august": [],
            "september": [], "october": [], "november": [], "december": []
        }
        
        for crop in crops:
            planting_months = crop.get("planting_months", ["june"])
            for month in planting_months:
                if month.lower() in calendar:
                    calendar[month.lower()].append({
                        "crop": crop["name"],
                        "activity": "Planting",
                        "duration": f"{crop.get('growth_duration_days', 120)} days"
                    })
        
        return calendar