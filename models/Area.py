from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Area(Base):
    __tablename__ = 'areas'

    uuid = Column(String(36), primary_key=True)
    name = Column(String(255))
    floor_uuid = Column(String(36))
