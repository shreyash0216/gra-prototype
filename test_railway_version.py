#!/usr/bin/env python3
"""
Test the Railway-compatible version locally
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from rag.simple_retriever import SimpleRAGRetriever
from rag.simple_ingestion import SimpleDocumentIngestion

def test_simple_rag():
    """Test the simple RAG system"""
    print("🧪 Testing Railway-Compatible RAG System")
    print("=" * 50)
    
    # Test retriever
    print("\n1. Testing Simple Retriever...")
    retriever = SimpleRAGRetriever()
    
    # Test ingestion
    print("2. Testing Document Ingestion...")
    ingestion = SimpleDocumentIngestion(retriever)
    result = ingestion.ingest_sample_data()
    
    print(f"   ✅ Ingested {result['ingested_count']} documents")
    print(f"   📊 Total documents: {result['total_documents']}")
    
    # Test retrieval
    print("\n3. Testing Document Retrieval...")
    query = "What is RAG and how does it work?"
    results = retriever.retrieve(query)
    
    print(f"   ✅ Retrieved {len(results)} documents for query: '{query}'")
    for i, doc in enumerate(results[:2]):
        print(f"   📄 Doc {i+1}: {doc['content'][:100]}...")
    
    # Test collection info
    print("\n4. Testing Collection Info...")
    info = retriever.get_collection_info()
    print(f"   ✅ Collection: {info['name']}")
    print(f"   📊 Document count: {info['count']}")
    
    print("\n🎉 Railway-compatible RAG system is working!")
    return True

if __name__ == "__main__":
    test_simple_rag()