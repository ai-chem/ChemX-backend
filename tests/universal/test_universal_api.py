import pytest
from fastapi.testclient import TestClient

from app.domains.universal.schemas import DataType
from app.domains.universal.schemas import Domain
from app.main import app


client = TestClient(app)

# Ожидаемые значения для проверки схемы
EXPECTED_DOMAINS = [d.value for d in Domain]
EXPECTED_DATA_TYPES = [dt.value for dt in DataType]

# Создаем список всех возможных комбинаций
ALL_COMBINATIONS = [
    (domain, data_type)
    for domain in EXPECTED_DOMAINS
    for data_type in EXPECTED_DATA_TYPES
]

# --- Тесты ---


def test_get_data_schema():
    """
    Проверяет, что эндпоинт /schema возвращает правильный и полный
    список доступных доменов и типов данных.
    """
    response = client.get("/api/v1/data/schema")

    assert response.status_code == 200
    data = response.json()

    assert "available_domains" in data
    assert "available_data_types" in data

    # Сравниваем содержимое списков (порядок не важен)
    assert set(data["available_domains"]) == set(EXPECTED_DOMAINS)
    assert set(data["available_data_types"]) == set(EXPECTED_DATA_TYPES)


@pytest.mark.parametrize("domain, data_type", ALL_COMBINATIONS)
def test_get_universal_data_for_all_combinations(domain: str, data_type: str):
    """
    Проверяет, что универсальный эндпоинт /data успешно возвращает данные
    для КАЖДОЙ возможной комбинации параметров.
    """
    print(f"Testing combination: domain={domain}, data_type={data_type}")

    response = client.get(f"/api/v1/data?domain={domain}&data_type={data_type}")

    assert (
        response.status_code == 200
    ), f"Failed for domain={domain}, data_type={data_type}"

    data = response.json()
    assert isinstance(data, list)

    # Если эндпоинт вернул данные, проверяем, что они не пустые и имеют структуру
    if data:
        first_item = data[0]
        assert isinstance(first_item, dict)
        assert len(first_item.keys()) > 0
    else:
        # Если данных нет, это не обязательно ошибка. Просто выводим предупреждение.
        print(
            f"Warning: Empty list returned for domain={domain}, data_type={data_type}"
        )
