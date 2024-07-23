"""Person Model Module"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.config.database import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    vehicles = relationship("Vehicle", back_populates="person", cascade='all, delete')
