# app/domains/universal/schemas.py
from enum import Enum


class Domain(str, Enum):
    cytotox = "cytotox"
    nanomag = "nanomag"
    nanozymes = "nanozymes"
    seltox = "seltox"
    synergy = "synergy"

    benzimidazoles = "benzimidazoles"
    co_crystals = "co_crystals"
    complexes = "complexes"
    eyedrops = "eyedrops"
    oxazolidinones = "oxazolidinones"


class DataType(str, Enum):
    all_data = "all_data"
    ml_data = "ml_data"
    column_stats = "column_stats"
    row_stats = "row_stats"
    top_categories = "top_categories"
