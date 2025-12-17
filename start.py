#!/usr/bin/env python3
"""
Railway-compatible start script for GRA Prototype
"""

import os
import sys
import uvicorn

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from main import app

if __name__ == "__main__":
    # Railway provides PORT environment variable
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    print(f"🚀 Starting GRA Prototype on {host}:{port}")
    
    uvicorn.run(
        app, 
        host=host, 
        port=port,
        log_level="info"
    )