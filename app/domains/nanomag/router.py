# app/api/v1/nanomag/router.py
from fastapi import APIRouter

from .endpoints import get_all_nanomag_data
from .endpoints import get_nanomag_column_stats
from .endpoints import get_nanomag_row_stats
from .endpoints import get_nanomag_top_categories
from app.domains.nanomag.endpoints import get_nanomag_ml_data

# Импортируем наш эндпоинт из соседнего файла

router = APIRouter()

# Регистрация эндпоинта для скачивания всех данных
router.add_api_route(
    "/data/all",
    get_all_nanomag_data,
    methods=["GET"],
    summary="Скачать все данные Nanomag",
    description="Скачивает все записи из витрины nanomag в формате JSON или CSV.",
)
router.add_api_route(
    "/analytics/column-stats",
    get_nanomag_column_stats,
    methods=["GET"],
    summary="Скачать статистику по колонкам (Nanomag)",
)
router.add_api_route(
    "/analytics/row-stats",
    get_nanomag_row_stats,
    methods=["GET"],
    summary="Скачать статистику по строкам (Nanomag)",
)
router.add_api_route(
    "/analytics/top-categories",
    get_nanomag_top_categories,
    methods=["GET"],
    summary="Скачать топовые категории (Nanomag)",
)


router.add_api_route(
    "/data/ml",
    get_nanomag_ml_data,
    methods=["GET"],
    summary="Скачать данные для ML (Nanomag)",
    description="Скачивает все записи из ML-витрины nanomag.",
)
