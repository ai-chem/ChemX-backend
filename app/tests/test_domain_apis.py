# tests/test_domain_apis.py
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Если добавится новый домен, просто добавлю сюда
DOMAIN_PREFIXES = [
    "/api/v1/cytotox",
    "/api/v1/nanomag",
    "/api/v1/nanozymes",
    "/api/v1/seltox",
    "/api/v1/synergy",
]

# Определяем список ОБЩИХ эндпоинтов, которые есть у каждого домена
COMMON_ENDPOINTS = [
    "/data/all",
    "/analytics/column-stats",
    "/analytics/row-stats",
    "/analytics/top-categories",
]


# Создаем тестовую функцию, которая проверит ВСЁ
@pytest.mark.parametrize("domain_prefix", DOMAIN_PREFIXES)
@pytest.mark.parametrize("endpoint", COMMON_ENDPOINTS)
def test_all_common_endpoints_succeed(domain_prefix: str, endpoint: str):
    """
    Тест, который проверяет, что каждый общий эндпоинт
    для каждого домена возвращает успешный ответ 200 и правильный
    тип файла (CSV или JSON)
    """
    # Формируем полный URL для запроса
    # например /api/v1/cytotox + /data/all
    full_url = f"{domain_prefix}{endpoint}"

    # Проверяем скачивание в формате CSV
    print(f"проверяем загрузку csv для - {full_url}")  # Этот print поможет при отладке
    response_csv = client.get(f"{full_url}?file_format=csv")

    # Проверка ответа для CSV
    assert response_csv.status_code == 200, f"Failed GET {full_url}?file_format=csv"
    assert "text/csv" in response_csv.headers["content-type"]

    # Проверяем скачивание в формате JSON
    print(f"Testing JSON download for: {full_url}")  # И этот тоже
    response_json = client.get(f"{full_url}?file_format=json")

    # Проверка ответа для JSON
    assert response_json.status_code == 200, f"Failed GET {full_url}?file_format=json"
    assert "application/json" in response_json.headers["content-type"]
