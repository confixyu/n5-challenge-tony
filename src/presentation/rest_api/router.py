"""Routers Module"""

from fastapi import APIRouter
from src.presentation.rest_api.vehicle import vehicle_router
from src.presentation.rest_api.person import person_router

api_router = APIRouter()
api_router.include_router(vehicle_router)
api_router.include_router(person_router)
