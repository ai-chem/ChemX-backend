from fastapi import APIRouter
from .endpoints import get_all_nanozymes_data

router = APIRouter()

router.add_api_route(
    "/data/all",
    get_all_nanozymes_data,
    methods=["GET"],
    summary="Скачать все данные Nanozymes",
    description="Скачивает все записи из витрины nanozymes в формате JSON или CSV."
)