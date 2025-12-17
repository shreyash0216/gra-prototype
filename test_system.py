#!/usr/bin/env python3
"""
GRA Prototype Test Script
Run comprehensive tests on the GRA system
"""

import requests
import json
import time
from typing import Dict, Any

BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test if the API is running"""
    print("🔍 Testing Health Check...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_sample_data_ingestion():
    """Test loading sample data"""
    print("\n📚 Testing Sample Data Ingestion...")
    try:
        response = requests.post(f"{BASE_URL}/ingest-sample")
        if response.status_code == 200:
            result = response.json()
            print("✅ Sample data ingestion passed")
            print(f"   Ingested: {result['result']['ingested_count']} documents")
            print(f"   Total documents: {result['result']['total_documents']}")
            return True
        else:
            print(f"❌ Sample data ingestion failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Sample data ingestion error: {e}")
        return False

def test_query_processing():
    """Test query processing with different templates"""
    print("\n🤖 Testing Query Processing...")
    
    test_queries = [
        {
            "query": "What is RAG and how does it work?",
            "context": "I'm learning about AI systems"
        },
        {
            "query": "Explain simulation scenarios",
            "context": "I need to test system performance"
        },
        {
            "query": "How do prompt templates work?",
            "context": None
        }
    ]
    
    success_count = 0
    
    for i, test_query in enumerate(test_queries, 1):
        try:
            print(f"   Test Query {i}: {test_query['query'][:50]}...")
            response = requests.post(f"{BASE_URL}/query", json=test_query)
            
            if response.status_code == 200:
                result = response.json()
                print(f"   ✅ Query {i} successful")
                print(f"      Response length: {len(result['response'])} chars")
                print(f"      Context items: {len(result['context'])}")
                success_count += 1
            else:
                print(f"   ❌ Query {i} failed: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Query {i} error: {e}")
    
    print(f"\n   Query Processing Results: {success_count}/{len(test_queries)} passed")
    return success_count == len(test_queries)

def test_scenarios():
    """Test getting available scenarios"""
    print("\n📋 Testing Scenarios List...")
    try:
        response = requests.get(f"{BASE_URL}/scenarios")
        if response.status_code == 200:
            scenarios = response.json()['scenarios']
            print("✅ Scenarios list retrieved")
            print(f"   Available scenarios: {scenarios}")
            return scenarios
        else:
            print(f"❌ Scenarios list failed: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Scenarios list error: {e}")
        return []

def test_simulations():
    """Test running different simulations"""
    print("\n🎯 Testing Simulations...")
    
    test_simulations = [
        {
            "name": "Basic Query Test",
            "scenario_type": "basic_query",
            "parameters": {"query_count": 3, "delay": 0.1}
        },
        {
            "name": "Stress Test",
            "scenario_type": "stress_test", 
            "parameters": {"concurrent_users": 2, "queries_per_user": 5}
        },
        {
            "name": "Context Switching",
            "scenario_type": "context_switching",
            "parameters": {"context_switches": 3}
        },
        {
            "name": "Knowledge Gap",
            "scenario_type": "knowledge_gap",
            "parameters": {"query_count": 5, "knowledge_coverage": 0.8}
        }
    ]
    
    success_count = 0
    
    for sim in test_simulations:
        try:
            print(f"   Running {sim['name']}...")
            response = requests.post(f"{BASE_URL}/simulate", json={
                "scenario_type": sim["scenario_type"],
                "parameters": sim["parameters"]
            })
            
            if response.status_code == 200:
                result = response.json()['result']
                print(f"   ✅ {sim['name']} completed")
                
                # Print key metrics based on scenario type
                if sim['scenario_type'] == 'basic_query':
                    print(f"      Total queries: {result['total_queries']}")
                    print(f"      Success rate: {result['success_rate']:.2%}")
                    print(f"      Avg response time: {result['average_response_time']:.3f}s")
                elif sim['scenario_type'] == 'stress_test':
                    print(f"      Total queries: {result['total_queries']}")
                    print(f"      Failed queries: {result['failed_queries']}")
                    print(f"      Success rate: {result['success_rate']:.2%}")
                elif sim['scenario_type'] == 'context_switching':
                    print(f"      Context switches: {result['total_switches']}")
                    print(f"      Unique contexts: {result['unique_contexts']}")
                    print(f"      Avg accuracy: {result['average_accuracy']:.2%}")
                elif sim['scenario_type'] == 'knowledge_gap':
                    print(f"      Total queries: {result['total_queries']}")
                    print(f"      Queries with knowledge: {result['queries_with_knowledge']}")
                    print(f"      Avg confidence: {result['average_confidence']:.2%}")
                
                success_count += 1
            else:
                print(f"   ❌ {sim['name']} failed: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ {sim['name']} error: {e}")
    
    print(f"\n   Simulation Results: {success_count}/{len(test_simulations)} passed")
    return success_count == len(test_simulations)

def test_performance():
    """Test system performance"""
    print("\n⚡ Testing Performance...")
    
    # Test response times
    start_time = time.time()
    test_query = {"query": "Performance test query", "context": None}
    
    try:
        response = requests.post(f"{BASE_URL}/query", json=test_query)
        end_time = time.time()
        
        if response.status_code == 200:
            response_time = end_time - start_time
            print(f"✅ Performance test completed")
            print(f"   Response time: {response_time:.3f} seconds")
            
            if response_time < 1.0:
                print("   🚀 Excellent performance (< 1s)")
            elif response_time < 3.0:
                print("   👍 Good performance (< 3s)")
            else:
                print("   ⚠️  Slow performance (> 3s)")
            
            return True
        else:
            print(f"❌ Performance test failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Performance test error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 GRA Prototype System Test Suite")
    print("=" * 50)
    
    tests = [
        ("Health Check", test_health_check),
        ("Sample Data Ingestion", test_sample_data_ingestion),
        ("Query Processing", test_query_processing),
        ("Scenarios List", lambda: test_scenarios() != []),
        ("Simulations", test_simulations),
        ("Performance", test_performance)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        if test_func():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"🎯 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your GRA prototype is working perfectly!")
    else:
        print(f"⚠️  {total - passed} tests failed. Check the output above for details.")
    
    print("\n💡 Next steps:")
    print("   - Open frontend/index.html in your browser")
    print("   - Try the interactive interface")
    print("   - Load sample data and run queries")
    print("   - Experiment with different simulation scenarios")

if __name__ == "__main__":
    main()