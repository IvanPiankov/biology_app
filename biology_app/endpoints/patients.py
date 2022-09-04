from typing import List, Optional

from fastapi import APIRouter, Depends, status, HTTPException
from core.repositories.patients import PatientsRepository
from core.schemas.patient import Patient, PatientIn
from ..api import get_user_repsitory

router_patients = APIRouter()


@router_patients.get("/", response_model=List[Patient], status_code=status.HTTP_200_OK,
                     description="Return array with json patient object by uniq patient_id")
async def get_info_patients(
        limit: Optional[int] = None,
        skip: Optional[int] = None,
        patients: PatientsRepository = Depends(get_user_repsitory)
):
    return await patients.get_all(limit=limit, skip=skip)


@router_patients.post("/", response_model=List[Patient], status_code=status.HTTP_200_OK,
                      description="Create patient from array with json patient object by uniq patient_id")
async def create_patients(
        patient: List[PatientIn],
        patients: PatientsRepository = Depends(get_user_repsitory)
):
    list_of_patients = []
    added_in_db_parients = []
    for p_in in patient:
        new_p = await patients.create_patient(patient=p_in)
        if not new_p:
            raise HTTPException(status_code=400, detail=f"Patient with patient id - '{p_in.Patient_id}'"
                                                        f" found in DataBase, "
                                                        f"Patient with patient id {*added_in_db_parients,} added in "
                                                        f"DataBase")
        list_of_patients.append(new_p)
        added_in_db_parients.append(new_p.Patient_id)
    return list_of_patients
