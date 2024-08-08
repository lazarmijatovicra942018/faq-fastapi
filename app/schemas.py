from pydantic import BaseModel
from typing import Optional, List


class FaqBase(BaseModel):
    title: str
    subtitle: str
    body: str
    language: str
    url: str
    category: str
    keywords: str

    class Config:
        from_attributes = True


class CreateFaq(FaqBase):

    pass


class FaqResponse(FaqBase):
    id: int
    embedding: Optional[List[float]] = None

    class Config:
        from_attributes = True
