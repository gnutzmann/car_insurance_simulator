from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AGE_RATE_INCREMENT: float = 0.005
    BROKER_FEE: float
    COVERAGE_PERCENTAGE: float
    DEDUCTIBLE_PERCENTAGE: float
    VALUE_RATE_INCREMENT: float = 0.005

    class Config:
        env_file = ".env"
