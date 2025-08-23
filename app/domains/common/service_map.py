# app/domains/common/service_map.py
# Импортируем все наши доменные сервисы
from app.domains.nanomaterials.cytotox.service import CytotoxService
from app.domains.nanomaterials.nanomag.service import NanomagService
from app.domains.nanomaterials.nanozymes.service import NanozymesService
from app.domains.nanomaterials.seltox.service import SeltoxService
from app.domains.nanomaterials.synergy.service import SynergyService
from app.domains.small_molecules.benzimidazoles.service import BenzimidazolesService
from app.domains.small_molecules.co_crystals.service import CoCrystalsService
from app.domains.small_molecules.complexes.service import ComplexesService
from app.domains.small_molecules.eyedrops.service import EyedropsService
from app.domains.small_molecules.oxazolidinones.service import OxazolidinonesService

# Создаем словарь, который связывает строковое имя домена с классом сервиса
SERVICE_MAP = {
    "cytotox": CytotoxService,
    "nanomag": NanomagService,
    "nanozymes": NanozymesService,
    "seltox": SeltoxService,
    "synergy": SynergyService,
    "benzimidazoles": BenzimidazolesService,
    "co_crystals": CoCrystalsService,
    "complexes": ComplexesService,
    "eyedrops": EyedropsService,
    "oxazolidinones": OxazolidinonesService,
}

# Словарь, который связывает тип данных с именем метода в сервисах
METHOD_MAP = {
    "all_data": "get_all_data",
    "ml_data": "get_ml_data",
    "column_stats": "get_column_stats",
    "row_stats": "get_row_stats",
    "top_categories": "get_top_categories",
}
