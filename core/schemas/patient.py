import datetime

from pydantic import BaseModel
from typing import Optional


class Patient(BaseModel):
    id: Optional[int]
    Patient_id: str
    MHCI: float
    MHCII: float
    Coactivation_molecules: float
    Effector_cells: float
    T_cell_traffic: float
    NK_cells: float
    T_cells: float
    B_cells: float
    M1_signatures: float
    Th1_signature: float
    Antitumor_cytokines: float
    Checkpoint_inhibition: float
    Treg: float
    T_reg_traffic: float
    Neutrophil_signature: float
    Granulocyte_traffic: float
    MDSC: float
    MDSC_traffic: float
    Macrophages: float
    Macrophage_DC_traffic: float
    Th2_signature: float
    Protumor_cytokines: float
    CAF: float
    Matrix: float
    Matrix_remodeling: float
    Angiogenesis: float
    Endothelium: float
    Proliferation_rate: float
    EMT_signature: float
    created_at: datetime.datetime
    updated_at: datetime.datetime


class PatientIn(BaseModel):
    Patient_id: str
    MHCI: float
    MHCII: float
    Coactivation_molecules: float
    Effector_cells: float
    T_cell_traffic: float
    NK_cells: float
    T_cells: float
    B_cells: float
    M1_signatures: float
    Th1_signature: float
    Antitumor_cytokines: float
    Checkpoint_inhibition: float
    Treg: float
    T_reg_traffic: float
    Neutrophil_signature: float
    Granulocyte_traffic: float
    MDSC: float
    MDSC_traffic: float
    Macrophages: float
    Macrophage_DC_traffic: float
    Th2_signature: float
    Protumor_cytokines: float
    CAF: float
    Matrix: float
    Matrix_remodeling: float
    Angiogenesis: float
    Endothelium: float
    Proliferation_rate: float
    EMT_signature: float
