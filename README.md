# Car Insurance Simulator

This is a car insurance simulator developed with FastAPI. It calculates insurance quotes based on provided input data.

## Requirements

- Python 3.12
- Docker
- Docker Compose

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/gnutzmann/car_insurance_simulator.git
   cd car_insurance_simulator
   ```

2. Create and activate a virtual environment:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a [.env](http://_vscodecontentref_/1) file with the necessary environment variables:

   ```env
    AGE_RATE_INCREMENT = 0.005
    BROKER_FEE = 50.0
    DEDUCTIBLE_PERCENTAGE = 0.1
    VALUE_RATE_INCREMENT = 0.005
    COVERAGE_PERCENTAGE = 1.0
   ```

## Usage

### Run Locally

1. Run the application:

   ```sh
   python3 app/main.py
   ```

2. Access the application at [http://localhost:5000](http://localhost:5000).

### Run with Docker

1. Build and start the containers:

   ```sh
   docker-compose up --build
   ```

2. Access the application at [http://localhost:5000](http://localhost:5000).

## Endpoints

### Calculate Insurance Quote

- **URL:** `/insurance/quote`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "car": {
      "make": "Toyota",
      "model": "Corolla",
      "year": 2015,
      "value": 100000
    },
    "deductible_percentage": 0.1,
    "broker_fee": 50.0
  }
  ```

- **Response Body:**

  ```json
  {
    "car": {
      "make": "Toyota",
      "model": "Corolla",
      "value": 100000.0,
      "year": 2015
    },
    "applied_rate": 0.1,
    "policy_limit": 90000.0,
    "calculated_premium": 9050.0,
    "deductible_value": 10000.0
  }
  ```

## Postman Collection

A Postman collection for testing the API is available in the `docs` folder.

# Project Structure

- `app/main.py`: Application entry point.
- `app/services/insurance_calculation_service.py`: Premium calculation service.
- `app/models/insurance_quote_input.py`: Input model for insurance quote.
- `app/models/insurance_quote_output.py`: Output model for insurance quote.
- `app/base/config.py`: Application settings.
