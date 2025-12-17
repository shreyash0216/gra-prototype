#!/usr/bin/env python3
"""
Test the deployed GRA prototype on Railway
"""

import requests
import json
import time

def test_deployed_app(base_url):
    """Test the deployed application"""
    print(f"🧪 Testing Deployed GRA Prototype")
    print(f"🌐 URL: {base_url}")
    print("=" * 60)
    
    # Test 1: Health Check
    print("\n🔍 Test 1: Health Check")
    try:
        response = requests.get(f"{base_url}/", timeout=30)
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False
    
    # Test 2: Load Sample Data
    print("\n📚 Test 2: Loading Sample Data")
    try:
        response = requests.post(f"{base_url}/ingest-sample", timeout=30)
        if response.status_code == 200:
            result = response.json()
            print("✅ Sample data loaded successfully!")
            print(f"   Documents ingested: {result['result']['ingested_count']}")
        else:
            print(f"❌ Sample data loading failed: HTTP {response.status_code}")
    except Exception as e:
        print(f"❌ Sample data loading error: {e}")
    
    # Test 3: Query Processing
    print("\n🤖 Test 3: Query Processing")
    test_query = {
        "query": "What is RAG and how does it work?",
        "context": "I'm testing the deployed system"
    }
    
    try:
        response = requests.post(f"{base_url}/query", json=test_query, timeout=30)
        if response.status_code == 200:
            result = response.json()
            print("✅ Query processing works!")
            print(f"   Response length: {len(result['response'])} characters")
            print(f"   Context items: {len(result['context'])}")
            print(f"   Sample response: {result['response'][:100]}...")
        else:
            print(f"❌ Query processing failed: HTTP {response.status_code}")
    except Exception as e:
        print(f"❌ Query processing error: {e}")
    
    # Test 4: Simulation
    print("\n🎯 Test 4: Simulation Testing")
    simulation_request = {
        "scenario_type": "basic_query",
        "parameters": {"query_count": 3, "delay": 0.1}
    }
    
    try:
        response = requests.post(f"{base_url}/simulate", json=simulation_request, timeout=30)
        if response.status_code == 200:
            result = response.json()['result']
            print("✅ Simulation works!")
            print(f"   Success rate: {result['success_rate']:.1%}")
            print(f"   Average response time: {result['average_response_time']:.3f}s")
        else:
            print(f"❌ Simulation failed: HTTP {response.status_code}")
    except Exception as e:
        print(f"❌ Simulation error: {e}")
    
    # Test 5: Scenarios List
    print("\n📋 Test 5: Available Scenarios")
    try:
        response = requests.get(f"{base_url}/scenarios", timeout=30)
        if response.status_code == 200:
            scenarios = response.json()['scenarios']
            print("✅ Scenarios endpoint works!")
            print(f"   Available scenarios: {scenarios}")
        else:
            print(f"❌ Scenarios endpoint failed: HTTP {response.status_code}")
    except Exception as e:
        print(f"❌ Scenarios endpoint error: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 Deployment Testing Complete!")
    print(f"\n🌐 Your GRA Prototype is live at: {base_url}")
    print("\n💡 Next Steps:")
    print("   1. Open the URL in your browser")
    print("   2. Test the web interface")
    print("   3. Share the URL with others!")
    
    return True

def main():
    """Main function to test deployed app"""
    print("🚀 Railway Deployment Tester")
    print("=" * 60)
    
    # You'll need to replace this with your actual Railway URL
    print("📝 Please enter your Railway app URL:")
    print("   (It should look like: https://gra-prototype-production-xxxx.up.railway.app)")
    
    base_url = input("\nEnter your Railway URL: ").strip()
    
    if not base_url:
        print("❌ No URL provided. Please check your Railway dashboard for the public URL.")
        return
    
    if not base_url.startswith('http'):
        base_url = 'https://' + base_url
    
    # Remove trailing slash
    base_url = base_url.rstrip('/')
    
    test_deployed_app(base_url)

if __name__ == "__main__":
    main()