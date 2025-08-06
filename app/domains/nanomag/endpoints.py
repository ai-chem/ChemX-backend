# app/api/v1/nanomag/endpoints.py
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from fastapi import Response
from sqlalchemy.orm import Session

from .service import NanomagService
from app.database import get_db
from app.domains.common.utils import create_downloadable_response

# Используем нашу общую утилиту


async def get_all_nanomag_data(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"]),
    nanoparticle: str | None = Query(
        None, description="Фильтр по материалу наночастицы"
    ),
) -> Response:
    try:
        all_data = NanomagService.get_all_data(db, nanoparticle=nanoparticle)

        base_filename = "nanomag_all_data"
        # Можно добавить логику для "умного" имени файла
        if nanoparticle:
            base_filename = "nanomag_filtered_data"

        return create_downloadable_response(
            data=all_data, file_format=file_format, base_filename=base_filename
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_nanomag_column_stats(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"]),
) -> Response:
    try:
        data = NanomagService.get_column_stats(db)
        return create_downloadable_response(data, file_format, "nanomag_column_stats")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_nanomag_row_stats(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"]),
) -> Response:
    try:
        data = NanomagService.get_row_stats(db)
        return create_downloadable_response(data, file_format, "nanomag_row_stats")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_nanomag_top_categories(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"]),
) -> Response:
    try:
        data = NanomagService.get_top_categories(db)
        return create_downloadable_response(data, file_format, "nanomag_top_categories")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
