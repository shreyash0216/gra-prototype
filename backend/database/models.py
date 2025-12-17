from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, JSON, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./climate_adaptation.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class AdaptationPlan(Base):
    __tablename__ = "adaptation_plans"
    
    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(String, unique=True, index=True)
    location = Column(String, index=True)
    farm_size = Column(Float)
    soil_type = Column(String)
    water_source = Column(String)
    current_crops = Column(JSON)
    budget = Column(Float)
    experience_level = Column(String)
    
    # Climate analysis results
    climate_risks = Column(JSON)
    adaptation_goals = Column(JSON)
    
    # Recommendations
    recommended_crops = Column(JSON)
    market_analysis = Column(JSON)
    government_schemes = Column(JSON)
    farm_layout_svg = Column(Text)
    
    # Implementation details
    implementation_timeline = Column(JSON)
    estimated_costs = Column(JSON)
    expected_benefits = Column(JSON)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()