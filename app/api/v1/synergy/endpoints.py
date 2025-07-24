from fastapi import Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session
from app.api.v1.common.utils import create_downloadable_response
from app.database import get_db
from .service import SynergyService

async def get_all_synergy_data(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = SynergyService.get_all_data(db)
        return create_downloadable_response(data, file_format, "synergy_all_data")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_synergy_column_stats(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = SynergyService.get_column_stats(db)
        return create_downloadable_response(data, file_format, "synergy_column_stats")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_synergy_row_stats(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = SynergyService.get_row_stats(db)
        return create_downloadable_response(data, file_format, "synergy_row_stats")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_synergy_top_categories(db: Session = Depends(get_db), file_format: str = Query("json", enum=["json", "csv"])) -> Response:
    try:
        data = SynergyService.get_top_categories(db)
        return create_downloadable_response(data, file_format, "synergy_top_categories")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))