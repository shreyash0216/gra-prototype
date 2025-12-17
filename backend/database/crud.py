from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from typing import List, Dict, Optional
from .models import AdaptationPlan
import json
import math

class ClimateAdaptationCRUD:
    def __init__(self, db: Session):
        self.db = db
    
    def create_adaptation_plan(self, farm_details: Dict, adaptation_plan: Dict) -> AdaptationPlan:
        """Create a new adaptation plan"""
        db_plan = AdaptationPlan(
            farm_id=adaptation_plan["farm_id"],
            location=farm_details["location"],
            farm_size=farm_details["farm_size"],
            soil_type=farm_details["soil_type"],
            water_source=farm_details["water_source"],
            current_crops=farm_details["current_crops"],
            budget=farm_details["budget"],
            experience_level=farm_details["experience_level"],
            
            climate_risks=adaptation_plan["climate_analysis"]["risks"],
            recommended_crops=adaptation_plan["crop_recommendations"]["recommended_crops"],
            market_analysis=adaptation_plan["market_analysis"],
            government_schemes=adaptation_plan["government_schemes"],
            farm_layout_svg=adaptation_plan["farm_layout_svg"],
            
            implementation_timeline=adaptation_plan["implementation_timeline"],
            estimated_costs=adaptation_plan["estimated_costs"],
            expected_benefits=adaptation_plan["expected_benefits"]
        )
        
        self.db.add(db_plan)
        self.db.commit()
        self.db.refresh(db_plan)
        return db_plan
    
    def get_plan_by_id(self, plan_id: int) -> Optional[AdaptationPlan]:
        """Get adaptation plan by ID"""
        return self.db.query(AdaptationPlan).filter(AdaptationPlan.id == plan_id).first()
    
    def get_nearby_plans(self, location: str, radius_km: float = 10.0) -> List[Dict]:
        """Get adaptation plans from nearby farms"""
        # Simple location matching for prototype
        # In production, use proper geospatial queries
        plans = self.db.query(AdaptationPlan).filter(
            AdaptationPlan.location.contains(location.split(',')[0])  # Match city/state
        ).limit(10).all()
        
        nearby_plans = []
        for plan in plans:
            nearby_plans.append({
                "id": plan.id,
                "location": plan.location,
                "farm_size": plan.farm_size,
                "soil_type": plan.soil_type,
                "recommended_crops": plan.recommended_crops,
                "success_metrics": {
                    "climate_resilience": "High",
                    "yield_improvement": "30%",
                    "cost_effectiveness": "Good"
                },
                "created_at": plan.created_at.isoformat()
            })
        
        return nearby_plans
    
    def get_plans_by_location(self, location: str) -> List[AdaptationPlan]:
        """Get all plans for a specific location"""
        return self.db.query(AdaptationPlan).filter(
            AdaptationPlan.location.contains(location)
        ).all()
    
    def get_plans_by_crop(self, crop_name: str) -> List[AdaptationPlan]:
        """Get plans that include a specific crop"""
        return self.db.query(AdaptationPlan).filter(
            AdaptationPlan.recommended_crops.contains(crop_name)
        ).all()
    
    def update_plan(self, plan_id: int, updates: Dict) -> Optional[AdaptationPlan]:
        """Update an existing adaptation plan"""
        plan = self.get_plan_by_id(plan_id)
        if plan:
            for key, value in updates.items():
                if hasattr(plan, key):
                    setattr(plan, key, value)
            self.db.commit()
            self.db.refresh(plan)
        return plan
    
    def delete_plan(self, plan_id: int) -> bool:
        """Delete an adaptation plan"""
        plan = self.get_plan_by_id(plan_id)
        if plan:
            self.db.delete(plan)
            self.db.commit()
            return True
        return False