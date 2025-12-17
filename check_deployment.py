#!/usr/bin/env python3
"""
Check if the Climate Adaptation System deployment is working
"""

import requests
import json
import sys

def check_deployment(base_url):
    """Check if deployment is working correctly"""
    
    print(f"🌱 Checking Climate Adaptation System at: {base_url}")
    print("=" * 60)
    
    try:
        # Test 1: Frontend
        print("1. Testing Frontend...")
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200 and "Climate Adaptation System" in response.text:
            print("   ✅ Frontend is working")
        else:
            print(f"   ❌ Frontend issue: {response.status_code}")
            return False
        
        # Test 2: API Health
        print("\n2. Testing API Health...")
        api_url = f"{base_url}/api" if not base_url.endswith('/api') else base_url
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ API is working: {data.get('message', 'OK')}")
        else:
            print(f"   ❌ API issue: {response.status_code}")
            return False
        
        # Test 3: Crops Database
        print("\n3. Testing Crops Database...")
        response = requests.get(f"{api_url}/crops", timeout=10)
        if response.status_code == 200:
            data = response.json()
            crop_count = len(data.get('crops', []))
            print(f"   ✅ Crops database loaded: {crop_count} crops")
        else:
            print(f"   ❌ Crops database issue: {response.status_code}")
        
        # Test 4: Schemes Database
        print("\n4. Testing Schemes Database...")
        response = requests.get(f"{api_url}/schemes", timeout=10)
        if response.status_code == 200:
            data = response.json()
            scheme_count = len(data.get('schemes', []))
            print(f"   ✅ Schemes database loaded: {scheme_count} schemes")
        else:
            print(f"   ❌ Schemes database issue: {response.status_code}")
        
        # Test 5: Sample Analysis (if possible)
        print("\n5. Testing Sample Analysis...")
        sample_request = {
            "farm_details": {
                "location": "Pune, Maharashtra",
                "farm_size": 5.0,
                "soil_type": "black",
                "water_source": "borewell",
                "current_crops": ["rice"],
                "budget": 100000,
                "experience_level": "intermediate"
            },
            "climate_concerns": ["drought"],
            "adaptation_goals": ["increase yield"]
        }
        
        response = requests.post(
            f"{api_url}/analyze-climate",
            json=sample_request,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("   ✅ Climate analysis working")
                plan = data.get('adaptation_plan', {})
                if plan.get('crop_recommendations'):
                    crops = plan['crop_recommendations'].get('recommended_crops', [])
                    print(f"   📊 Sample result: {len(crops)} crops recommended")
            else:
                print("   ⚠️ Analysis returned but with issues")
        else:
            print(f"   ⚠️ Analysis endpoint issue: {response.status_code}")
        
        print("\n" + "=" * 60)
        print("🎉 Deployment Check Complete!")
        print(f"✅ Your Climate Adaptation System is live at: {base_url}")
        print("\n📱 Try it out:")
        print("1. Fill in your farm details")
        print("2. Specify climate concerns")
        print("3. Get AI-powered recommendations!")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Connection error: {e}")
        print("Make sure the URL is correct and the site is deployed.")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_deployment.py <deployment_url>")
        print("Example: python check_deployment.py https://your-app.vercel.app")
        sys.exit(1)
    
    url = sys.argv[1].rstrip('/')
    success = check_deployment(url)
    sys.exit(0 if success else 1)