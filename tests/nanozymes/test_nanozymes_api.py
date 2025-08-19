from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_all_nanozymes_data_contract():
    """
    Проверяет контракт ответа для эндпоинта /data/all домена Nanozymes.
    """
    EXPECTED_COLUMNS = {
        "id",
        "nanoparticle_id",
        "publication_id",
        "source_id",
        "activity",
        "reaction_type",
        "target_source",
        "c_min",
        "c_max",
        "c_const",
        "c_const_unit",
        "ccat_value",
        "ccat_unit",
        "km_value",
        "km_unit",
        "vmax_value",
        "vmax_unit",
        "ph",
        "temperature",
        "nanoparticle",
        "syngony",
        "surface",
        "length_lower",
        "length_upper",
        "length_mean",
        "width_lower",
        "width_upper",
        "width_mean",
        "depth_lower",
        "depth_upper",
        "depth_mean",
        "length",
        "width",
        "depth",
        "doi",
        "journal",
        "year",
        "title",
        "pdf",
        "access",
        "access_bool",
        "source_table",
        "dbt_loaded_at",
        "dbt_curated_at",
    }

    response = client.get("/api/v1/nanozymes/data/all?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert (
        len(data) > 0
    ), "Ожидалось, что данные для /nanozymes/data/all не будут пустыми"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /nanozymes/data/all нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_nanozymes_column_stats_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по колонкам домена Nanozymes.
    """
    EXPECTED_COLUMNS = {
        "column_name",
        "data_type",
        "total_rows",
        "null_count",
        "null_percentage",
    }

    response = client.get("/api/v1/nanozymes/analytics/column-stats?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что статистика по колонкам не будет пустой"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /nanozymes/analytics/column-stats нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_nanozymes_row_stats_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по строкам домена Nanozymes.
    """
    EXPECTED_COLUMNS = {
        "total_rows",
        "unique_nanoparticles",
        "unique_publications",
        "unique_sources",
        "min_year",
        "max_year",
        "rows_with_80_percent_filled",
    }

    response = client.get("/api/v1/nanozymes/analytics/row-stats?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert (
        len(data) == 1
    ), "Ожидалось, что статистика по строкам будет состоять из одной записи"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /nanozymes/analytics/row-stats нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_nanozymes_top_categories_contract():
    """
    Проверяет контракт ответа для эндпоинта
    со статистикой по топовым категориям домена Nanozymes.
    """
    EXPECTED_COLUMNS = {
        "nanoparticle",
        "experiments_count",
        "avg_vmax",
        "min_vmax",
        "max_vmax",
        "unique_publications",
        "first_year",
        "last_year",
    }

    response = client.get("/api/v1/nanozymes/analytics/top-categories?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert (
        len(data) > 0
    ), "Ожидалось, что статистика по топовым категориям не будет пустой"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /nanozymes/analytics/top-categories нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_nanozymes_ml_data_contract():
    """
    Проверяет контракт ответа для эндпоинта с ML-данными домена Nanozymes.
    """

    EXPECTED_COLUMNS = {
        # Столбцы без импутации
        "nanoparticle",
        "activity",
        "reaction_type",
        # Числовые столбцы и их флаги импутации
        "length_mean",
        "is_length_mean_imputed",
        "width_mean",
        "is_width_mean_imputed",
        "depth_mean",
        "is_depth_mean_imputed",
        "c_min",
        "is_c_min_imputed",
        "c_max",
        "is_c_max_imputed",
        "c_const",
        "is_c_const_imputed",
        "ccat_value",
        "is_ccat_value_imputed",
        "km_value",
        "is_km_value_imputed",
        "ph",
        "is_ph_imputed",
        "temperature",
        "is_temperature_imputed",
        "vmax_standardized_m_per_s",
        "is_vmax_standardized_m_per_s_imputed",
        # Категориальные столбцы и их флаги импутации
        "syngony",
        "is_syngony_imputed",
        "length",
        "is_length_imputed",
        "width",
        "is_width_imputed",
        "depth",
        "is_depth_imputed",
        "surface",
        "is_surface_imputed",
        "c_const_unit",
        "is_c_const_unit_imputed",
        "ccat_unit",
        "is_ccat_unit_imputed",
        "km_unit",
        "is_km_unit_imputed",
    }

    response = client.get("/api/v1/nanozymes/data/ml?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что ML-данные не будут пустыми"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /nanozymes/data/ml нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )
