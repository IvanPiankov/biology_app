from typing import List, Union, Dict

from fastapi import APIRouter, Depends, Query, HTTPException, status
from core.repositories.patients import PatientsRepository
from core.schemas.patient import Patient
from ..api import get_user_repsitory

router_signatures = APIRouter()


@router_signatures.get("/", status_code=status.HTTP_200_OK, description="Return signatures by patient_id")
async def get_signatures_by_patient_id(
        patient_id: str,
        signature_names: Union[List[str], None] = Query(default=None),
        patients: PatientsRepository = Depends(get_user_repsitory)
):
    response = await patients.get_signatures_values_by_patient_id_and_signatures_names(patient_id, signature_names)
    if not response:
        raise HTTPException(status_code=400,
                            detail=f"Patient with patient id - '{patient_id}'"
                                   f" found in DataBase")
    return response


@router_signatures.put("/", response_model=Patient,
                       status_code=status.HTTP_200_OK,
                       description="Update signatures by patient_id"
                       )
async def update_signatures(
        patient_id: str,
        signature_value: Dict[str, int],
        patients: PatientsRepository = Depends(get_user_repsitory)):
    response = await patients.update_signature_patient(patient_id=patient_id, signature_value=signature_value)
    if not isinstance(response, Patient) and isinstance(response, str):
        raise HTTPException(status_code=400, detail=response)
    return response
