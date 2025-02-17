from pydantic import BaseModel
from app.models.car import Car


class InsuranceQuoteInput(BaseModel):
    car: Car
    deductible_percentage: float
    broker_fee: float
