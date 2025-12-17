"""
Railway-compatible version of GRA Prototype
Uses simple in-memory retrieval instead of ChromaDB
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os

# Use simple retriever for Railway compatibility
from rag.simple_retriever import SimpleRAGRetriever
from rag.simple_ingestion import SimpleDocumentIngestion
from simulation.scenarios import ScenarioRunner
from prompts.templates import PromptManager

app = FastAPI(title="GRA Prototype API - Railway", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components with simple retriever
rag_retriever = SimpleRAGRetriever()
document_ingestion = SimpleDocumentIngestion(rag_retriever)
scenario_runner = ScenarioRunner()
prompt_manager = PromptManager()

class QueryRequest(BaseModel):
    query: str
    context: Optional[str] = None

class SimulationRequest(BaseModel):
    scenario_type: str
    parameters: dict

@app.get("/")
async def root():
    return {"message": "GRA Prototype API is running on Railway! 🚂"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "platform": "Railway",
        "retriever": "SimpleRAG",
        "documents": rag_retriever.count()
    }

@app.post("/query")
async def process_query(request: QueryRequest):
    try:
        # Retrieve relevant context
        context = rag_retriever.retrieve(request.query)
        
        # Generate response using prompt templates
        response = prompt_manager.generate_response(
            query=request.query,
            context=context,
            additional_context=request.context
        )
        
        return {"response": response, "context": context}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/simulate")
async def run_simulation(request: SimulationRequest):
    try:
        result = scenario_runner.run_scenario(
            scenario_type=request.scenario_type,
            parameters=request.parameters
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/scenarios")
async def list_scenarios():
    return {"scenarios": scenario_runner.get_available_scenarios()}

@app.post("/ingest-sample")
async def ingest_sample_data():
    try:
        result = document_ingestion.ingest_sample_data()
        return {"message": "Sample data ingested successfully", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)