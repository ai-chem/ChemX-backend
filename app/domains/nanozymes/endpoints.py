from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from fastapi import Response
from sqlalchemy.orm import Session

from .service import NanozymesService
from app.database import get_db
from app.domains.common.utils import create_downloadable_response


async def get_all_nanozymes_data(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"]),
    nanoparticle: str | None = Query(
        None, description="Фильтр по материалу наночастицы"
    ),
) -> Response:
    try:
        data = NanozymesService.get_all_data(db, nanoparticle=nanoparticle)
        base_filename = (
            "nanozymes_filtered_data" if nanoparticle else "nanozymes_all_data"
        )
        return create_downloadable_response(data, file_format, base_filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Остальные эндпоинты для аналитики остаются без изменений
async def get_nanozymes_column_stats(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"]),
) -> Response:
    try:
        data = NanozymesService.get_column_stats(db)
        return create_downloadable_response(data, file_format, "nanozymes_column_stats")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_nanozymes_row_stats(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"]),
) -> Response:
    try:
        data = NanozymesService.get_row_stats(db)
        return create_downloadable_response(data, file_format, "nanozymes_row_stats")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_nanozymes_top_categories(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"]),
) -> Response:
    try:
        data = NanozymesService.get_top_categories(db)
        return create_downloadable_response(
            data, file_format, "nanozymes_top_categories"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_nanozymes_ml_data(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"]),
) -> Response:
    try:
        ml_data = NanozymesService.get_ml_data(db)
        return create_downloadable_response(
            data=ml_data, file_format=file_format, base_filename="nanozymes_ml_data"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
