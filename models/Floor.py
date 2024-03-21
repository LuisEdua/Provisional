from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Floor(Base):
    __tablename__ = 'floors'

    uuid = Column(String(36), primary_key=True)
    level = Column(String(45))    
