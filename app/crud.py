from sqlalchemy.orm import Session
from embedding import generate_embedding
import models
import schemas


def create_faq(db: Session, faq: schemas.CreateFaq):
    existing_faq = db.query(models.Faq).filter(
        models.Faq.title == faq.title,
        models.Faq.body == faq.body
    ).first()
    if existing_faq:
        return None
    db_faq = models.Faq(**faq.dict(),
                        embedding=generate_embedding(sentence=faq.title))
    db.add(db_faq)
    db.commit()
    db.refresh(db_faq)
    return db_faq


def get_faqs(db: Session, page: int = 0, limit: int = 100, pagination=False):

    if not pagination:
        skip = 0
        limit = None
    else:
        if page < 0:
            page = 0
        if limit < 0:
            limit = 0
        skip = (page) * limit

    return db.query(models.Faq).offset(skip).limit(limit).all()


def get_faq(db: Session, faq_id: int):
    db_faq = db.query(models.Faq).filter(models.Faq.id == faq_id).first()
    if db_faq:
        faq_data = schemas.FaqResponse.from_orm(db_faq)
        return faq_data
    return None


def update_faq(db: Session, faq_id: int, faq: schemas.CreateFaq):
    db_faq = db.query(models.Faq).filter(models.Faq.id == faq_id).first()
    if db_faq is None:
        return None

    update_data = faq.dict(exclude_unset=True)
    for key, value in update_data.items():
        if value and value != "string":
            setattr(db_faq, key, value)

    db.commit()
    db.refresh(db_faq)
    return db_faq


def delete_faq(db: Session, faq_id: int):
    db_faq = db.query(models.Faq).filter(models.Faq.id == faq_id).first()
    if db_faq is None:
        return None
    db.delete(db_faq)
    db.commit()
    return db_faq
