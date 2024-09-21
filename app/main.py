from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

from app.config import settings
from app.database import init_db
from app.models.cybersecurity import ThreatIntelligence
from app.services.osint_service import OSINTService
from app.services.analysis_service import AnalysisService

app = FastAPI(title=settings.APP_NAME)

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize database
@app.on_event("startup")
async def startup_event():
    init_db()

# Dependency
def get_osint_service():
    return OSINTService()

def get_analysis_service():
    return AnalysisService()

class ThreatIntelligenceCreate(BaseModel):
    name: str
    description: str
    source: str

@app.post("/threat_intelligence/", response_model=ThreatIntelligence)
def create_threat_intelligence(
    threat: ThreatIntelligenceCreate,
    osint_service: OSINTService = Depends(get_osint_service),
    analysis_service: AnalysisService = Depends(get_analysis_service)
):
    # Gather additional information using OSINT
    additional_info = osint_service.gather_info(threat.name)
    
    # Analyze the threat
    analysis = analysis_service.analyze_threat(threat.dict(), additional_info)
    
    # Create and return the threat intelligence
    return ThreatIntelligence(**analysis)

@app.get("/threat_intelligence/", response_model=List[ThreatIntelligence])
def get_all_threat_intelligence():
    # Retrieve all threat intelligence from the database
    # This is a placeholder and should be replaced with actual database query
    return []

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)