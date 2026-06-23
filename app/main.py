from fastapi import FastAPI

from app.api.routes.health import (
    router as health_router
)

from app.api.routes.prediction import (
    router as prediction_router
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

app = FastAPI(
    title="Counterfeit Drug Detection API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False
)

app.include_router(
    health_router,
    prefix="/api"
)

app.include_router(
    prediction_router,
    prefix="/api"
)