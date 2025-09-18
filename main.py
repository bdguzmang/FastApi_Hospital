from fastapi import FastAPI
from app.api.routes import health
from app.api.routes import hospitals
from app.api.routes import usuarios

app = FastAPI(title="Hospitales API")

app.include_router(health.router)
app.include_router(hospitals.router)
app.include_router(usuarios.router)
