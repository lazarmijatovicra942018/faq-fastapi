from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Faq(Base):
    __tablename__ = 'faqs'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True)
    subtitle = Column(String, index=True)
    body = Column(String)
    language = Column(String)
    url = Column(String)
    category = Column(String)
    keywords = Column(String)
