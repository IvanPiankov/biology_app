from fastapi import APIRouter, Depends, HTTPException, status
from core.repositories.patients import PatientsRepository
from core.schemas.patient import Patient, PatientIn
from ..api import get_user_repsitory

router_patient = APIRouter()


@router_patient.get("/", response_model=Patient, status_code=status.HTTP_200_OK,
                    description="Return json patient object by uniq patient_id")
async def read_patient(
        patient_id: str,
        patients: PatientsRepository = Depends(get_user_repsitory)
):
    response = await patients.get_patient_by_patient_id(patient_id)
    if not response:
        raise HTTPException(status_code=400, detail=f"Patient_id - '{patient_id}' not found in DataBase")
    return response


@router_patient.post("/", response_model=Patient, status_code=status.HTTP_201_CREATED,
                     description="Create patient in db")
async def create(
        patient: PatientIn,
        patients: PatientsRepository = Depends(get_user_repsitory)
):
    response = await patients.create_patient(patient=patient)
    if not response:
        raise HTTPException(status_code=400, detail=f"Patient with patient id - '{patient.Patient_id}'"
                                                    f" found in DataBase")
    return response


@router_patient.put("/", response_model=Patient, status_code=status.HTTP_200_OK,
                    description="Update patient in db")
async def update(
        patient_id: str,
        patient: PatientIn,
        patients: PatientsRepository = Depends(get_user_repsitory)):
    response = await patients.update_patient(patient_id=patient_id, patient=patient)
    if not response:
        raise HTTPException(status_code=400, detail=f"Patient with patient id - '{patient_id}'"
                                                    f" not found in DataBase")
    return response


@router_patient.delete("/", status_code=status.HTTP_200_OK,
                       description="Delete patient from db")
async def delete(
        patient_id: str,
        patients: PatientsRepository = Depends(get_user_repsitory)):
    response = await patients.delete_patient(patient_id=patient_id)
    if not response:
        raise HTTPException(status_code=400, detail=f"Patient with patient id - '{patient_id}'"
                                                    f" not found in DataBase")
    return HTTPException(status_code=200, detail=f"Patient with patient id - '{patient_id}'"
                                                    f" delete from DataBase")
