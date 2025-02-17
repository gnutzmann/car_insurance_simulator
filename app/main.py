from fastapi import FastAPI, HTTPException
from app.services.insurance_calculation_service import PremiumCalculationService
from app.models.insurance_quote_input import InsuranceQuoteInput
from app.models.insurance_quote_output import InsuranceQuoteOutput
import uvicorn

app = FastAPI()


@app.post("/insurance/quote", response_model=InsuranceQuoteOutput)
async def calculate_insurance_quote(input_data: InsuranceQuoteInput):
    try:
        premium_service = PremiumCalculationService()
        output_data = premium_service.calculate_premium(input_data)
        return output_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
