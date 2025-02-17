from pydantic import BaseModel
from app.models.car import Car


class InsuranceQuoteInput(BaseModel):
    broker_fee: float
    car: Car
    deductible_percentage: float
