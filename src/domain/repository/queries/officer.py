"""Officer Query Module"""
from src.domain.model.officer import Officer


class OfficerQuery:
    """Officer Query class"""

    def __init__(self, db_session):
        self.db_session = db_session

    def list_all(self):
        """
        Method to list all officer
        :return list[Officer]:
        """
        return self.db_session.query(Officer).all()

    def get_by_id(self, id: int):
        """
        Method to get an officer
        :param id:
        :return Officer:
        """
        return self.db_session.query(Officer).filter(Officer.id == id).first()

    def get_by_code(self, code: int):
        """
            Method to get an officer
            :param code:
            :return Officer:
        """
        return self.db_session.query(Officer).filter(Officer.code == code).first()
