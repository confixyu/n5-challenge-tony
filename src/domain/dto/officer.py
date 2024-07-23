"""Officer DTO Module"""
from pydantic import BaseModel


class Officer(BaseModel):
    name: str
    code: int
