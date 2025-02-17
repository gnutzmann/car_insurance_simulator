from pydantic import BaseSettings


class Settings(BaseSettings):
    AGE_RATE_INCREMENT: float = 0.005
    BROKER_FEE: float
    DEDUCTIBLE_PERCENTAGE: float
    VALUE_RATE_INCREMENT: float = 0.005

    class Config:
        env_file = ".env"


settings = Settings()
