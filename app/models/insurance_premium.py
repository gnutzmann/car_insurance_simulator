from pydantic import BaseModel


class InsurancePremium(BaseModel):
    base_premium: float
    deductible_discount: float
    broker_fee: float
