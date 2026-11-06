
from fastapi import FastAPI

app = FastAPI(title="Apex Operations API")


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/ready")
def readiness_check():
    return {"status": "ready"}
