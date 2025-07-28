from fastapi import Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session
from typing import Optional
from app.domains.common.utils import create_downloadable_response
from database import get_db
from .service import SeltoxService

async def get_all_seltox_data(
        db: Session = Depends(get_db),
        file_format: str = Query("json", enum=["json", "csv"]),
        nanoparticle: Optional[str] = Query(None, description="Фильтр по материалу наночастицы")
) -> Response:
    try:
        data = SeltoxService.get_all_data(db, nanoparticle=nanoparticle)
        base_filename = "seltox_filtered_data" if nanoparticle else "seltox_all_data"
        return create_downloadable_response(data, file_format, base_filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Остальные эндпоинты для аналитики остаются без изменений
async def get_seltox_column_stats(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = SeltoxService.get_column_stats(db)
        return create_downloadable_response(data, file_format, "seltox_column_stats")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_seltox_row_stats(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = SeltoxService.get_row_stats(db)
        return create_downloadable_response(data, file_format, "seltox_row_stats")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_seltox_top_categories(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = SeltoxService.get_top_categories(db)
        return create_downloadable_response(data, file_format, "seltox_top_categories")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))