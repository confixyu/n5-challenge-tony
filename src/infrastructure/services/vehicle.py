"""Vehicle Service Module"""
from fastapi import HTTPException

from src.domain.repository.commands.ticket import TicketCommand
from src.domain.repository.commands.vehicle import VehicleCommand
from src.domain.repository.queries.officer import OfficerQuery
from src.domain.repository.queries.person import PersonQuery
from src.domain.repository.queries.ticket import TicketQuery
from src.domain.repository.queries.vehicle import VehicleQuery


class VehicleService:
    """Vehicle Class"""
    def __init__(self):
        self.officer_query = OfficerQuery
        self.person_query = PersonQuery
        self.ticket_query = TicketQuery
        self.vehicle_query = VehicleQuery
        self.vehicle_command = VehicleCommand
        self.ticket_command = TicketCommand

    def list_all(self, db_session):
        """
        List vehicle from database
        :param db_session:
        :return list[Vehicle]:
        """
        return self.vehicle_query(db_session).list_all()

    def get_by_id(self, id: int, db_session):
        """
        Get a vehicle
        :param id:
        :param db_session:
        :return Vehicle:
        """
        return self.vehicle_query(db_session).get_by_id(id)

    def get_by_plate(self, plate: str, db_session):
        """
        Get a Vehicle
        :param plate:
        :param db_session:
        :return Vehicle:
        """
        return self.vehicle_query(db_session).get_by_plate(plate)

    def create(self, data, db_session):
        """
        Create a vehicle
        :param data:
        :param db_session:
        :return Vehicle:
        """
        person = self.person_query(db_session).get_by_id(data.person_id)
        if not person:
            raise HTTPException(status_code=404, detail="Persona no existe")

        vehicle = {
            **data.dict(),
            "person_id": person.id
        }
        return self.vehicle_command(db_session).create(vehicle)

    def update(self, vehicle, data, db_session):
        """
        Update a Vehicle
        :param vehicle:
        :param data:
        :param db_session:
        :return Vehicle:
        """
        person = self.person_query(db_session).get_by_id(data.person_id)
        if not person:
            raise HTTPException(status_code=404, detail="Persona no existe")
        return self.vehicle_command(db_session).update(vehicle, data)

    def list_all_ticket(self, db_session):
        """
        List all ticket
        :param db_session:
        :return list[Ticket]:
        """
        return self.ticket_query(db_session).list_all()

    def create_ticket(self, code: int, data, db_session):
        """
        Create a ticket
        :param code:
        :param data:
        :param db_session:
        :return Ticket:
        """
        officer = self.officer_query(db_session).get_by_code(code)
        if not officer:
            raise HTTPException(status_code=404, detail="Codigo del oficial no existe")

        vehicle = self.vehicle_query(db_session).get_by_plate(data.plate)
        if not vehicle:
            raise HTTPException(status_code=404, detail="Placa del vehiculo no existe")

        ticket = {
            **data.dict(),
            "officer_id": officer.id,
            "vehicle_id": vehicle.id
        }
        return self.ticket_command(db_session).create(ticket)

    def delete(self, id: int, db_session):
        """
        Delete a vehicle
        :param id:
        :param db_session:
        :return bool:
        """
        if vehicle := self.vehicle_query(db_session).get_by_id(id):
            return self.vehicle_command(db_session).delete(vehicle)
        raise HTTPException(status_code=404, detail="el vehiculo no exite")
