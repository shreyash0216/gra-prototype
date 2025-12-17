from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add the parent directory to the path so we can import from backend
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.main import app

# This is the entry point for Vercel
# Vercel will automatically detect this as a serverless function