from pydantic import BaseModel


class InsurancePremium(BaseModel):
    base_premium: float
    deductible_percentage: float
    broker_fee: float
    final_premium: float
