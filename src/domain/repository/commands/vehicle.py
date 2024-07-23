"""Vehicle Command Module"""
from src.domain.model.vehicle import Vehicle


class VehicleCommand:
    """Vehicle Command class"""

    def __init__(self, db_session):
        self.db_session = db_session

    def create(self, data):
        """
        Method to create a vehicle
        :param data:
        :return Vehicle:
        """
        vehicle = Vehicle(
            plate=data.get("plate"),
            label=data.get("label"),
            color=data.get("color"),
            person_id=data.get("person_id")
        )
        self.db_session.add(vehicle)
        self.db_session.commit()
        self.db_session.refresh(vehicle)
        return vehicle

    def update(self, vehicle, data):
        """
        Method to update a vehicle
        :param vehicle:
        :param data:
        :return Vehicle:
        """
        vehicle.plate = data.plate
        vehicle.label = data.label
        vehicle.color = data.color
        vehicle.person_id = data.person_id
        self.db_session.commit()
        self.db_session.refresh(vehicle)
        return vehicle

    def delete(self, vehicle):
        """
        Method to delete a vehicle
        :param vehicle:
        :return bool:
        """
        self.db_session.delete(vehicle)
        self.db_session.commit()
        return True
