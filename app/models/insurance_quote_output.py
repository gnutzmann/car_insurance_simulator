from pydantic import BaseModel
from app.models.car import Car


class InsuranceQuoteOutput(BaseModel):
    car: Car
    applied_rate: float
    policy_limit: float
    calculated_premium: float
    deductible_value: float
