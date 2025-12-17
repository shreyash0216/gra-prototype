#!/usr/bin/env python3
"""
Advanced Query Testing for GRA Prototype
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_advanced_queries():
    """Test various types of queries"""
    print("🔬 Advanced Query Testing")
    print("=" * 50)
    
    # Load test queries
    with open('advanced_test_queries.json', 'r') as f:
        test_queries = json.load(f)
    
    results = []
    
    for i, test_case in enumerate(test_queries, 1):
        print(f"\n📝 Test {i}: {test_case['name']}")
        print(f"   Query: {test_case['query']}")
        print(f"   Context: {test_case['context']}")
        
        start_time = time.time()
        
        try:
            response = requests.post(f"{BASE_URL}/query", json={
                "query": test_case['query'],
                "context": test_case['context']
            })
            
            end_time = time.time()
            response_time = end_time - start_time
            
            if response.status_code == 200:
                result = response.json()
                
                print(f"   ✅ Success ({response_time:.2f}s)")
                print(f"   📄 Response: {result['response'][:100]}...")
                print(f"   🔍 Context items retrieved: {len(result['context'])}")
                
                # Analyze response quality
                response_length = len(result['response'])
                context_count = len(result['context'])
                
                quality_score = "Good"
                if response_length < 50:
                    quality_score = "Short"
                elif response_length > 500:
                    quality_score = "Detailed"
                
                print(f"   📊 Quality: {quality_score} ({response_length} chars)")
                
                results.append({
                    "test": test_case['name'],
                    "success": True,
                    "response_time": response_time,
                    "response_length": response_length,
                    "context_count": context_count,
                    "quality": quality_score
                })
                
            else:
                print(f"   ❌ Failed: HTTP {response.status_code}")
                results.append({
                    "test": test_case['name'],
                    "success": False,
                    "error": f"HTTP {response.status_code}"
                })
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
            results.append({
                "test": test_case['name'],
                "success": False,
                "error": str(e)
            })
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Advanced Query Test Summary")
    print("=" * 50)
    
    successful_tests = [r for r in results if r['success']]
    
    print(f"✅ Successful tests: {len(successful_tests)}/{len(results)}")
    
    if successful_tests:
        avg_response_time = sum(r['response_time'] for r in successful_tests) / len(successful_tests)
        avg_response_length = sum(r['response_length'] for r in successful_tests) / len(successful_tests)
        avg_context_count = sum(r['context_count'] for r in successful_tests) / len(successful_tests)
        
        print(f"⏱️  Average response time: {avg_response_time:.2f}s")
        print(f"📝 Average response length: {avg_response_length:.0f} characters")
        print(f"🔍 Average context items: {avg_context_count:.1f}")
        
        # Performance rating
        if avg_response_time < 1.0:
            print("🚀 Performance: Excellent")
        elif avg_response_time < 2.0:
            print("👍 Performance: Good")
        elif avg_response_time < 3.0:
            print("⚠️  Performance: Acceptable")
        else:
            print("🐌 Performance: Needs improvement")
    
    return results

if __name__ == "__main__":
    test_advanced_queries()