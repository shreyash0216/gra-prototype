import chromadb
from typing import List, Dict, Any
import os

class RAGRetriever:
    def __init__(self, collection_name: str = "gra_knowledge"):
        self.client = chromadb.Client()
        self.collection_name = collection_name
        self.collection = None
        self._initialize_collection()
    
    def _initialize_collection(self):
        """Initialize or get existing collection"""
        try:
            self.collection = self.client.get_collection(self.collection_name)
        except:
            self.collection = self.client.create_collection(self.collection_name)
    
    def add_documents(self, documents: List[str], metadatas: List[Dict] = None, ids: List[str] = None):
        """Add documents to the vector store"""
        if not ids:
            ids = [f"doc_{i}" for i in range(len(documents))]
        
        if not metadatas:
            metadatas = [{"source": "unknown"} for _ in documents]
        
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
    
    def retrieve(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """Retrieve relevant documents for a query"""
        if self.collection.count() == 0:
            return []
        
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        retrieved_docs = []
        for i, doc in enumerate(results['documents'][0]):
            retrieved_docs.append({
                'content': doc,
                'metadata': results['metadatas'][0][i] if results['metadatas'][0] else {},
                'distance': results['distances'][0][i] if results['distances'][0] else 0
            })
        
        return retrieved_docs
    
    def get_collection_info(self) -> Dict[str, Any]:
        """Get information about the current collection"""
        return {
            'name': self.collection_name,
            'count': self.collection.count()
        }