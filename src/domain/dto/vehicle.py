"""Vehicle DTO Module"""

from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Vehicle(BaseModel):
    plate: str
    label: str
    color: str
    person_id: int


class Ticket(BaseModel):
    plate: str
    comment: str


class VehicleOutput(BaseModel):
    plate: str
    label: str
    color: str
    tickets: Optional[list[Ticket]]





class TicketOutput(BaseModel):
    plate: str
    created_at: datetime
    comment: str
