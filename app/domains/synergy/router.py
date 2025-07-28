from fastapi import APIRouter
from .endpoints import (
    get_all_synergy_data,
    get_synergy_column_stats,
    get_synergy_row_stats,
    get_synergy_top_categories
)

router = APIRouter()

router.add_api_route("/data/all", get_all_synergy_data, methods=["GET"], summary="Скачать все сырые данные Synergy")
router.add_api_route("/analytics/column-stats", get_synergy_column_stats, methods=["GET"], summary="Скачать статистику по колонкам (Synergy)")
router.add_api_route("/analytics/row-stats", get_synergy_row_stats, methods=["GET"], summary="Скачать статистику по строкам (Synergy)")
router.add_api_route("/analytics/top-categories", get_synergy_top_categories, methods=["GET"], summary="Скачать топовые категории (Synergy)")