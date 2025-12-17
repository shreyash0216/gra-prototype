from typing import Dict, List
import asyncio
from data.knowledge_base import get_schemes_data

class SchemeFinder:
    """AI agent for finding relevant government schemes and subsidies"""
    
    def __init__(self):
        self.schemes_database = get_schemes_data()
    
    async def find_relevant_schemes(self, farm_details: Dict, adaptation_goals: List[str]) -> Dict:
        """Find government schemes relevant to the farmer's needs"""
        
        # Simulate AI processing
        await asyncio.sleep(0.1)
        
        # Filter schemes based on eligibility
        eligible_schemes = self._filter_eligible_schemes(farm_details)
        
        # Match schemes to adaptation goals
        matched_schemes = self._match_schemes_to_goals(eligible_schemes, adaptation_goals)
        
        # Prioritize schemes by benefit
        prioritized_schemes = self._prioritize_schemes(matched_schemes, farm_details)
        
        return {
            "recommended_schemes": prioritized_schemes[:5],
            "total_potential_subsidy": self._calculate_total_subsidy(prioritized_schemes[:5]),
            "application_timeline": self._generate_application_timeline(prioritized_schemes[:5]),
            "required_documents": self._get_required_documents(prioritized_schemes[:5]),
            "scheme_categories": self._categorize_schemes(prioritized_schemes)
        }
    
    def _filter_eligible_schemes(self, farm_details: Dict) -> List[Dict]:
        """Filter schemes based on farmer eligibility"""
        eligible_schemes = []
        
        farm_size = farm_details.get("farm_size", 0)
        location = farm_details.get("location", "").lower()
        
        for scheme in self.schemes_database:
            # Check farm size eligibility
            if self._check_farm_size_eligibility(scheme, farm_size):
                # Check location eligibility
                if self._check_location_eligibility(scheme, location):
                    eligible_schemes.append(scheme)
        
        return eligible_schemes
    
    def _check_farm_size_eligibility(self, scheme: Dict, farm_size: float) -> bool:
        """Check if farm size meets scheme criteria"""
        size_criteria = scheme.get("eligibility", {}).get("farm_size", {})
        
        min_size = size_criteria.get("min", 0)
        max_size = size_criteria.get("max", float('inf'))
        
        return min_size <= farm_size <= max_size
    
    def _check_location_eligibility(self, scheme: Dict, location: str) -> bool:
        """Check if location is eligible for the scheme"""
        location_criteria = scheme.get("eligibility", {}).get("states", [])
        
        if not location_criteria:  # National scheme
            return True
        
        # Check if any state matches
        return any(state.lower() in location for state in location_criteria)
    
    def _match_schemes_to_goals(self, schemes: List[Dict], adaptation_goals: List[str]) -> List[Dict]:
        """Match schemes to farmer's adaptation goals"""
        matched_schemes = []
        
        for scheme in schemes:
            scheme_objectives = scheme.get("objectives", [])
            scheme_categories = scheme.get("categories", [])
            
            # Calculate relevance score
            relevance_score = 0
            matching_goals = []
            
            for goal in adaptation_goals:
                goal_lower = goal.lower()
                
                # Check objectives match
                for objective in scheme_objectives:
                    if any(keyword in objective.lower() for keyword in goal_lower.split()):
                        relevance_score += 2
                        matching_goals.append(goal)
                
                # Check categories match
                for category in scheme_categories:
                    if any(keyword in category.lower() for keyword in goal_lower.split()):
                        relevance_score += 1
                        if goal not in matching_goals:
                            matching_goals.append(goal)
            
            if relevance_score > 0:
                scheme_copy = scheme.copy()
                scheme_copy["relevance_score"] = relevance_score
                scheme_copy["matching_goals"] = matching_goals
                matched_schemes.append(scheme_copy)
        
        return matched_schemes
    
    def _prioritize_schemes(self, schemes: List[Dict], farm_details: Dict) -> List[Dict]:
        """Prioritize schemes by potential benefit"""
        
        for scheme in schemes:
            priority_score = scheme.get("relevance_score", 0)
            
            # Add subsidy amount weight
            subsidy_amount = scheme.get("subsidy", {}).get("amount", 0)
            if subsidy_amount > 50000:
                priority_score += 3
            elif subsidy_amount > 20000:
                priority_score += 2
            elif subsidy_amount > 5000:
                priority_score += 1
            
            # Add ease of application weight
            application_complexity = scheme.get("application", {}).get("complexity", "medium")
            if application_complexity == "easy":
                priority_score += 2
            elif application_complexity == "medium":
                priority_score += 1
            
            scheme["priority_score"] = priority_score
        
        return sorted(schemes, key=lambda x: x.get("priority_score", 0), reverse=True)
    
    def _calculate_total_subsidy(self, schemes: List[Dict]) -> Dict:
        """Calculate total potential subsidy amount"""
        total_subsidy = 0
        total_loan = 0
        
        for scheme in schemes:
            subsidy_info = scheme.get("subsidy", {})
            total_subsidy += subsidy_info.get("amount", 0)
            
            loan_info = scheme.get("loan", {})
            total_loan += loan_info.get("amount", 0)
        
        return {
            "total_subsidy_amount": total_subsidy,
            "total_loan_amount": total_loan,
            "estimated_savings": total_subsidy + (total_loan * 0.3),  # Assuming 30% effective benefit from loans
            "farmer_contribution_required": max(0, 100000 - total_subsidy)  # Assuming 1 lakh total project cost
        }
    
    def _generate_application_timeline(self, schemes: List[Dict]) -> List[Dict]:
        """Generate application timeline for schemes"""
        timeline = []
        
        for i, scheme in enumerate(schemes):
            application_info = scheme.get("application", {})
            
            timeline.append({
                "scheme_name": scheme["name"],
                "application_period": application_info.get("period", "Year-round"),
                "processing_time": application_info.get("processing_days", "30-45 days"),
                "priority_order": i + 1,
                "recommended_start_date": f"Month {i + 1}"
            })
        
        return timeline
    
    def _get_required_documents(self, schemes: List[Dict]) -> Dict:
        """Compile required documents for all schemes"""
        all_documents = set()
        scheme_specific_docs = {}
        
        for scheme in schemes:
            documents = scheme.get("required_documents", [])
            all_documents.update(documents)
            scheme_specific_docs[scheme["name"]] = documents
        
        # Common documents
        common_docs = [
            "Aadhaar Card",
            "Land Records (7/12, 8A)",
            "Bank Account Details",
            "Passport Size Photos"
        ]
        
        return {
            "common_documents": common_docs,
            "all_required_documents": list(all_documents),
            "scheme_specific_documents": scheme_specific_docs,
            "document_checklist": self._create_document_checklist(all_documents)
        }
    
    def _create_document_checklist(self, documents: set) -> List[Dict]:
        """Create a checklist for document preparation"""
        checklist = []
        
        for doc in sorted(documents):
            checklist.append({
                "document": doc,
                "status": "pending",
                "notes": self._get_document_notes(doc)
            })
        
        return checklist
    
    def _get_document_notes(self, document: str) -> str:
        """Get helpful notes for document preparation"""
        notes_map = {
            "Aadhaar Card": "Ensure Aadhaar is linked to mobile number",
            "Land Records (7/12, 8A)": "Get latest copy from village office",
            "Bank Account Details": "Ensure account is active and linked to Aadhaar",
            "Soil Health Card": "Get from nearest Krishi Vigyan Kendra",
            "Income Certificate": "Valid for 1 year from issue date",
            "Caste Certificate": "Required for SC/ST/OBC schemes"
        }
        
        return notes_map.get(document, "Ensure document is valid and up-to-date")
    
    def _categorize_schemes(self, schemes: List[Dict]) -> Dict:
        """Categorize schemes by type"""
        categories = {
            "infrastructure": [],
            "crop_development": [],
            "water_management": [],
            "technology": [],
            "credit_support": [],
            "insurance": []
        }
        
        for scheme in schemes:
            scheme_categories = scheme.get("categories", [])
            
            for category in scheme_categories:
                category_lower = category.lower()
                
                if any(keyword in category_lower for keyword in ["infrastructure", "equipment", "machinery"]):
                    categories["infrastructure"].append(scheme["name"])
                elif any(keyword in category_lower for keyword in ["crop", "seed", "fertilizer"]):
                    categories["crop_development"].append(scheme["name"])
                elif any(keyword in category_lower for keyword in ["water", "irrigation", "drip"]):
                    categories["water_management"].append(scheme["name"])
                elif any(keyword in category_lower for keyword in ["technology", "digital", "precision"]):
                    categories["technology"].append(scheme["name"])
                elif any(keyword in category_lower for keyword in ["credit", "loan", "finance"]):
                    categories["credit_support"].append(scheme["name"])
                elif any(keyword in category_lower for keyword in ["insurance", "risk", "protection"]):
                    categories["insurance"].append(scheme["name"])
        
        return {k: v for k, v in categories.items() if v}  # Remove empty categories