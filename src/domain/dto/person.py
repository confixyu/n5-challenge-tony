"""Person DTO Module"""
from pydantic import BaseModel
from typing import Optional

from src.domain.dto.vehicle import VehicleOutput


class Person(BaseModel):
    name: str
    email: str


class PersonOutput(BaseModel):
    name: str
    email: str
    vehicles: Optional[list[VehicleOutput]]
