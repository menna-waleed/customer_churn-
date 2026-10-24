from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import numpy as np

app= FastAPI(
    title="customer churn prediction API"
)
with open ("model.pkl", 'rb') as file:
    model=pickle.load(file)

class CustomerData(BaseModel):
    age:float
    monthly_charges: float
    support_calls: float
    tenure_months: float
    satisfaction_score: float
    total_spend: float

@app.get("/")
def home():
        return{"message": "welcome to customer churn prediction API!"}
@app.post("/predict")
def predict_churn(data: CustomerData ):
        input_data = np.array([[
            data.age,
            data.monthly_charges,
            data.tenure_months,
            data.support_calls,
            data.satisfaction_score,
            data.total_spend
        ]])

        prediction = int(model.predict(input_data)[0])

        status ="will churn (1)" if prediction == 1 else "stay (0)"

        return {
             "prediction_result": prediction,
             "customer_status": status
  }