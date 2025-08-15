# app/domains/common/service_map.py
# Импортируем все наши доменные сервисы
from app.domains.cytotox.service import CytotoxService
from app.domains.nanomag.service import NanomagService
from app.domains.nanozymes.service import NanozymesService
from app.domains.seltox.service import SeltoxService
from app.domains.synergy.service import SynergyService

# Создаем словарь, который связывает строковое имя домена с классом сервиса
SERVICE_MAP = {
    "cytotox": CytotoxService,
    "nanomag": NanomagService,
    "nanozymes": NanozymesService,
    "seltox": SeltoxService,
    "synergy": SynergyService,
}

# Словарь, который связывает тип данных с именем метода в сервисах
METHOD_MAP = {
    "all_data": "get_all_data",
    "ml_data": "get_ml_data",
    "column_stats": "get_column_stats",
    "row_stats": "get_row_stats",
    "top_categories": "get_top_categories",
}
