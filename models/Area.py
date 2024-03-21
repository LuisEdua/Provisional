from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from models.Floor import Floor

Base = declarative_base()

class Area(Base):
    __tablename__ = 'areas'

    uuid = Column(String(36), primary_key=True)
    name = Column(String(255))
    floor_uuid = Column(String(36))

