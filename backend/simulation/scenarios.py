from typing import Dict, Any, List
import random
import time

class ScenarioRunner:
    def __init__(self):
        self.scenarios = {
            'basic_query': self._basic_query_scenario,
            'stress_test': self._stress_test_scenario,
            'context_switching': self._context_switching_scenario,
            'knowledge_gap': self._knowledge_gap_scenario
        }
    
    def get_available_scenarios(self) -> List[str]:
        """Get list of available simulation scenarios"""
        return list(self.scenarios.keys())
    
    def run_scenario(self, scenario_type: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Run a specific simulation scenario"""
        if scenario_type not in self.scenarios:
            raise ValueError(f"Unknown scenario type: {scenario_type}")
        
        return self.scenarios[scenario_type](parameters)
    
    def _basic_query_scenario(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate basic query processing"""
        query_count = parameters.get('query_count', 10)
        delay = parameters.get('delay', 0.1)
        
        results = []
        start_time = time.time()
        
        for i in range(query_count):
            # Simulate query processing
            time.sleep(delay)
            
            result = {
                'query_id': i,
                'response_time': delay + random.uniform(0, 0.05),
                'success': random.random() > 0.05,  # 95% success rate
                'tokens_used': random.randint(50, 200)
            }
            results.append(result)
        
        total_time = time.time() - start_time
        
        return {
            'scenario': 'basic_query',
            'total_queries': query_count,
            'total_time': total_time,
            'average_response_time': sum(r['response_time'] for r in results) / len(results),
            'success_rate': sum(1 for r in results if r['success']) / len(results),
            'total_tokens': sum(r['tokens_used'] for r in results),
            'results': results
        }
    
    def _stress_test_scenario(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate high-load stress testing"""
        concurrent_users = parameters.get('concurrent_users', 5)
        queries_per_user = parameters.get('queries_per_user', 20)
        
        # Simulate concurrent load
        total_queries = concurrent_users * queries_per_user
        failed_queries = int(total_queries * random.uniform(0.02, 0.08))  # 2-8% failure rate under stress
        
        return {
            'scenario': 'stress_test',
            'concurrent_users': concurrent_users,
            'queries_per_user': queries_per_user,
            'total_queries': total_queries,
            'failed_queries': failed_queries,
            'success_rate': (total_queries - failed_queries) / total_queries,
            'average_response_time': random.uniform(0.5, 2.0),  # Higher response time under load
            'peak_memory_usage': f"{random.randint(200, 500)}MB",
            'cpu_utilization': f"{random.randint(60, 95)}%"
        }
    
    def _context_switching_scenario(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate context switching between different topics"""
        context_switches = parameters.get('context_switches', 5)
        topics = parameters.get('topics', ['technology', 'science', 'business', 'health'])
        
        results = []
        current_context = None
        
        for i in range(context_switches):
            new_context = random.choice(topics)
            context_change = new_context != current_context
            
            # Simulate performance impact of context switching
            response_time = random.uniform(0.1, 0.3)
            if context_change:
                response_time += random.uniform(0.05, 0.15)  # Additional time for context switch
            
            results.append({
                'switch_id': i,
                'previous_context': current_context,
                'new_context': new_context,
                'context_changed': context_change,
                'response_time': response_time,
                'accuracy_score': random.uniform(0.8, 0.98)
            })
            
            current_context = new_context
        
        return {
            'scenario': 'context_switching',
            'total_switches': context_switches,
            'unique_contexts': len(set(r['new_context'] for r in results)),
            'average_response_time': sum(r['response_time'] for r in results) / len(results),
            'average_accuracy': sum(r['accuracy_score'] for r in results) / len(results),
            'context_changes': sum(1 for r in results if r['context_changed']),
            'results': results
        }
    
    def _knowledge_gap_scenario(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate queries with varying knowledge availability"""
        query_count = parameters.get('query_count', 15)
        knowledge_coverage = parameters.get('knowledge_coverage', 0.7)  # 70% of queries have good knowledge
        
        results = []
        
        for i in range(query_count):
            has_knowledge = random.random() < knowledge_coverage
            
            if has_knowledge:
                confidence = random.uniform(0.8, 0.95)
                response_quality = random.uniform(0.85, 0.98)
                retrieval_count = random.randint(3, 8)
            else:
                confidence = random.uniform(0.3, 0.6)
                response_quality = random.uniform(0.4, 0.7)
                retrieval_count = random.randint(0, 2)
            
            results.append({
                'query_id': i,
                'has_knowledge': has_knowledge,
                'confidence_score': confidence,
                'response_quality': response_quality,
                'retrieved_documents': retrieval_count,
                'fallback_used': not has_knowledge and random.random() > 0.3
            })
        
        return {
            'scenario': 'knowledge_gap',
            'total_queries': query_count,
            'knowledge_coverage': knowledge_coverage,
            'queries_with_knowledge': sum(1 for r in results if r['has_knowledge']),
            'average_confidence': sum(r['confidence_score'] for r in results) / len(results),
            'average_quality': sum(r['response_quality'] for r in results) / len(results),
            'fallback_usage': sum(1 for r in results if r['fallback_used']),
            'results': results
        }