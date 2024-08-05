from fastapi import FastAPI
import models 
from database import engine
from api import faqs



models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(faqs.router)

