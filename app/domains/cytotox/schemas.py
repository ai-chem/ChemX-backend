from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class CytotoxQueryParams(BaseModel):
    """Параметры запроса данных цитотоксичности"""
    limit: int = 50
    offset: int = 0


class CytotoxResponse(BaseModel):
    """Ответ с данными цитотоксичности"""
    data: List[Dict[str, Any]]
    total: int

class CytotoxAllDataResponse(BaseModel):
    """Ответ со ВСЕМИ данными цитотоксичности"""
    data: List[Dict[str, Any]]