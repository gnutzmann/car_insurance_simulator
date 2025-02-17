from app.models.car import Car
from app.base.config import Settings
from app.models.insurance_quote_output import InsuranceQuoteOutput
from app.models.insurance_quote_input import InsuranceQuoteInput

import datetime


class RateCalculationService:
    def __init__(self):
        self.config = Settings()

    def _calculate_age(self, year: int) -> int:
        current_year = datetime.datetime.now().year
        return current_year - year

    def calculate_base_rate(self, car: Car) -> float:
        age = self._calculate_age(car.year)
        age_rate = age * self.config.AGE_RATE_INCREMENT
        value_rate = (car.value / 10000) * self.config.VALUE_RATE_INCREMENT

        return age_rate + value_rate


class PremiumCalculationService:
    def __init__(self):
        self.config = Settings()
        self.rate_calculation_service = RateCalculationService()

    def calculate_premium(self, input_data: InsuranceQuoteInput
                          ) -> InsuranceQuoteOutput:
        car = input_data.car
        deductible_percentage = input_data.deductible_percentage
        broker_fee = input_data.broker_fee

        applied_rate = self.rate_calculation_service.calculate_base_rate(car)

        base_premium = car.value * applied_rate
        deductible_discount = base_premium * deductible_percentage
        calculated_premium = base_premium - deductible_discount + broker_fee

        base_policy_limit = car.value * self.config.COVERAGE_PERCENTAGE
        deductible_value = base_policy_limit * deductible_percentage
        policy_limit = base_policy_limit - deductible_value

        return InsuranceQuoteOutput(
            applied_rate=applied_rate,
            car=car,
            calculated_premium=calculated_premium,
            deductible_value=deductible_value,
            policy_limit=policy_limit
        )
