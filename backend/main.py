from fastapi import FastAPI
from database import engine, Base
import models
from router import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)