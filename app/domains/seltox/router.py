from fastapi import APIRouter
from .endpoints import (
    get_all_seltox_data,
    get_seltox_column_stats,
    get_seltox_row_stats,
    get_seltox_top_categories,
)

router = APIRouter()

router.add_api_route(
    "/data/all",
    get_all_seltox_data,
    methods=["GET"],
    summary="Скачать все сырые данные Seltox",
)
router.add_api_route(
    "/analytics/column-stats",
    get_seltox_column_stats,
    methods=["GET"],
    summary="Скачать статистику по колонкам (Seltox)",
)
router.add_api_route(
    "/analytics/row-stats",
    get_seltox_row_stats,
    methods=["GET"],
    summary="Скачать статистику по строкам (Seltox)",
)
router.add_api_route(
    "/analytics/top-categories",
    get_seltox_top_categories,
    methods=["GET"],
    summary="Скачать топовые категории (Seltox)",
)
