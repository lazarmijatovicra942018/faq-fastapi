from sqlalchemy.orm import Session
import models
import schemas

def create_faq(db: Session, faq: schemas.CreateFaq):
    existing_faq = db.query(models.Faq).filter(
        models.Faq.title == faq.title,
        models.Faq.body == faq.body
    ).first()
    if existing_faq:
        return None
    db_faq = models.Faq(**faq.dict())
    db.add(db_faq)
    db.commit()
    db.refresh(db_faq)
    return db_faq

def get_faqs(db: Session, page: int = 1, limit: int = None):
    skip = (page-1)*limit
    return db.query(models.Faq).offset(skip).limit(limit).all()

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
