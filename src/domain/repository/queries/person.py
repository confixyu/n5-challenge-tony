"""Person Query Module"""
from src.domain.model.person import Person


class PersonQuery:
    """Person Query class"""

    def __init__(self, db_session):
        self.db_session = db_session

    def list_all(self):
        """
        Method to list all Persons
        :return list[Person]:
        """
        return self.db_session.query(Person).all()

    def get_by_id(self, id: int):
        """
        Method to get a person
        :param id:
        :return Person:
        """
        return self.db_session.query(Person).filter(Person.id == id).first()

    def get_by_email(self, email: str):
        """
            Method to get a person
            :param id:
            :return Person:
        """
        return self.db_session.query(Person).filter(Person.email == email).first()
