"""
ORIGIN - Pydantic Request & Response Schemas
Provides strict type-checking and validation for all API interactions.
"""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field, field_validator


class AnalyzeRequest(BaseModel):
    state: str = Field(..., min_length=2, description="Indian State")
    district: str = Field(..., min_length=2, description="District name")
    block: Optional[str] = Field(default="", description="Block or Taluka")
    village: str = Field(..., min_length=2, description="Village or Gram Panchayat")
    capital: float = Field(..., gt=0, description="Available margin capital in INR (must be > 0)")
    business: str = Field(default="dairy", description="Business category key")
    language: Optional[str] = Field(default="en", description="Language: en, hi, or mr")

    @field_validator("capital")
    @classmethod
    def validate_capital_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Available margin capital must be strictly positive (greater than ₹0).")
        return v


class FinancialCalculateRequest(BaseModel):
    capital: float = Field(..., gt=0, description="Available margin capital in INR")
    business: Optional[str] = Field(default="dairy", description="Business category key")


class AdvisoryRequest(BaseModel):
    state: str
    district: str
    block: Optional[str] = ""
    village: str
    capital: float
    business: str = "dairy"
    language: Optional[str] = "en"


class LocationQuery(BaseModel):
    search: Optional[str] = None


class ReportRequest(BaseModel):
    analysis_payload: Dict[str, Any]

