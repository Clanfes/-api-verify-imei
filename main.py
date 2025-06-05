from .routes import router
from fastapi import FastAPI

app = FastAPI(title="Private API Gateway")

app.include_router(router)
