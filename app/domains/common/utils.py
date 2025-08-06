from typing import Any

import pandas as pd
from fastapi import Response
from sqlalchemy import text
from sqlalchemy.sql.elements import TextClause


def create_downloadable_response(
    data: list[dict[str, Any]], file_format: str, base_filename: str
) -> Response:
    """
    Универсальная функция для создания ответа для скачивания файла (JSON или CSV).

    Args:
        data: Список словарей с данными.
        file_format: Желаемый формат ('csv' или 'json').
        base_filename: Базовое имя файла без расширения (e.g., 'cytotox_data').

    Returns:
        Объект fastapi.Response, готовый к отправке.
    """
    if not data:
        # Если данных нет, возвращаем пустой ответ
        return Response(status_code=204)

    # Создаем DataFrame из "сырых" данных
    df = pd.DataFrame(data)

    # В зависимости от формата, готовим контент и метаданные
    if file_format == "csv":
        content = df.to_csv(index=False)
        media_type = "text/csv"
        filename = f"{base_filename}.csv"

    else:  # По умолчанию json
        content = df.to_json(orient="records", indent=2)
        media_type = "application/json"
        filename = f"{base_filename}.json"

    # Возвращаем готовый Response
    return Response(
        content=content,
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


def build_filtered_query(
    base_table: str, filters: dict[str, Any] | None = None
) -> tuple[TextClause, dict[str, Any]]:
    """
    Универсально строит SQL-запрос с WHERE-условиями на основе словаря.

    Args:
        base_table: Имя таблицы с путем (e.g., 'dbt_serving.my_table').
        filters: Словарь, где ключ - имя колонки, значение - значение для фильтра.

    Returns:
        Кортеж из (SQLAlchemy-запрос, словарь с параметрами).
    """
    query_string = f"SELECT * FROM {base_table}"
    params = {}
    where_clauses = []

    if filters:
        for column, value in filters.items():
            if value is not None:
                # Мы предполагаем, что имена колонок безопасны,
                # т.к. они приходят из кода, а не от пользователя напрямую.
                param_name = f"filter_{column}"
                where_clauses.append(f"{column} = :{param_name}")
                params[param_name] = value

    if where_clauses:
        query_string += " WHERE " + " AND ".join(where_clauses)

    return text(query_string), params
