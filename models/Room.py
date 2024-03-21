from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.Area import Area
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Room(Base):
    __tablename__ = 'rooms'
    uuid = Column(String(36), primary_key=True)
    number = Column(Integer, nullable=False)
    area_uuid = Column(String(36), ForeignKey('areas.uuid'), nullable=False)
    area = relationship(Area, backref=backref('habitaciones', uselist=True, cascade="all, delete"))
