import csv
from sqlalchemy.orm import Session
from crud import create_faq
import schemas


def insert_faqs_from_csv(db: Session, file_path: str):
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            faq = schemas.CreateFaq(
                title=row['Article title - Question'],
                subtitle=row['Article subtitle - Complementary'],
                body=row['Article body - Answer'],
                language=row['Article language'],
                url=row['Article URL'],
                category=row['Category'],
                keywords=row['Keywords']
            )

            create_faq(db=db, faq=faq)
