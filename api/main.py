from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI(title="RFM Customer Segmentation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

scaler = joblib.load("model/scaler.pkl")
kmeans_model = joblib.load("model/kmeans_model.pkl")

cluster_mapping = {
    0: "VIP Sadıklar",
    1: "Riskli Kayıp Müşteriler",
    2: "Potansiyel VIP'ler"
}

class CustomerRFM(BaseModel):
    Recency: float
    Frequency: float
    Monetary: float

@app.get("/")
def home():
    return {"message": "RFM Segmentation API"}

@app.post("/predict")
def predict_segment(customer: CustomerRFM):
    df_new = pd.DataFrame([customer.dict()])
    scaled_new = scaler.transform(df_new)
    cluster_label = kmeans_model.predict(scaled_new)[0]
    segment = cluster_mapping.get(cluster_label, "Bilinmeyen")
    return {
        "Cluster": int(cluster_label),
        "Segment": segment
    }
