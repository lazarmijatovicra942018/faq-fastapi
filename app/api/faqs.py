from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas
from fastapi import APIRouter
from database import get_db


router = APIRouter(
    prefix='/faqs',
    tags=['Faqs']
)


@router.get('/get')
def get_faqs(db: Session = Depends(get_db)):
    faq = db.query(models.Faq).all()
    return  faq



@router.post('/post', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreateFaq])
def post_faq(faq_faq:schemas.CreateFaq, db:Session = Depends(get_db)):

    new_faq = models.Faq(**faq_faq.dict())
    db.add(new_faq)
    db.commit()
    db.refresh(new_faq)

    return [new_faq]

@router.get('/get/{id}', response_model=schemas.CreateFaq, status_code=status.HTTP_200_OK)
def get_one_faq(id:int ,db:Session = Depends(get_db)):

    idv_faq = db.query(models.Faq).filter(models.Faq.id == id).first()

    if idv_faq is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The id: {id} you requested for does not exist")
    return idv_faq



@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_faq(id:int, db:Session = Depends(get_db)):

    deleted_faq = db.query(models.Faq).filter(models.Faq.id == id)

    if deleted_faq.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    deleted_faq.delete(synchronize_session=False)
    db.commit()



@router.put('/put/{id}', response_model=schemas.CreateFaq)
def update_faq(update_faq:schemas.FaqBase, id:int, db:Session = Depends(get_db)):

    updated_faq =  db.query(models.Faq).filter(models.Faq.id == id)

    if updated_faq.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    updated_faq.update(update_faq.dict(), synchronize_session=False)
    db.commit()
    
    return  updated_faq.first()




