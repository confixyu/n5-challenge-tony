"""Officer Model Module"""
from sqlalchemy import Column, Integer, String
from src.config.database import Base


class Officer(Base):
    __tablename__ = "officers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(Integer, unique=True)
    token = Column(String)
