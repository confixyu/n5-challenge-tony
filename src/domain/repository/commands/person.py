"""Person Command Module"""
from src.domain.model.person import Person


class PersonCommand:
    """Person Command class"""

    def __init__(self, db_session):
        self.db_session = db_session

    def create(self, data):
        """
        Method to create a person
        :param data:
        :return Person:
        """
        person = Person(**data.dict())
        self.db_session.add(person)
        self.db_session.commit()
        return person

    def update(self, person, data):
        """
        Method to update a person
        :param person:
        :param data:
        :return Person:
        """
        person.name = data.name
        person.email = data.email
        self.db_session.commit()
        self.db_session.refresh(person)
        return person

    def delete(self, person):
        """
        Method to delete a person
        :param person:
        :return bool:
        """
        self.db_session.delete(person)
        self.db_session.commit()
        return True
