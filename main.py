from fastapi import FastAPI
from predictor import predict
from schemas import CropData, PredictedData

app = FastAPI()

@app.post('/predict')
def predict_yield(data: CropData) -> PredictedData:
    predicted_yield, total_production, total_quintals = predict(crop=data.crop,
    season=data.season,
    state=data.state,
    year=data.year,
    rainfall=data.rainfall,
    area=data.area,
    fertilizer=data.fertilizer,
    pesticide=data.pesticide
    )

    return PredictedData(
        predicted_yield = predicted_yield,
        total_production = total_production,
        total_quintals = total_quintals
    )