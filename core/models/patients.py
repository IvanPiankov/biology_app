import sqlalchemy
from .base import metadata
import datetime


DEFAULT_VALUE = 0

patients = sqlalchemy.Table(
    "patients",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("Patient_id", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column("MHCI", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("MHCII", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Coactivation_molecules", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Effector_cells", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("T_cell_traffic", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("NK_cells", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("T_cells", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("B_cells", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("M1_signatures", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Th1_signature", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Antitumor_cytokines", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Checkpoint_inhibition", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Treg", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("T_reg_traffic", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Neutrophil_signature", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Granulocyte_traffic", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("MDSC", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("MDSC_traffic", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Macrophages", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Macrophage_DC_traffic", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Th2_signature", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Protumor_cytokines", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("CAF", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Matrix", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Matrix_remodeling", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Angiogenesis", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Endothelium", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("Proliferation_rate", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("EMT_signature", sqlalchemy.Float, default=DEFAULT_VALUE),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow)
)

