"""Officer Route Module"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Union

from src.infrastructure.services.person import PersonService
from src.config.database import get_db
from src.domain.dto.person import PersonOutput


person_router = APIRouter(tags=["Vehicle"])
person_service = PersonService()


@person_router.get("/generar_informe/{person_email}")
def generar_informe(person_email: str, db: Session = Depends(get_db)) -> Union[PersonOutput, None]:
    """
    En este endpoint se lista todos los vehiculos con infracciones en caso de que
    lo tenga que le pertenece a la persona consultada por medio del email.
    """
    return person_service.get_by_email(person_email, db)
