"""Officer Command Module"""
from src.domain.model.officer import Officer


class OfficerCommand:
    """Officer Command class"""

    def __init__(self, db_session):
        self.db_session = db_session

    def create(self, data):
        """
        Method to create an officer
        :param data:
        :return Officer:
        """
        officer = Officer(**data)
        self.db_session.add(officer)
        self.db_session.commit()
        self.db_session.refresh(officer)
        return officer

    def update(self, officer, data):
        """
        Method to update an officer
        :param officer:
        :param data:
        :return Officer:
        """
        officer.name = data.name
        officer.code = data.code
        self.db_session.commit()
        self.db_session.refresh(officer)
        return officer

    def delete(self, officer):
        """
        Method to delete an officer
        :param officer:
        :return bool:
        """
        self.db_session.delete(officer)
        self.db_session.commit()
        return True
