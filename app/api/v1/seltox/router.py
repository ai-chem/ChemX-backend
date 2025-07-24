from fastapi import APIRouter
from .endpoints import get_all_seltox_data

router = APIRouter()

router.add_api_route(
    "/data/all",
    get_all_seltox_data,
    methods=["GET"],
    summary="Скачать все данные Seltox",
    description="Скачивает все записи из витрины seltox в формате JSON или CSV."
)