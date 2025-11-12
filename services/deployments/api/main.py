from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "mlops-api"}

@app.get("/predict")
def predict():
    return {"prediction": 0.85}