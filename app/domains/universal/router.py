# app/domains/universal/router.py
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from .schemas import DataType
from .schemas import Domain
from .service import UniversalDataService
from app.database import get_db
from app.domains.common.utils import create_downloadable_response

router = APIRouter()

# --- Эндпоинты ---


@router.get("/schema", summary="Получить схему доступных данных")
def get_data_schema():
    """
    Возвращает список всех доступных доменов и типов данных.
    """
    return {
        "available_domains": [d.value for d in Domain],
        "available_data_types": [dt.value for dt in DataType],
    }


@router.get("", summary="Универсальный эндпоинт для получения данных")
def get_universal_data(
    domain: Domain, data_type: DataType, db: Session = Depends(get_db)
):
    """
    Получает указанный датасет для указанного домена.
    """
    try:
        data = UniversalDataService.get_data(
            db=db, domain=domain.value, data_type=data_type.value
        )
        return create_downloadable_response(
            data, "json", f"{domain.value}_{data_type.value}"
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
