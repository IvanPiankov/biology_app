from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status

from core.repositories.patients import PatientsRepository
from core.schemas.patient import Patient
from ..api import get_user_repsitory

router_signature = APIRouter()


@router_signature.get("/",
                      status_code=status.HTTP_200_OK,
                      description="Return signature by patient_id")
async def get_signature_by_patient_id(
        patient_id: str,
        signature_name: str,
        patients: PatientsRepository = Depends(get_user_repsitory)):
    response = await patients.get_signature_value_by_patient_id_and_signature_name(patient_id, signature_name)
    if not response:
        raise HTTPException(status_code=400,
                            detail=f"Please check signature name or patient_id")
    return response


@router_signature.put("/", response_model=Patient,
                      status_code=status.HTTP_200_OK,
                      description="Update signature by patient_id")
async def update_signature(
        patient_id: str,
        signature_value:  Dict[str, int],
        patients: PatientsRepository = Depends(get_user_repsitory)):
    response = await patients.update_signature_patient(patient_id=patient_id, signature_value=signature_value)
    if not isinstance(response, Patient) and isinstance(response, str):
        raise HTTPException(status_code=400, detail=response)
    return response
