from pydantic import BaseModel


class Car(BaseModel):
    make: str
    model: str
    value: float
    year: int
