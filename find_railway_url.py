#!/usr/bin/env python3
"""
Help find your Railway deployment URL
"""

import requests
import re

def test_common_railway_patterns(project_id):
    """Test common Railway URL patterns"""
    print("🔍 Testing common Railway URL patterns...")
    
    # Extract project ID from the URL you provided
    patterns = [
        f"https://web-production-{project_id[:5]}.up.railway.app",
        f"https://gra-prototype-production-{project_id[:5]}.up.railway.app",
        f"https://backend-production-{project_id[:5]}.up.railway.app",
        f"https://main-production-{project_id[:5]}.up.railway.app"
    ]
    
    for url in patterns:
        print(f"\n🧪 Testing: {url}")
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                try:
                    data = response.json()
                    if 'message' in data and 'GRA' in data['message']:
                        print(f"✅ FOUND IT! Your Railway URL is: {url}")
                        return url
                except:
                    pass
            print(f"   ❌ Not responding (HTTP {response.status_code})")
        except Exception as e:
            print(f"   ❌ Connection failed: {str(e)[:50]}...")
    
    return None

def main():
    print("🚂 Railway URL Finder")
    print("=" * 50)
    
    # Extract project ID from the URL you provided
    project_url = "https://railway.com/project/42d6c713-64ca-4869-8532-e8ac7e48bf87/settings"
    project_id = "42d6c713-64ca-4869-8532-e8ac7e48bf87"
    
    print(f"📋 Your Railway project ID: {project_id}")
    
    found_url = test_common_railway_patterns(project_id)
    
    if found_url:
        print(f"\n🎉 SUCCESS! Your GRA Prototype is live at:")
        print(f"🌐 {found_url}")
        print(f"\n📋 Test it:")
        print(f"   1. Open: {found_url}")
        print(f"   2. API Docs: {found_url}/docs")
        print(f"   3. Health Check: {found_url}/")
        
        # Test the app
        print(f"\n🧪 Quick functionality test:")
        try:
            # Test health
            response = requests.get(found_url, timeout=10)
            data = response.json()
            print(f"   ✅ Health: {data}")
            
            # Test sample data loading
            response = requests.post(f"{found_url}/ingest-sample", timeout=15)
            if response.status_code == 200:
                print(f"   ✅ Sample data loaded successfully")
            
            # Test query
            test_query = {"query": "What is RAG?", "context": "Testing"}
            response = requests.post(f"{found_url}/query", json=test_query, timeout=15)
            if response.status_code == 200:
                print(f"   ✅ Query processing works")
            
        except Exception as e:
            print(f"   ⚠️  Some features may need time to start: {e}")
    
    else:
        print(f"\n❌ Could not auto-detect your Railway URL")
        print(f"\n📋 Manual steps:")
        print(f"   1. Go to your Railway dashboard")
        print(f"   2. Click on your 'gra-prototype' project")
        print(f"   3. Look for 'Deployments' or 'Settings' tab")
        print(f"   4. Find the 'Public URL' or 'Domain' section")
        print(f"   5. Copy the URL (should end with .railway.app)")
        
        print(f"\n🔍 Or check Railway logs for:")
        print(f"   'Uvicorn running on http://0.0.0.0:8000'")
        print(f"   Your public URL should be shown nearby")

if __name__ == "__main__":
    main()