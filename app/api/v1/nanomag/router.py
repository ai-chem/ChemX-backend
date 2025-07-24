# app/api/v1/nanomag/router.py

from fastapi import APIRouter
# Импортируем наш эндпоинт из соседнего файла
from .endpoints import get_all_nanomag_data

router = APIRouter()

# Регистрация эндпоинта для скачивания всех данных
router.add_api_route(
    "/data/all",
    get_all_nanomag_data,
    methods=["GET"],
    summary="Скачать все данные Nanomag",
    description="Скачивает все записи из витрины nanomag в формате JSON или CSV."
)