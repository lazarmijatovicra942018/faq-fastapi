from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import VECTOR


Base = declarative_base()


class Faq(Base):
    __tablename__ = 'faqs'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    subtitle = Column(String)
    body = Column(Text, nullable=False)
    language = Column(String)
    url = Column(String)
    category = Column(String)
    keywords = Column(String)
    embedding = Column(VECTOR, nullable=True)
