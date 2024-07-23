"""Ticket Query Module"""
from src.domain.model.vehicle import Ticket


class TicketQuery:
    """Ticket Query class"""

    def __init__(self, db_session):
        self.db_session = db_session

    def list_all(self):
        """
        Method to list all tickets
        :return list[Ticket]:
        """
        return self.db_session.query(Ticket).all()
