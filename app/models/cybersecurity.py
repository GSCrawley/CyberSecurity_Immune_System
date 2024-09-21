from pydantic import BaseModel
from typing import List

class ThreatIntelligence(BaseModel):
    name: str
    description: str
    source: str
    risk_level: str
    indicators: List[str]