from fastapi import Request, APIRouter, Depends, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from starlette.responses import HTMLResponse
from typing import Annotated
from pathlib import Path

from src.config.database import get_db
from src.infrastructure.services.officer import OfficerService
from src.infrastructure.services.person import PersonService
from src.infrastructure.services.vehicle import VehicleService
from src.domain.dto.officer import Officer
from src.domain.dto.person import Person
from src.domain.dto.vehicle import Vehicle


web_router = APIRouter()
CURRENT_DIRECTORY = Path(__file__).resolve().parent
TEMPLATE_DIRECTORY = CURRENT_DIRECTORY / "html"
templates = Jinja2Templates(directory=str(TEMPLATE_DIRECTORY))
officer_service = OfficerService()
person_service = PersonService()
vehicle_service = VehicleService()


@web_router.get("/admin", response_class=HTMLResponse)
async def officer_render(request: Request, db: Session = Depends(get_db)):
    officers = officer_service.list_all(db)
    return templates.TemplateResponse(
        request=request, name="officer.html", context={"officers": officers}
    )


@web_router.post("/admin/officers", response_class=HTMLResponse, include_in_schema=False)
async def create_officer_render(
        request: Request,
        name: Annotated[str, Form()],
        code: Annotated[int, Form()],
        db: Session = Depends(get_db)):
    error_message = None
    try:
        officer_service.create(Officer(name=name, code=code), db)
    except IntegrityError:
        db.rollback()
        error_message = "La identificación ha sido registrada!"
    except Exception as e:
        db.rollback()
        error_message = str(e)
    officers = officer_service.list_all(db)
    return templates.TemplateResponse(
        request=request, name="officer.html", context={"officers": officers, "error_message": error_message}
    )


@web_router.get("/admin/form/officers/{id}", response_class=HTMLResponse, include_in_schema=False)
async def update_officer_render(
        request: Request,
        id: int,
        db: Session = Depends(get_db)):
    officer = officer_service.get_by_id(id, db)
    return templates.TemplateResponse(
        request=request, name="form_officer.html", context={"officer": officer}
    )


@web_router.post("/admin/update/officers/{id}", response_class=HTMLResponse, include_in_schema=False)
async def update_officer_render(
        request: Request,
        id: int,
        name: Annotated[str, Form()],
        code: Annotated[int, Form()],
        db: Session = Depends(get_db)):
    error_message = None
    officer = officer_service.get_by_id(id, db)
    try:
        officer_service.update(officer, Officer(name=name, code=code), db)
    except IntegrityError:
        db.rollback()
        error_message = "La identificación ha sido registrada!"
    except Exception as e:
        db.rollback()
        error_message = str(e)
    officers = officer_service.list_all(db)
    return templates.TemplateResponse(
        request=request, name="officer.html", context={"officers": officers, "error_message": error_message}
    )



@web_router.get("/admin/officers/delete/{id}", response_class=HTMLResponse, include_in_schema=False)
async def delete_officer_render(
        request: Request,
        id: int,
        db: Session = Depends(get_db)):
    error_message = None
    try:
        officer_service.delete(id, db)
    except Exception as e:
        error_message = str(e)
    officers = officer_service.list_all(db)
    return templates.TemplateResponse(
        request=request, name="officer.html", context={"officers": officers, "error_message": error_message}
    )


@web_router.get("/admin/persons", response_class=HTMLResponse, include_in_schema=False)
async def person_render(request: Request, db: Session = Depends(get_db)):
    persons = person_service.list_all(db)
    return templates.TemplateResponse(
        request=request, name="person.html", context={"persons": persons}
    )


@web_router.post("/admin/persons", response_class=HTMLResponse, include_in_schema=False)
async def create_person_render(
        request: Request,
        name: Annotated[str, Form()],
        email: Annotated[str, Form()],
        db: Session = Depends(get_db)):
    error_message = None
    try:
        person_service.create(Person(name=name, email=email), db)
    except IntegrityError:
        db.rollback()
        error_message = "El correo ha sido registrado!"
    except Exception as e:
        db.rollback()
        error_message = str(e)
    persons = person_service.list_all(db)
    return templates.TemplateResponse(
        request=request, name="person.html", context={"persons": persons, "error_message": error_message}
    )


@web_router.get("/admin/form/persons/{id}", response_class=HTMLResponse, include_in_schema=False)
async def form_person_render(
        request: Request,
        id: int,
        db: Session = Depends(get_db)):
    person = person_service.get_by_id(id, db)
    return templates.TemplateResponse(
        request=request, name="form_person.html", context={"person": person}
    )


@web_router.post("/admin/update/persons/{id}", response_class=HTMLResponse, include_in_schema=False)
async def update_person_render(
        request: Request,
        id: int,
        name: Annotated[str, Form()],
        email: Annotated[str, Form()],
        db: Session = Depends(get_db)):
    error_message = None
    person = person_service.get_by_id(id, db)
    try:
        person_service.update(person, Person(name=name, email=email), db)
    except IntegrityError:
        db.rollback()
        error_message = "El correo ha sido registrado!"
    except Exception as e:
        db.rollback()
        error_message = str(e)
    persons = person_service.list_all(db)
    return templates.TemplateResponse(
        request=request, name="person.html", context={"persons": persons, "error_message": error_message}
    )


@web_router.get("/admin/persons/delete/{id}", response_class=HTMLResponse, include_in_schema=False)
async def delete_person_render(
        request: Request,
        id: int,
        db: Session = Depends(get_db)):
    error_message = None
    try:
        person_service.delete(id, db)
    except Exception as e:
        error_message = str(e)
    persons = person_service.list_all(db)
    return templates.TemplateResponse(
        request=request, name="person.html", context={"persons": persons, "error_message": error_message}
    )


@web_router.get("/admin/tickets", response_class=HTMLResponse, include_in_schema=False)
async def ticket_render(request: Request, db: Session = Depends(get_db)):
    tickets = vehicle_service.list_all_ticket(db)
    return templates.TemplateResponse(
        request=request, name="ticket.html", context={"tickets": tickets}
    )


@web_router.get("/admin/vehicles", response_class=HTMLResponse, include_in_schema=False)
async def vehicle_render(request: Request, db: Session = Depends(get_db)):
    vehicles = vehicle_service.list_all(db)
    persons = person_service.list_all(db)
    return templates.TemplateResponse(
        request=request, name="vehicle.html", context={"vehicles": vehicles, "persons": persons}
    )


@web_router.post("/admin/vehicles", response_class=HTMLResponse, include_in_schema=False)
async def create_vehicle_render(
        request: Request,
        plate: Annotated[str, Form()],
        label: Annotated[str, Form()],
        color: Annotated[str, Form()],
        person_id: Annotated[str, Form()],
        db: Session = Depends(get_db)):
    error_message = None
    try:
        vehicle_service.create(Vehicle(plate=plate, label=label, color=color, person_id=person_id), db)
    except IntegrityError:
        db.rollback()
        error_message = "La placa ya ha sido registrada"
    except Exception as e:
        db.rollback()
        error_message = str(e)
    persons = person_service.list_all(db)
    vehicles = vehicle_service.list_all(db)
    return templates.TemplateResponse(
        request=request,
        name="vehicle.html",
        context={"vehicles": vehicles, "error_message": error_message, "persons": persons}
    )


@web_router.get("/admin/form/vehicles/{id}", response_class=HTMLResponse, include_in_schema=False)
async def form_update_vehicle_render(
        request: Request,
        id: int,
        db: Session = Depends(get_db)):
    vehicle = vehicle_service.get_by_id(id, db)
    persons = person_service.list_all(db)
    return templates.TemplateResponse(
        request=request,
        name="form_vehicle.html",
        context={"vehicle": vehicle, "persons": persons}
    )


@web_router.post("/admin/update/vehicles/{id}", response_class=HTMLResponse, include_in_schema=False)
async def update_vehicle_render(
        request: Request,
        id: int,
        plate: Annotated[str, Form()],
        label: Annotated[str, Form()],
        color: Annotated[str, Form()],
        person_id: Annotated[int, Form()],
        db: Session = Depends(get_db)):
    error_message = None
    vehicle = vehicle_service.get_by_id(id, db)
    try:
        vehicle_service.update(vehicle, Vehicle(plate=plate, label=label, color=color, person_id=person_id), db)
    except IntegrityError:
        db.rollback()
        error_message = "La placa ya ha sido registrada"
    except Exception as e:
        db.rollback()
        error_message = str(e)
    persons = person_service.list_all(db)
    vehicles = vehicle_service.list_all(db)
    return templates.TemplateResponse(
        request=request,
        name="vehicle.html",
        context={"vehicles": vehicles, "error_message": error_message, "persons": persons}
    )


@web_router.get("/admin/vehicles/delete/{id}", response_class=HTMLResponse, include_in_schema=False)
async def delete_vehicle_render(
        request: Request,
        id: int,
        db: Session = Depends(get_db)):
    error_message = None
    try:
        vehicle_service.delete(id, db)
    except Exception as e:
        error_message = str(e)
    vehicles = vehicle_service.list_all(db)
    return templates.TemplateResponse(
        request=request, name="vehicle.html", context={"vehicles": vehicles, "error_message": error_message}
    )
