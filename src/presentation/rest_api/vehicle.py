"""Vehicle Route Module"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.infrastructure.authentication import decode_jwt
from src.infrastructure.services.vehicle import VehicleService
from src.domain.dto.vehicle import Ticket, TicketOutput
from src.config.database import get_db


vehicle_router = APIRouter(tags=["Vehicle"])
vehicle_service = VehicleService()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_officer(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_jwt(token)
        code: int = payload.get("code")
        if code is None:
            raise HTTPException(status_code=403, detail="Invalid credentials")
        return code
    except Exception:
        raise HTTPException(status_code=403, detail="Invalid credentials")


@vehicle_router.post("/cargar_infraccion", status_code=201, response_model=TicketOutput)
def create_ticket(data: Ticket, code: int = Depends(get_current_officer), db: Session = Depends(get_db)):
    """
    En este endpoint se lista todas las infracciones creadas,
    el Auth Bearer Token se puede conseguir en el admin panel
    al crear un oficial de policia.

    Cada oficial de policia tiene su propio token que lo identifica.
    """
    return vehicle_service.create_ticket(code, data, db)

