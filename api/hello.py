from http.server import BaseHTTPRequestHandler
import json
import random
import time
from urllib.parse import urlparse, parse_qs

# Sample data for the prototype
SAMPLE_DATA = [
    {
        'content': 'GRA (Generative Retrieval-Augmented) systems combine the power of large language models with external knowledge retrieval.',
        'metadata': {'source': 'sample', 'topic': 'gra_overview'},
        'id': 'sample_0'
    },
    {
        'content': 'RAG systems work by first retrieving relevant documents from a knowledge base, then using those documents as context for generation.',
        'metadata': {'source': 'sample', 'topic': 'rag_explanation'},
        'id': 'sample_1'
    },
    {
        'content': 'Simulation scenarios help test and validate AI system behavior under different conditions and constraints.',
        'metadata': {'source': 'sample', 'topic': 'simulation'},
        'id': 'sample_2'
    },
    {
        'content': 'Prompt engineering is crucial for getting optimal performance from language models in specific domains.',
        'metadata': {'source': 'sample', 'topic': 'prompt_engineering'},
        'id': 'sample_3'
    }
]

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        path = self.path
        
        if path == '/api' or path == '/api/':
            response = {
                "message": "GRA Prototype API is running on Vercel! 🚀",
                "status": "healthy",
                "version": "1.0.0",
                "endpoints": ["/api/query", "/api/simulate", "/api/scenarios", "/api/ingest-sample"]
            }
        elif path == '/api/scenarios':
            response = {
                "scenarios": ["basic_query", "stress_test", "context_switching", "knowledge_gap"]
            }
        else:
            response = {
                "message": "GRA Prototype API is running on Vercel! 🚀",
                "status": "healthy"
            }
        
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length) if content_length > 0 else b'{}'
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            path = self.path
            
            if path == '/api/ingest-sample':
                response = {
                    "message": "Sample data loaded successfully! 🎉",
                    "result": {
                        "ingested_count": len(SAMPLE_DATA),
                        "total_documents": len(SAMPLE_DATA)
                    }
                }
            
            elif path == '/api/query':
                try:
                    data = json.loads(post_data.decode('utf-8'))
                    query = data.get("query", "")
                    context_input = data.get("context", "")
                    
                    # Simple retrieval simulation
                    relevant_docs = []
                    query_lower = query.lower()
                    
                    for doc in SAMPLE_DATA:
                        if any(word in doc['content'].lower() for word in query_lower.split()):
                            relevant_docs.append({
                                'content': doc['content'],
                                'metadata': doc['metadata'],
                                'distance': random.uniform(0.1, 0.3)
                            })
                    
                    # If no matches, return all docs
                    if not relevant_docs:
                        relevant_docs = [{
                            'content': doc['content'],
                            'metadata': doc['metadata'],
                            'distance': random.uniform(0.4, 0.6)
                        } for doc in SAMPLE_DATA]
                    
                    # Generate response based on query
                    if "rag" in query_lower or "retrieval" in query_lower:
                        ai_response = "RAG (Retrieval-Augmented Generation) systems combine large language models with external knowledge retrieval. They work by first finding relevant documents from a knowledge base, then using those documents as context to generate more accurate and informed responses. This approach helps overcome the limitations of pure language models by grounding responses in factual, up-to-date information."
                    elif "simulation" in query_lower or "test" in query_lower:
                        ai_response = "Simulation scenarios are essential for testing AI system behavior under various conditions. They help validate system performance, identify edge cases, and ensure reliability. The GRA prototype includes multiple simulation types: basic query testing, stress testing with concurrent users, context switching validation, and knowledge gap analysis."
                    elif "gra" in query_lower or "generative" in query_lower:
                        ai_response = "GRA (Generative Retrieval-Augmented) systems represent an advanced approach to AI that combines the generative capabilities of large language models with sophisticated document retrieval mechanisms. This creates more accurate, contextual, and reliable AI responses by grounding generation in relevant retrieved information."
                    else:
                        ai_response = f"Based on your query about '{query}', I can provide information using the retrieved context. The system has successfully found {len(relevant_docs)} relevant documents to help answer your question. This demonstrates the RAG system's ability to retrieve and utilize relevant information for generating contextual responses."
                    
                    if context_input:
                        ai_response += f" Given your additional context about '{context_input}', this information helps tailor the response to your specific needs."
                    
                    response = {
                        "response": ai_response,
                        "context": relevant_docs[:4]  # Return top 4 matches
                    }
                    
                except json.JSONDecodeError:
                    response = {"error": "Invalid JSON data"}
                except Exception as e:
                    response = {"error": f"Query processing error: {str(e)}"}
            
            elif path == '/api/simulate':
                try:
                    data = json.loads(post_data.decode('utf-8'))
                    scenario_type = data.get("scenario_type", "basic_query")
                    parameters = data.get("parameters", {})
                    
                    # Simulate different scenarios
                    if scenario_type == "basic_query":
                        query_count = parameters.get('query_count', 5)
                        delay = parameters.get('delay', 0.1)
                        
                        result = {
                            'scenario': 'basic_query',
                            'total_queries': query_count,
                            'success_rate': random.uniform(0.95, 1.0),
                            'average_response_time': delay + random.uniform(0.05, 0.15),
                            'total_tokens': query_count * random.randint(50, 200),
                            'total_time': query_count * delay + random.uniform(0.1, 0.5)
                        }
                    
                    elif scenario_type == "stress_test":
                        concurrent_users = parameters.get('concurrent_users', 3)
                        queries_per_user = parameters.get('queries_per_user', 10)
                        total_queries = concurrent_users * queries_per_user
                        
                        result = {
                            'scenario': 'stress_test',
                            'concurrent_users': concurrent_users,
                            'queries_per_user': queries_per_user,
                            'total_queries': total_queries,
                            'failed_queries': random.randint(0, max(1, total_queries // 20)),
                            'success_rate': random.uniform(0.90, 0.98),
                            'average_response_time': random.uniform(0.5, 1.5),
                            'peak_memory_usage': f"{random.randint(200, 400)}MB",
                            'cpu_utilization': f"{random.randint(60, 85)}%"
                        }
                    
                    elif scenario_type == "context_switching":
                        context_switches = parameters.get('context_switches', 5)
                        
                        result = {
                            'scenario': 'context_switching',
                            'total_switches': context_switches,
                            'unique_contexts': min(context_switches, random.randint(2, 4)),
                            'average_response_time': random.uniform(0.2, 0.4),
                            'average_accuracy': random.uniform(0.85, 0.95),
                            'context_changes': random.randint(context_switches // 2, context_switches)
                        }
                    
                    elif scenario_type == "knowledge_gap":
                        query_count = parameters.get('query_count', 15)
                        knowledge_coverage = parameters.get('knowledge_coverage', 0.7)
                        
                        queries_with_knowledge = int(query_count * knowledge_coverage)
                        
                        result = {
                            'scenario': 'knowledge_gap',
                            'total_queries': query_count,
                            'knowledge_coverage': knowledge_coverage,
                            'queries_with_knowledge': queries_with_knowledge,
                            'average_confidence': random.uniform(0.6, 0.9),
                            'average_quality': random.uniform(0.7, 0.9),
                            'fallback_usage': query_count - queries_with_knowledge
                        }
                    
                    else:
                        result = {
                            'scenario': scenario_type,
                            'error': 'Unknown scenario type'
                        }
                    
                    response = {"result": result}
                    
                except json.JSONDecodeError:
                    response = {"error": "Invalid JSON data"}
                except Exception as e:
                    response = {"error": f"Simulation error: {str(e)}"}
            
            else:
                response = {"error": "Unknown endpoint"}
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {"error": f"Server error: {str(e)}"}
        
        self.wfile.write(json.dumps(response).encode())