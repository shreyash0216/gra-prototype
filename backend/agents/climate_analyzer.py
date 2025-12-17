from typing import Dict, List
import json
import asyncio

class ClimateAnalyzer:
    """AI agent for analyzing climate risks and adaptation needs"""
    
    def __init__(self):
        self.climate_data = self._load_climate_knowledge()
    
    async def analyze_risks(self, location: str, concerns: List[str]) -> Dict:
        """Analyze climate risks for a specific location"""
        
        # Simulate AI analysis (in production, integrate with Claude/GPT)
        await asyncio.sleep(0.1)  # Simulate processing time
        
        location_lower = location.lower()
        
        # Risk assessment based on location and concerns
        risks = []
        severity_scores = {}
        
        # Common climate risks by region (simplified for prototype)
        if any(region in location_lower for region in ['maharashtra', 'karnataka', 'telangana']):
            risks.extend(['drought', 'irregular_rainfall', 'heat_waves'])
        elif any(region in location_lower for region in ['kerala', 'west bengal', 'assam']):
            risks.extend(['flooding', 'excessive_rainfall', 'cyclones'])
        elif any(region in location_lower for region in ['punjab', 'haryana', 'uttar pradesh']):
            risks.extend(['water_scarcity', 'soil_degradation', 'temperature_fluctuations'])
        else:
            risks.extend(['irregular_rainfall', 'temperature_variations'])
        
        # Add user-specified concerns
        for concern in concerns:
            if concern not in risks:
                risks.append(concern)
        
        # Calculate severity scores
        for risk in risks:
            severity_scores[risk] = self._calculate_risk_severity(risk, location)
        
        # Generate adaptation strategies
        adaptation_strategies = self._generate_adaptation_strategies(risks)
        
        return {
            "location": location,
            "risks": risks,
            "severity_scores": severity_scores,
            "adaptation_strategies": adaptation_strategies,
            "climate_trends": self._get_climate_trends(location),
            "urgency_level": self._calculate_urgency(severity_scores)
        }
    
    def _load_climate_knowledge(self) -> Dict:
        """Load climate knowledge base"""
        return {
            "risk_factors": {
                "drought": {
                    "description": "Extended periods of low rainfall",
                    "impact": "Crop failure, water scarcity",
                    "adaptation": ["drought-resistant crops", "water conservation", "mulching"]
                },
                "flooding": {
                    "description": "Excessive water accumulation",
                    "impact": "Crop damage, soil erosion",
                    "adaptation": ["drainage systems", "raised beds", "flood-tolerant crops"]
                },
                "heat_waves": {
                    "description": "Extreme high temperatures",
                    "impact": "Heat stress, reduced yields",
                    "adaptation": ["shade nets", "heat-tolerant varieties", "irrigation timing"]
                }
            }
        }
    
    def _calculate_risk_severity(self, risk: str, location: str) -> float:
        """Calculate severity score for a risk (0-1 scale)"""
        base_scores = {
            "drought": 0.7,
            "flooding": 0.6,
            "heat_waves": 0.8,
            "irregular_rainfall": 0.6,
            "water_scarcity": 0.7,
            "soil_degradation": 0.5,
            "cyclones": 0.9,
            "temperature_fluctuations": 0.4
        }
        
        return base_scores.get(risk, 0.5)
    
    def _generate_adaptation_strategies(self, risks: List[str]) -> List[Dict]:
        """Generate adaptation strategies based on identified risks"""
        strategies = []
        
        strategy_map = {
            "drought": {
                "strategy": "Water Conservation & Drought Management",
                "actions": [
                    "Install drip irrigation systems",
                    "Implement rainwater harvesting",
                    "Use drought-resistant crop varieties",
                    "Apply mulching techniques"
                ],
                "priority": "High"
            },
            "flooding": {
                "strategy": "Flood Management & Drainage",
                "actions": [
                    "Construct proper drainage systems",
                    "Create raised bed farming",
                    "Plant flood-tolerant crops",
                    "Build water retention structures"
                ],
                "priority": "High"
            },
            "heat_waves": {
                "strategy": "Heat Stress Management",
                "actions": [
                    "Install shade nets over crops",
                    "Use heat-tolerant crop varieties",
                    "Optimize irrigation timing",
                    "Implement cooling systems"
                ],
                "priority": "Medium"
            }
        }
        
        for risk in risks:
            if risk in strategy_map:
                strategies.append(strategy_map[risk])
        
        return strategies
    
    def _get_climate_trends(self, location: str) -> Dict:
        """Get climate trends for the location"""
        return {
            "temperature_trend": "+1.2°C over last decade",
            "rainfall_trend": "-15% compared to historical average",
            "extreme_events": "Increasing frequency of droughts and heat waves",
            "seasonal_shifts": "Delayed monsoon onset, extended summer"
        }
    
    def _calculate_urgency(self, severity_scores: Dict) -> str:
        """Calculate overall urgency level"""
        avg_severity = sum(severity_scores.values()) / len(severity_scores) if severity_scores else 0
        
        if avg_severity >= 0.7:
            return "High"
        elif avg_severity >= 0.5:
            return "Medium"
        else:
            return "Low"