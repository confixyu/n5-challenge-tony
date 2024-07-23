"""Vehicle Query Module"""
from src.domain.model.vehicle import Vehicle


class VehicleQuery:
    """Vehicle Query class"""

    def __init__(self, db_session):
        self.db_session = db_session

    def list_all(self):
        """
        Method to list all vehicles
        :return list[Vehicle]:
        """
        return self.db_session.query(Vehicle).all()

    def get_by_id(self, id: int):
        """
        Method to get a vehicle
        :param id:
        :return Vehicle:
        """
        return self.db_session.query(Vehicle).filter(Vehicle.id == id).first()

    def get_by_plate(self, plate: str):
        """
        Method to get a vehicle
        :param plate:
        :return Vehicle:
        """
        return self.db_session.query(Vehicle).filter(Vehicle.plate == plate).first()
