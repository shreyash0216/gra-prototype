"""
Simple document ingestion for Railway deployment
"""

import os
import json
from typing import List, Dict, Any
from pathlib import Path
from .simple_retriever import SimpleRAGRetriever

class SimpleDocumentIngestion:
    def __init__(self, retriever: SimpleRAGRetriever = None):
        self.retriever = retriever or SimpleRAGRetriever()
        self.data_dir = Path(__file__).parent.parent / "data"
    
    def ingest_sample_data(self) -> Dict[str, Any]:
        """Ingest sample data for testing"""
        sample_docs = [
            "GRA (Generative Retrieval-Augmented) systems combine the power of large language models with external knowledge retrieval. These systems first retrieve relevant documents from a knowledge base, then use those documents as context for generating responses.",
            "RAG systems work by first retrieving relevant documents from a knowledge base using vector similarity search, then using those documents as context for generation. This approach allows AI systems to access up-to-date information beyond their training data.",
            "Simulation scenarios help test and validate AI system behavior under different conditions and constraints. Common scenarios include basic query testing, stress testing with multiple concurrent users, context switching between topics, and knowledge gap analysis.",
            "Prompt engineering is crucial for getting optimal performance from language models in specific domains. Different prompt templates like analytical, creative, technical, and summarization templates can be used to guide the model's response style and focus.",
            "Performance testing of AI systems involves measuring response times, success rates, throughput, and resource utilization under various load conditions. This helps identify bottlenecks and optimize system performance.",
            "Vector databases like ChromaDB, Pinecone, and Weaviate are designed to store and search high-dimensional embeddings efficiently. They enable semantic search capabilities that power RAG systems.",
            "FastAPI is a modern Python web framework that provides automatic API documentation, type validation, and high performance for building REST APIs. It's commonly used for deploying AI and machine learning models.",
            "Deployment platforms like Railway, Render, and Heroku provide easy ways to deploy web applications to the cloud. They handle infrastructure management, scaling, and provide free tiers for prototyping."
        ]
        
        metadatas = [
            {'source': 'sample', 'topic': 'gra_overview', 'category': 'systems'},
            {'source': 'sample', 'topic': 'rag_explanation', 'category': 'ai'},
            {'source': 'sample', 'topic': 'simulation', 'category': 'testing'},
            {'source': 'sample', 'topic': 'prompt_engineering', 'category': 'ai'},
            {'source': 'sample', 'topic': 'performance_testing', 'category': 'testing'},
            {'source': 'sample', 'topic': 'vector_databases', 'category': 'technology'},
            {'source': 'sample', 'topic': 'fastapi', 'category': 'technology'},
            {'source': 'sample', 'topic': 'deployment', 'category': 'devops'}
        ]
        
        ids = [f"sample_{i}" for i in range(len(sample_docs))]
        
        self.retriever.add_documents(sample_docs, metadatas, ids)
        
        return {
            'ingested_count': len(sample_docs),
            'total_documents': self.retriever.get_collection_info()['count']
        }