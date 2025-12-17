#!/usr/bin/env python3
"""
Test script for Climate Adaptation System
Run this to verify the system is working correctly
"""

import sys
import os
import asyncio
import json

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

async def test_climate_adaptation_system():
    """Test the main components of the climate adaptation system"""
    
    print("🌱 Testing Climate Adaptation System...")
    print("=" * 50)
    
    try:
        # Test imports
        print("1. Testing imports...")
        from agents.climate_analyzer import ClimateAnalyzer
        from agents.crop_advisor import CropAdvisor
        from agents.market_analyzer import MarketAnalyzer
        from agents.scheme_finder import SchemeFinder
        from utils.svg_generator import SVGGenerator
        from data.knowledge_base import get_crops_data, get_schemes_data, get_market_data
        print("   ✅ All imports successful")
        
        # Test knowledge base
        print("\n2. Testing knowledge base...")
        crops = get_crops_data()
        schemes = get_schemes_data()
        market_data = get_market_data()
        print(f"   ✅ Loaded {len(crops)} crops, {len(schemes)} schemes")
        
        # Test climate analyzer
        print("\n3. Testing Climate Analyzer...")
        climate_analyzer = ClimateAnalyzer()
        climate_result = await climate_analyzer.analyze_risks(
            location="Pune, Maharashtra",
            concerns=["drought", "irregular_rainfall"]
        )
        print(f"   ✅ Identified {len(climate_result['risks'])} climate risks")
        print(f"   📊 Urgency level: {climate_result['urgency_level']}")
        
        # Test crop advisor
        print("\n4. Testing Crop Advisor...")
        crop_advisor = CropAdvisor()
        farm_details = {
            "location": "Pune, Maharashtra",
            "farm_size": 5.0,
            "soil_type": "black",
            "water_source": "borewell",
            "budget": 100000,
            "experience_level": "intermediate"
        }
        crop_result = await crop_advisor.recommend_crops(farm_details, climate_result['risks'])
        print(f"   ✅ Recommended {len(crop_result['recommended_crops'])} crops")
        print(f"   🌾 Top crops: {', '.join(crop_result['recommended_crops'][:3])}")
        
        # Test market analyzer
        print("\n5. Testing Market Analyzer...")
        market_analyzer = MarketAnalyzer()
        market_result = await market_analyzer.analyze_market_potential(
            crops=crop_result['recommended_crops'][:3],
            location="Pune, Maharashtra"
        )
        print(f"   ✅ Analyzed market for {len(market_result['crop_market_analysis'])} crops")
        
        # Test scheme finder
        print("\n6. Testing Scheme Finder...")
        scheme_finder = SchemeFinder()
        scheme_result = await scheme_finder.find_relevant_schemes(
            farm_details=farm_details,
            adaptation_goals=["increase yield", "water conservation"]
        )
        print(f"   ✅ Found {len(scheme_result['recommended_schemes'])} relevant schemes")
        print(f"   💰 Total potential subsidy: ₹{scheme_result['total_potential_subsidy']['total_subsidy_amount']:,}")
        
        # Test SVG generator
        print("\n7. Testing SVG Generator...")
        svg_generator = SVGGenerator()
        svg_content = svg_generator.generate_farm_layout(
            farm_size=5.0,
            recommended_crops=crop_result['recommended_crops'][:3],
            water_source="borewell"
        )
        print(f"   ✅ Generated SVG layout ({len(svg_content)} characters)")
        
        # Test database models
        print("\n8. Testing Database Models...")
        from database.models import Base, engine
        Base.metadata.create_all(bind=engine)
        print("   ✅ Database tables created successfully")
        
        print("\n" + "=" * 50)
        print("🎉 All tests passed! Climate Adaptation System is ready.")
        print("\nTo run the system:")
        print("1. Backend: cd backend && python main.py")
        print("2. Frontend: Open frontend/index.html in browser")
        print("\nSample test data:")
        print(f"- Location: {farm_details['location']}")
        print(f"- Farm size: {farm_details['farm_size']} acres")
        print(f"- Recommended crops: {', '.join(crop_result['recommended_crops'][:3])}")
        print(f"- Climate risks: {', '.join(climate_result['risks'][:3])}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_climate_adaptation_system())
    sys.exit(0 if success else 1)