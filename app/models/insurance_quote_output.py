from pydantic import BaseModel
from app.models.car import Car


class InsuranceQuoteOutput(BaseModel):
    applied_rate: float
    calculated_premium: float
    car: Car
    deductible_value: float
    policy_limit: float
