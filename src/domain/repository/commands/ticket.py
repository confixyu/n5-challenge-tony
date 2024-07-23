"""Ticket Command Module"""
from src.domain.model.vehicle import Ticket


class TicketCommand:
    """Ticket Command class"""

    def __init__(self, db_session):
        self.db_session = db_session

    def create(self, data):
        """
        Method to create a ticket
        :param data:
        :return Ticket:
        """
        ticket = Ticket(
            plate=data.get("plate"),
            comment=data.get("comment"),
            officer_id=data.get("officer_id"),
            vehicle_id=data.get("vehicle_id"),
        )
        self.db_session.add(ticket)
        self.db_session.commit()
        self.db_session.refresh(ticket)
        return ticket
