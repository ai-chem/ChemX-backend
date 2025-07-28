
from fastapi import Depends, HTTPException, Query, Response
from typing import Optional
from sqlalchemy.orm import Session

# Импортируем новую утилиту
from app.domains.common.utils import create_downloadable_response

from database import get_db
from app.domains.cytotox.service import CytotoxService
from app.domains.cytotox.schemas import CytotoxResponse


# --- Эндпоинт с пагинацией ---
async def get_cytotox_data(
    limit: int = Query(50, gt=0, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
) -> CytotoxResponse:
    try:
        data, total = CytotoxService.get_data(db, limit, offset)
        return CytotoxResponse(data=data, total=total)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении данных: {str(e)}")



async def get_all_cytotox_data(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"]),
    nanoparticle: Optional[str] = Query(None, description="Фильтр по материалу наночастицы")
) -> Response:
    try:
        # Передаем параметр в сервис
        all_data = CytotoxService.get_all_data(db, nanoparticle=nanoparticle)

        # 2. Делегируем всю работу по созданию ответа нашей утилите
        return create_downloadable_response(
            data=all_data,
            file_format=file_format,
            base_filename="cytotox_all_data"
        )

    except Exception as e:
        # Обработка ошибок остается на случай, если сервис вернет ошибку
        print(f"Произошла ошибка: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка при получении данных: {str(e)}")


async def get_cytotox_column_stats(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"])
) -> Response:
    """
    Скачать статистику по колонкам для домена Cytotox.
    """
    try:
        # Вызываем новый метод сервиса
        stats_data = CytotoxService.get_column_stats(db)
        # Переиспользуем нашу универсальную утилиту
        return create_downloadable_response(
            data=stats_data,
            file_format=file_format,
            base_filename="cytotox_column_stats"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_cytotox_row_stats(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"])
) -> Response:
    """
    Скачать статистику по строкам для домена Cytotox.
    """
    try:
        # Вызываем второй новый метод сервиса
        stats_data = CytotoxService.get_row_stats(db)
        # И снова переиспользуем нашу утилиту
        return create_downloadable_response(
            data=stats_data,
            file_format=file_format,
            base_filename="cytotox_row_stats"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_cytotox_top_categories(
    db: Session = Depends(get_db),
    file_format: str = Query("json", enum=["json", "csv"])
) -> Response:
    """
    Скачать статистику по топовым категориям для домена Cytotox.
    """
    try:
        stats_data = CytotoxService.get_top_categories(db)
        return create_downloadable_response(
            data=stats_data,
            file_format=file_format,
            base_filename="cytotox_top_categories"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))