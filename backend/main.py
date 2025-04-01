from fastapi import FastAPI
from database import engine
import models
from router import router

models.base.metadata.vreate_all(bind=engine)

app = FastAPI()
app.include_router(router)