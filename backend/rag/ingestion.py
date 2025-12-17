import os
import json
from typing import List, Dict, Any
from pathlib import Path
from .retriever import RAGRetriever

class DocumentIngestion:
    def __init__(self, retriever: RAGRetriever = None):
        self.retriever = retriever or RAGRetriever()
        self.data_dir = Path(__file__).parent.parent / "data"
    
    def ingest_text_files(self, file_paths: List[str]) -> Dict[str, Any]:
        """Ingest text files into the vector store"""
        documents = []
        metadatas = []
        ids = []
        
        for i, file_path in enumerate(file_paths):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                documents.append(content)
                metadatas.append({
                    'source': file_path,
                    'type': 'text_file',
                    'filename': os.path.basename(file_path)
                })
                ids.append(f"file_{i}_{os.path.basename(file_path)}")
                
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                continue
        
        if documents:
            self.retriever.add_documents(documents, metadatas, ids)
        
        return {
            'ingested_count': len(documents),
            'total_documents': self.retriever.get_collection_info()['count']
        }
    
    def ingest_json_data(self, json_file: str) -> Dict[str, Any]:
        """Ingest structured JSON data"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            documents = []
            metadatas = []
            ids = []
            
            if isinstance(data, list):
                for i, item in enumerate(data):
                    documents.append(json.dumps(item, indent=2))
                    metadatas.append({
                        'source': json_file,
                        'type': 'json_item',
                        'index': i
                    })
                    ids.append(f"json_{i}_{os.path.basename(json_file)}")
            else:
                documents.append(json.dumps(data, indent=2))
                metadatas.append({
                    'source': json_file,
                    'type': 'json_file'
                })
                ids.append(f"json_{os.path.basename(json_file)}")
            
            self.retriever.add_documents(documents, metadatas, ids)
            
            return {
                'ingested_count': len(documents),
                'total_documents': self.retriever.get_collection_info()['count']
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def ingest_sample_data(self) -> Dict[str, Any]:
        """Ingest sample data for testing"""
        sample_docs = [
            "GRA (Generative Retrieval-Augmented) systems combine the power of large language models with external knowledge retrieval.",
            "RAG systems work by first retrieving relevant documents from a knowledge base, then using those documents as context for generation.",
            "Simulation scenarios help test and validate AI system behavior under different conditions and constraints.",
            "Prompt engineering is crucial for getting optimal performance from language models in specific domains."
        ]
        
        metadatas = [
            {'source': 'sample', 'topic': 'gra_overview'},
            {'source': 'sample', 'topic': 'rag_explanation'},
            {'source': 'sample', 'topic': 'simulation'},
            {'source': 'sample', 'topic': 'prompt_engineering'}
        ]
        
        ids = [f"sample_{i}" for i in range(len(sample_docs))]
        
        self.retriever.add_documents(sample_docs, metadatas, ids)
        
        return {
            'ingested_count': len(sample_docs),
            'total_documents': self.retriever.get_collection_info()['count']
        }