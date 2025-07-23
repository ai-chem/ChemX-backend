from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union, Generic, TypeVar
from enum import Enum
from datetime import datetime


class SortDirection(str, Enum):
    """Направление сортировки данных"""
    ASC = "asc"
    DESC = "desc"


class SortParams(BaseModel):
    """Параметры сортировки данных"""
    field: str
    direction: SortDirection = SortDirection.ASC


class PaginationParams(BaseModel):
    """Параметры пагинации для постраничного вывода"""
    page: int = Field(1, ge=1, description="Номер страницы (начиная с 1)")
    page_size: int = Field(50, ge=1, le=500, description="Размер страницы")


class FilterOperator(str, Enum):
    """Операторы для фильтрации данных"""
    EQ = "eq"  # равно
    NE = "ne"  # не равно
    GT = "gt"  # больше
    GE = "ge"  # больше или равно
    LT = "lt"  # меньше
    LE = "le"  # меньше или равно
    LIKE = "like"  # содержит подстроку
    IN = "in"  # входит в список значений
    BETWEEN = "between"  # между двумя значениями


class FilterCondition(BaseModel):
    """Условие фильтрации для одного поля"""
    field: str
    operator: FilterOperator
    value: Any = None
    values: Optional[List[Any]] = None  # для операторов IN и BETWEEN


class DataFilter(BaseModel):
    """Полная модель фильтрации данных"""
    conditions: List[FilterCondition] = []
    logic_operator: str = "AND"  # OR, AND


class DataRequestParams(BaseModel):
    """Комбинированные параметры для запроса данных"""
    pagination: Optional[PaginationParams] = PaginationParams()
    sorting: Optional[List[SortParams]] = None
    filtering: Optional[DataFilter] = None


class BaseResponse(BaseModel):
    """Базовый класс для ответов API"""
    status: str = "success"


class DataResponse(BaseResponse):
    """Ответ с данными и метаинформацией"""
    data: List[Dict[str, Any]]
    total: int
    page: int
    page_size: int
    total_pages: int


class ErrorResponse(BaseModel):
    """Структура ответа при ошибке"""
    status: str = "error"
    message: str
    detail: Optional[Any] = None