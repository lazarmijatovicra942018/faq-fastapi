from pydantic import BaseModel, HttpUrl


class FaqBase(BaseModel):
    title: str
    subtitle: str
    body: str
    language: str
    url: str
    category: str
    keywords: str

    class Config:
        orm_mode = True



class CreateFaq(FaqBase):
    class Config:
        orm_mode = True