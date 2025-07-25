from fastapi import APIRouter
from app.api.v1.cytotox.endpoints import (
    get_cytotox_data,
    get_all_cytotox_data,
    get_cytotox_column_stats,
    get_cytotox_row_stats,
    get_cytotox_top_categories
)

router = APIRouter()

# Регистрация эндпоинта
router.add_api_route(
    "/data",
    get_cytotox_data,
    methods=["GET"],
    response_model_exclude_none=True,
    summary="Получить данные цитотоксичности",
    description="Получает данные из витрины cytotox с пагинацией"
)


router.add_api_route(
    "/data/all",
    get_all_cytotox_data,
    methods=["GET"],
    response_model_exclude_none=True,
    summary="Получить ВСЕ данные цитотоксичности",
    description="Получает все записи из витрины cytotox. Внимание: может вызвать высокую нагрузку!"
)

# Маршрут для статистики по колонкам
router.add_api_route(
    "/analytics/column-stats",
    get_cytotox_column_stats,
    methods=["GET"],
    summary="Скачать статистику по колонкам (Cytotox)",
    description="Скачивает посчитанную статистику по колонкам для домена Cytotox."
)

# Маршрут для статистики по строкам
router.add_api_route(
    "/analytics/row-stats",
    get_cytotox_row_stats,
    methods=["GET"],
    summary="Скачать статистику по строкам (Cytotox)",
    description="Скачивает посчитанную статистику по строкам для домена Cytotox."
)

router.add_api_route(
    "/analytics/top-categories",
    get_cytotox_top_categories,
    methods=["GET"],
    summary="Скачать топовые категории (Cytotox)",
    description="Скачивает посчитанную статистику по топовым категориям для домена Cytotox."
)