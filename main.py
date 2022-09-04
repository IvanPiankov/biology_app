import uvicorn
from fastapi import FastAPI
from core.models.base import database
import biology_app.endpoints.patient as patient
import biology_app.endpoints.patients as patients
import biology_app.endpoints.signature as signature
import biology_app.endpoints.signatures as signatures


biology_app = FastAPI()


biology_app.include_router(patient.router_patient, tags=["patient"], prefix="/patient")
biology_app.include_router(patients.router_patients, tags=["patients"], prefix="/patients")
biology_app.include_router(signature.router_signature, tags=["signature"], prefix="/signature")
biology_app.include_router(signatures.router_signatures, tags=["signatures"], prefix='/signatures')


@biology_app.on_event("startup")
async def startup():
    await database.connect()


@biology_app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# if __name__ == '__main__':
#     uvicorn.run("main:biology_app", port=8000, host="0.0.0.0", reload=True)
