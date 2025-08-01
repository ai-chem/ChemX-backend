# app/api/v1/nanomag/router.py

from fastapi import APIRouter

# Импортируем наш эндпоинт из соседнего файла
from .endpoints import (
    get_all_nanomag_data,
    get_nanomag_column_stats,
    get_nanomag_row_stats,
    get_nanomag_top_categories,
)

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
