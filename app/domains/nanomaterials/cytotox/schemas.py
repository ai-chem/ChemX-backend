from typing import Any

from pydantic import BaseModel


class CytotoxQueryParams(BaseModel):
    """Параметры запроса данных цитотоксичности"""

    limit: int = 50
    offset: int = 0


class CytotoxResponse(BaseModel):
    """Ответ с данными цитотоксичности"""

    data: list[dict[str, Any]]
    total: int


class CytotoxAllDataResponse(BaseModel):
    """Ответ со ВСЕМИ данными цитотоксичности"""

    data: list[dict[str, Any]]
