"""
Simple in-memory retriever for Railway deployment
Replaces ChromaDB to avoid compatibility issues
"""

from typing import List, Dict, Any
import json
import re

class SimpleRAGRetriever:
    def __init__(self, collection_name: str = "gra_knowledge"):
        self.collection_name = collection_name
        self.documents = []
        self.metadatas = []
        self.ids = []
    
    def add_documents(self, documents: List[str], metadatas: List[Dict] = None, ids: List[str] = None):
        """Add documents to the simple in-memory store"""
        if not ids:
            ids = [f"doc_{len(self.documents) + i}" for i in range(len(documents))]
        
        if not metadatas:
            metadatas = [{"source": "unknown"} for _ in documents]
        
        self.documents.extend(documents)
        self.metadatas.extend(metadatas)
        self.ids.extend(ids)
    
    def retrieve(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """Simple keyword-based retrieval"""
        if not self.documents:
            return []
        
        # Simple keyword matching
        query_words = set(query.lower().split())
        scores = []
        
        for i, doc in enumerate(self.documents):
            doc_words = set(doc.lower().split())
            # Calculate simple overlap score
            overlap = len(query_words.intersection(doc_words))
            total_words = len(query_words.union(doc_words))
            score = overlap / total_words if total_words > 0 else 0
            scores.append((score, i))
        
        # Sort by score and get top results
        scores.sort(reverse=True)
        top_indices = [idx for _, idx in scores[:n_results]]
        
        retrieved_docs = []
        for i in top_indices:
            retrieved_docs.append({
                'content': self.documents[i],
                'metadata': self.metadatas[i] if i < len(self.metadatas) else {},
                'distance': 1 - scores[i][0]  # Convert similarity to distance
            })
        
        return retrieved_docs
    
    def get_collection_info(self) -> Dict[str, Any]:
        """Get information about the current collection"""
        return {
            'name': self.collection_name,
            'count': len(self.documents)
        }
    
    def count(self) -> int:
        """Get document count"""
        return len(self.documents)