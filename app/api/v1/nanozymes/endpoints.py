from fastapi import Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session
from app.api.v1.common.utils import create_downloadable_response
from app.database import get_db
from .service import NanozymesService

async def get_all_nanozymes_data(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"])
) -> Response:
    try:
        all_data = NanozymesService.get_all_data(db)
        return create_downloadable_response(
            data=all_data,
            file_format=file_format,
            base_filename="nanozymes_all_data"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))