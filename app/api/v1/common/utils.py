
from fastapi import Response
import pandas as pd
from typing import List, Dict, Any


def create_downloadable_response(
        data: List[Dict[str, Any]],
        file_format: str,
        base_filename: str
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
        content = df.to_json(orient='records', indent=2)
        media_type = "application/json"
        filename = f"{base_filename}.json"

    # Возвращаем готовый Response
    return Response(
        content=content,
        media_type=media_type,
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )