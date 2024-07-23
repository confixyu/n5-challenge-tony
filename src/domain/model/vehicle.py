"""Vehicle Model Module"""
from datetime import datetime
from src.config.database import Base
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    plate = Column(String, unique=True)
    label = Column(String)
    color = Column(String)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship("Person", back_populates="vehicles")
    tickets = relationship("Ticket", back_populates="vehicle")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    plate = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    comment = Column(String)
    officer_id = Column(Integer, ForeignKey('officers.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))

    officer = relationship("Officer")
    vehicle = relationship("Vehicle", back_populates="tickets")
