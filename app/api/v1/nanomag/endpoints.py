# app/api/v1/nanomag/endpoints.py

from fastapi import Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session

# Используем нашу общую утилиту
from app.api.v1.common.utils import create_downloadable_response
from app.database import get_db
# Импортируем сервис ИМЕННО ЭТОГО домена
from .service import NanomagService


async def get_all_nanomag_data(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"])
) -> Response:
    """
    Скачать ВСЕ данные из витрины nanomag в формате JSON или CSV.
    Используйте параметр ?format=csv для получения CSV файла.
    """
    try:
        # Вызываем метод из NanomagService
        all_data = NanomagService.get_all_data(db)

        # Делегируем создание ответа нашей утилите
        return create_downloadable_response(
            data=all_data,
            file_format=file_format,
            base_filename="nanomag_all_data" # Указываем корректное имя файла
        )

    except Exception as e:
        print(f"Произошла ошибка в домене Nanomag: {e}")
        raise HTTPException(status_code=500, detail=str(e))

async def get_nanomag_column_stats(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = NanomagService.get_column_stats(db)
        return create_downloadable_response(data, file_format, "nanomag_column_stats")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_nanomag_row_stats(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = NanomagService.get_row_stats(db)
        return create_downloadable_response(data, file_format, "nanomag_row_stats")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_nanomag_top_categories(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = NanomagService.get_top_categories(db)
        return create_downloadable_response(data, file_format, "nanomag_top_categories")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

