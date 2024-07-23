"""Person Service Module"""
from fastapi import HTTPException

from src.domain.repository.commands.person import PersonCommand
from src.domain.repository.queries.person import PersonQuery


class PersonService:
    """Person Class"""
    def __init__(self):
        self.person_query = PersonQuery
        self.person_command = PersonCommand

    def list_all(self, db_session):
        """
        List all person from database
        :param db_session:
        :return list[Person]:
        """
        return self.person_query(db_session).list_all()

    def get_by_id(self, id: int, db_session):
        """
        Get a person
        :param id:
        :param db_session:
        :return Person:
        """
        return self.person_query(db_session).get_by_id(id)

    def get_by_email(self, email: str, db_session):
        """
        Get a person
        :param email:
        :param db_session:
        :return Person:
        """
        person = self.person_query(db_session).get_by_email(email)
        if not person:
            raise HTTPException(status_code=404, detail=f"La persona con email '{email}' a consultar no existe")
        return person

    def create(self, data, db_session):
        """
        Create a person
        :param data:
        :param db_session:
        :return Person:
        """
        return self.person_command(db_session).create(data)

    def update(self, person, data, db_session):
        """
        Update a person
        :param person:
        :param data:
        :param db_session:
        :return Person:
        """
        return self.person_command(db_session).update(person, data)

    def delete(self, id: int, db_session):
        """
        Delete a person
        :param id:
        :param db_session:
        :return bool:
        """
        if person := self.person_query(db_session).get_by_id(id):
            return self.person_command(db_session).delete(person)
        raise HTTPException(status_code=404, detail="la persona no exite")
