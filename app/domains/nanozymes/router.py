from fastapi import APIRouter

from .endpoints import get_all_nanozymes_data
from .endpoints import get_nanozymes_column_stats
from .endpoints import get_nanozymes_row_stats
from .endpoints import get_nanozymes_top_categories
from app.domains.nanozymes.endpoints import get_nanozymes_ml_data

router = APIRouter()

router.add_api_route(
    "/data/all",
    get_all_nanozymes_data,
    methods=["GET"],
    summary="Скачать все данные Nanozymes",
    description="Скачивает все записи из витрины nanozymes в формате JSON или CSV.",
)

router.add_api_route(
    "/analytics/column-stats",
    get_nanozymes_column_stats,
    methods=["GET"],
    summary="Скачать статистику по колонкам (Nanozymes)",
)
router.add_api_route(
    "/analytics/row-stats",
    get_nanozymes_row_stats,
    methods=["GET"],
    summary="Скачать статистику по строкам (Nanozymes)",
)
router.add_api_route(
    "/analytics/top-categories",
    get_nanozymes_top_categories,
    methods=["GET"],
    summary="Скачать топовые категории (Nanozymes)",
)


router.add_api_route(
    "/data/ml",
    get_nanozymes_ml_data,
    methods=["GET"],
    summary="Скачать данные для ML (Nanozymes)",
    description="Скачивает все записи из ML-витрины nanozymes.",
)
