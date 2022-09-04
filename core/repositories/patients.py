from datetime import datetime
from typing import List, Optional, Union

from .base import BaseRepository
from ..schemas.patient import Patient, PatientIn
from ..models.patients import patients


class PatientsRepository(BaseRepository):

    async def get_patient_by_patient_id(self, patient_id: str) -> Optional[Patient]:
        query = patients.select().where(patients.c.Patient_id == patient_id)
        patient = await self.database.fetch_one(query=query)
        if patient is None:
            return None
        return Patient.parse_obj(patient)

    async def create_patient(self, patient: PatientIn) -> Union[Patient, None]:
        # check patient_id in db
        query = patients.select().where(patients.c.Patient_id == patient.Patient_id)
        record = await self.database.fetch_one(query=query)
        if record:
            return None
        patient = Patient(
            Patient_id=patient.Patient_id,
            MHCI=patient.MHCI,
            MHCII=patient.MHCII,
            Coactivation_molecules=patient.Coactivation_molecules,
            Effector_cells=patient.Effector_cells,
            T_cell_traffic=patient.T_cell_traffic,
            NK_cells=patient.NK_cells,
            T_cells=patient.T_cells,
            B_cells=patient.B_cells,
            M1_signatures=patient.M1_signatures,
            Th1_signature=patient.Th1_signature,
            Antitumor_cytokines=patient.Antitumor_cytokines,
            Checkpoint_inhibition=patient.Checkpoint_inhibition,
            Treg=patient.Treg,
            T_reg_traffic=patient.T_reg_traffic,
            Neutrophil_signature=patient.Neutrophil_signature,
            Granulocyte_traffic=patient.Granulocyte_traffic,
            MDSC=patient.MDSC,
            MDSC_traffic=patient.MDSC_traffic,
            Macrophages=patient.Macrophages,
            Macrophage_DC_traffic=patient.Macrophage_DC_traffic,
            Th2_signature=patient.Th2_signature,
            Protumor_cytokines=patient.Protumor_cytokines,
            CAF=patient.CAF,
            Matrix=patient.Matrix,
            Matrix_remodeling=patient.Matrix_remodeling,
            Angiogenesis=patient.Angiogenesis,
            Endothelium=patient.Endothelium,
            Proliferation_rate=patient.Proliferation_rate,
            EMT_signature=patient.EMT_signature,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        values = {**patient.dict()}
        values.pop("id", None)
        query = patients.insert().values(**values)
        patient.id = await self.database.execute(query)
        return patient

    async def update_patient(self, patient_id: str, patient: PatientIn) -> Union[Patient, None]:
        query = patients.select().where(patients.c.Patient_id == patient_id)
        old_record_patient = await self.database.fetch_one(query=query)
        if not old_record_patient:
            return None
        else:
            old_record_patient = Patient.parse_obj(old_record_patient)
        patient = Patient(
            id=old_record_patient.id,
            Patient_id=patient.Patient_id,
            MHCI=patient.MHCI,
            MHCII=patient.MHCII,
            Coactivation_molecules=patient.Coactivation_molecules,
            Effector_cells=patient.Effector_cells,
            T_cell_traffic=patient.T_cell_traffic,
            NK_cells=patient.NK_cells,
            T_cells=patient.T_cells,
            B_cells=patient.B_cells,
            M1_signatures=patient.M1_signatures,
            Th1_signature=patient.Th1_signature,
            Antitumor_cytokines=patient.Antitumor_cytokines,
            Checkpoint_inhibition=patient.Checkpoint_inhibition,
            Treg=patient.Treg,
            T_reg_traffic=patient.T_reg_traffic,
            Neutrophil_signature=patient.Neutrophil_signature,
            Granulocyte_traffic=patient.Granulocyte_traffic,
            MDSC=patient.MDSC,
            MDSC_traffic=patient.MDSC_traffic,
            Macrophages=patient.Macrophages,
            Macrophage_DC_traffic=patient.Macrophage_DC_traffic,
            Th2_signature=patient.Th2_signature,
            Protumor_cytokines=patient.Protumor_cytokines,
            CAF=patient.CAF,
            Matrix=patient.Matrix,
            Matrix_remodeling=patient.Matrix_remodeling,
            Angiogenesis=patient.Angiogenesis,
            Endothelium=patient.Endothelium,
            Proliferation_rate=patient.Proliferation_rate,
            EMT_signature=patient.EMT_signature,
            updated_at=datetime.utcnow(),
            created_at=old_record_patient.created_at
        )
        values = {**patient.dict()}
        values.pop("id", None)
        query = patients.update().where(patients.c.Patient_id == patient_id).values(**values)
        await self.database.execute(query)
        return patient

    async def delete_patient(self, patient_id: str):
        query = patients.select().where(patients.c.Patient_id == patient_id)
        patient = await self.database.fetch_one(query=query)
        if not patient:
            return None
        query = patients.delete().where(patients.c.Patient_id == patient_id)
        await self.database.execute(query=query)
        return True

    async def get_all(self, limit: int = 10, skip: int = 0) -> List[Patient]:
        query = patients.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def update_signature_patient(self, patient_id: str, signature_value: dict) -> Union[Patient, str]:
        query = patients.select().where(patients.c.Patient_id == patient_id)
        if not query:
            return f"No patient with patient id {patient_id} in DataBase"
        patient_signature = Patient.parse_obj(query).dict()
        for signature in signature_value:
            if signature not in patient_signature:
                return f"No signature - '{signature}' in DataBase"
        signature_value["created_at"] = await self.database.fetch_val(query=query, column="created_at")
        query = patients.update().where(patients.c.Patient_id == patient_id).values(**signature_value)
        await self.database.execute(query)
        query = patients.select().where(patients.c.Patient_id == patient_id)
        patient_query = await self.database.fetch_one(query=query)
        return Patient.parse_obj(patient_query)

    async def get_signature_value_by_patient_id_and_signature_name(self, patient_id: str,
                                                                   signature_name: str) -> Optional[dict]:
        query = patients.select().where(patients.c.Patient_id == patient_id)
        signature_value = await self.database.fetch_val(query=query, column=signature_name)
        if signature_value is None:
            return None
        return signature_value

    async def get_signatures_values_by_patient_id_and_signatures_names(self, patient_id: str,
                                                                       signatures_names: List[str]) -> Optional[dict]:
        query = patients.select().where(patients.c.Patient_id == patient_id)
        patient_query = await self.database.fetch_one(query=query)
        if patient_query is None:
            return None
        patient = Patient.parse_obj(patient_query)
        patient.dict()
        return {sign: value for sign, value in patient.dict().items() if sign in signatures_names}
