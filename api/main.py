from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

# Simple in-memory storage for Vercel (serverless)
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

app = FastAPI(title="GRA Prototype API - Vercel", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str
    context: Optional[str] = None

class SimulationRequest(BaseModel):
    scenario_type: str
    parameters: dict

@app.get("/")
async def root():
    return {"message": "GRA Prototype API is running on Vercel! 🚀"}

@app.get("/api")
async def api_root():
    return {"message": "GRA Prototype API is running on Vercel! 🚀"}

@app.post("/api/query")
async def process_query(request: QueryRequest):
    try:
        # Simple retrieval from sample data
        context = []
        query_lower = request.query.lower()
        
        for doc in SAMPLE_DATA:
            if any(word in doc['content'].lower() for word in query_lower.split()):
                context.append({
                    'content': doc['content'],
                    'metadata': doc['metadata'],
                    'distance': 0.1
                })
        
        # If no matches, return all sample data
        if not context:
            context = [{'content': doc['content'], 'metadata': doc['metadata'], 'distance': 0.5} for doc in SAMPLE_DATA]
        
        # Generate response (simplified for Vercel)
        response = f"Based on the provided context about {request.query}, here's what I found: The system demonstrates RAG capabilities with document retrieval and response generation. This is a serverless implementation running on Vercel."
        
        return {"response": response, "context": context[:4]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/simulate")
async def run_simulation(request: SimulationRequest):
    try:
        import random
        import time
        
        scenario_type = request.scenario_type
        parameters = request.parameters
        
        # Simplified simulation for serverless
        if scenario_type == "basic_query":
            query_count = parameters.get('query_count', 5)
            result = {
                'scenario': 'basic_query',
                'total_queries': query_count,
                'success_rate': random.uniform(0.9, 1.0),
                'average_response_time': random.uniform(0.1, 0.3),
                'total_tokens': query_count * random.randint(50, 200)
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
                'success_rate': random.uniform(0.85, 0.98),
                'average_response_time': random.uniform(0.5, 1.5)
            }
        else:
            # Default simulation
            result = {
                'scenario': scenario_type,
                'success_rate': random.uniform(0.8, 0.95),
                'average_response_time': random.uniform(0.2, 0.8)
            }
        
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/scenarios")
async def list_scenarios():
    return {"scenarios": ["basic_query", "stress_test", "context_switching", "knowledge_gap"]}

@app.post("/api/ingest-sample")
async def ingest_sample_data():
    try:
        return {
            "message": "Sample data loaded successfully (in-memory for Vercel)",
            "result": {
                "ingested_count": len(SAMPLE_DATA),
                "total_documents": len(SAMPLE_DATA)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# For Vercel serverless functions
def handler(request):
    return app