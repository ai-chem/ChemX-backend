from fastapi import APIRouter
from .endpoints import get_all_synergy_data

router = APIRouter()

router.add_api_route(
    "/data/all",
    get_all_synergy_data,
    methods=["GET"],
    summary="Скачать все данные Synergy",
    description="Скачивает все записи из витрины synergy в формате JSON или CSV."
)