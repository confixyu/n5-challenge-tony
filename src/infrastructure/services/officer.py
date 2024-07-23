"""Officer Service Module"""
from fastapi import HTTPException

from src.domain.repository.commands.officer import OfficerCommand
from src.domain.repository.queries.officer import OfficerQuery
from src.infrastructure.authentication import encode_jwt


class OfficerService:
    """Officer Class"""
    def __init__(self):
        self.officer_query = OfficerQuery
        self.officer_command = OfficerCommand

    def list_all(self, db_session):
        """
        list all officers from database
        :param db_session:
        :return list[Officer]:
        """
        return self.officer_query(db_session).list_all()

    def get_by_id(self, id: int, db_session):
        """
        Get an Officer
        :param id:
        :param db_session:
        :return Officer:
        """
        return self.officer_query(db_session).get_by_id(id)

    def get_by_code(self, code: int, db_session):
        """
        Get an Officer
        :param code:
        :param db_session:
        :return Officer:
        """
        return self.officer_query(db_session).get_by_code(code)

    def create(self, data, db_session):
        """
        Create an officer
        :param data:
        :param db_session:
        :return Officer:
        """
        officer = data.dict()
        officer.update({"token": encode_jwt(data.code)})
        return self.officer_command(db_session).create(officer)

    def update(self, officer, data, db_session):
        """
        Update an officer
        :param officer:
        :param data:
        :param db_session:
        :return Officer:
        """
        return self.officer_command(db_session).update(officer, data)

    def delete(self, id: int, db_session):
        """
        Delete an officer
        :param id:
        :param db_session:
        :return:
        """
        if officer := self.officer_query(db_session).get_by_id(id):
            return self.officer_command(db_session).delete(officer)
        raise HTTPException(status_code=404, detail="El oficial no exite")
