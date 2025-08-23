from fastapi import APIRouter

from .endpoints import get_all_synergy_data
from .endpoints import get_synergy_column_stats
from .endpoints import get_synergy_row_stats
from .endpoints import get_synergy_top_categories
from app.domains.nanomaterials.synergy.endpoints import get_synergy_ml_data

router = APIRouter()

router.add_api_route(
    "/data/all",
    get_all_synergy_data,
    methods=["GET"],
    summary="Скачать все сырые данные Synergy",
)
router.add_api_route(
    "/analytics/column-stats",
    get_synergy_column_stats,
    methods=["GET"],
    summary="Скачать статистику по колонкам (Synergy)",
)
router.add_api_route(
    "/analytics/row-stats",
    get_synergy_row_stats,
    methods=["GET"],
    summary="Скачать статистику по строкам (Synergy)",
)
router.add_api_route(
    "/analytics/top-categories",
    get_synergy_top_categories,
    methods=["GET"],
    summary="Скачать топовые категории (Synergy)",
)

router.add_api_route(
    "/data/ml",
    get_synergy_ml_data,
    methods=["GET"],
    summary="Скачать данные для ML (Synergy)",
    description="Скачивает все записи из ML-витрины synergy.",
)
