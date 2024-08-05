from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas
from fastapi import APIRouter
from database import get_db
import crud

router = APIRouter(
    prefix='/faqs',
    tags=['Faqs']
)


@router.get('/get', response_model=List[schemas.CreateFaq])
def get_faqs(db: Session = Depends(get_db)):
    faqs = crud.get_faqs(db=db)
    return  faqs




@router.post('/post', status_code=status.HTTP_201_CREATED, response_model=schemas.CreateFaq)
def post_faq(faq:schemas.CreateFaq, db:Session = Depends(get_db)):

    new_faq = crud.create_faq(db=db, faq=faq)
    if new_faq is None:
        raise HTTPException(status_code=400, detail="FAQ already exists")
    return new_faq


@router.get('/get/{id}', response_model=schemas.CreateFaq, status_code=status.HTTP_200_OK)
def get_one_faq(id:int ,db:Session = Depends(get_db)):

    idv_faq = crud.get_faq(db=db, faq_id=id)

    if idv_faq is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The id: {id} you requested for does not exist")
    return idv_faq



@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_faq(id:int, db:Session = Depends(get_db)):

    deleted_faq = crud.delete_faq(db=db, faq_id=id)

    if deleted_faq is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    




@router.put('/put/{id}', response_model=schemas.CreateFaq)
def update_faq(update_faq:schemas.CreateFaq, id:int, db:Session = Depends(get_db)):
    
    db_faq = crud.update_faq(db=db, faq_id=id, faq=update_faq)
    
    if db_faq is None:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return db_faq



