from core.repositories.patients import PatientsRepository
from core.models.base import database


def get_user_repsitory() -> PatientsRepository:
    return PatientsRepository(database)
