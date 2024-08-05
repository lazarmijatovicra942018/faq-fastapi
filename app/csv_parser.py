import pandas as pd
from sqlalchemy.orm import Session
from . import crud, schemas


def read_csv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def insert_faqs_from_csv(db: Session, file_path: str):
    data = read_csv(file_path)
    for _ , row in data.iterrows():
        faq = schemas.FAQCreate(
            question=row['question'],
            answer=row['answer'],
            category=row['category'],
            url=row['url'] if 'url' in row else None
        )
        crud.create_faq(db=db, faq=faq)
