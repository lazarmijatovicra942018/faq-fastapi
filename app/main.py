from fastapi import FastAPI
from database import engine
from api import faqs
from csv_parser import insert_faqs_from_csv
from database import get_db
import models


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(faqs.router)


# Path to your CSV file
CSV_FILE_PATH = "data/faq_knowledge_base .csv"


@app.on_event("startup")
def startup_event():
    db_gen = get_db()
    db = next(db_gen)
    try:
        insert_faqs_from_csv(db, CSV_FILE_PATH)
    finally:
        db.close()
