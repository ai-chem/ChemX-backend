from fastapi import Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session
from app.api.v1.common.utils import create_downloadable_response
from app.database import get_db
from .service import SeltoxService

async def get_all_seltox_data(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = SeltoxService.get_all_data(db)
        return create_downloadable_response(data, file_format, "seltox_all_data")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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