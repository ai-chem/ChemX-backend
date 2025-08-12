from fastapi.testclient import TestClient

from app.main import app

# Создаем клиент, который будет использоваться для всех тестов в этом файле
client = TestClient(app)


# --- Тесты для эндпоинта /api/v1/seltox/data/all ---


def test_get_all_seltox_data_contract():
    """
    Проверяет контракт ответа для эндпоинта /data/all домена Seltox.
    """
    EXPECTED_COLUMNS = {
        "serial_number",
        "nanoparticle_id",
        "nanoparticle",
        "normalized_shape",
        "has_coating",
        "np_size_avg_nm",
        "canonical_name",
        "shape",
        "coating",
        "np_size_min_nm",
        "np_size_max_nm",
        "hydrodynamic_diameter_nm",
        "zeta_potential_mv",
        "synthesis_method",
        "standardized_synthesis_method",
        "precursor_of_np",
        "ph_during_synthesis",
        "temperature_for_extract_c",
        "duration_preparing_extract_min",
        "concentration_of_precursor_mm",
        "solvent_for_extract",
        "bacteria_id",
        "bacteria",
        "strain",
        "mdr",
        "publication_id",
        "doi",
        "article_list",
        "journal_name",
        "publisher",
        "year",
        "title",
        "journal_is_oa",
        "is_oa",
        "oa_status",
        "pdf",
        "access",
        "reference",
        "source_id",
        "source_table",
        "dbt_loaded_at",
        "method",
        "mic_np_µg_ml",
        "mic_np_µg_ml_parsed",
        "concentration",
        "zoi_np_mm",
        "time_set_hours",
    }

    response = client.get("/api/v1/seltox/data/all?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что данные для /seltox/data/all не будут пустыми"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /seltox/data/all нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_seltox_column_stats_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по колонкам домена Seltox.
    """
    EXPECTED_COLUMNS = {
        "column_name",
        "data_type",
        "total_rows",
        "null_count",
        "null_percentage",
    }

    response = client.get("/api/v1/seltox/analytics/column-stats?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что статистика по колонкам не будет пустой"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /seltox/analytics/column-stats нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_seltox_row_stats_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по строкам домена Seltox.
    """
    EXPECTED_COLUMNS = {
        "total_rows",
        "unique_nanoparticles",
        "unique_publications",
        "unique_bacteria",
        "unique_sources",
        "min_year",
        "max_year",
        "rows_with_80_percent_filled",
    }

    response = client.get("/api/v1/seltox/analytics/row-stats?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert (
        len(data) == 1
    ), "Ожидалось, что статистика по строкам будет состоять из одной записи"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /seltox/analytics/row-stats нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_seltox_top_categories_contract():
    """
    Проверяет контракт ответа для эндпоинта
    со статистикой по топовым категориям домена Seltox.
    """
    EXPECTED_COLUMNS = {
        "nanoparticle",
        "experiments_count",
        "avg_mic_np_µg_ml",
        "min_mic_np_µg_ml",
        "max_mic_np_µg_ml",
        "unique_publications",
        "unique_bacteria",
        "first_year",
        "last_year",
    }

    response = client.get("/api/v1/seltox/analytics/top-categories?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert (
        len(data) > 0
    ), "Ожидалось, что статистика по топовым категориям не будет пустой"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /seltox/analytics/top-categories нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_seltox_ml_data_contract():
    """
    Проверяет контракт ответа для эндпоинта с ML-данными домена Seltox.
    """
    EXPECTED_COLUMNS = {
        "serial_number",
        "nanoparticle",
        "has_coating",
        "normalized_shape",
        "method",
        "bacteria",
        "mdr",
        "coating",
        "is_coating_imputed",
        "np_size_min_nm",
        "is_np_size_min_nm_imputed",
        "np_size_max_nm",
        "is_np_size_max_nm_imputed",
        "np_size_avg_nm",
        "is_np_size_avg_nm_imputed",
        "zeta_potential_mv",
        "is_zeta_potential_mv_imputed",
        "hydrodynamic_diameter_nm",
        "is_hydrodynamic_diameter_nm_imputed",
        "temperature_for_extract_c",
        "is_temperature_for_extract_c_imputed",
        "duration_preparing_extract_min",
        "is_duration_preparing_extract_min_imputed",
        "concentration_of_precursor_mm",
        "is_concentration_of_precursor_mm_imputed",
        "mic_np_µg_ml_parsed",
        "is_mic_np_µg_ml_parsed_imputed",
        "concentration",
        "is_concentration_imputed",
        "zoi_np_mm",
        "is_zoi_np_mm_imputed",
        "time_set_hours",
        "is_time_set_hours_imputed",
        "shape",
        "is_shape_imputed",
        "standardized_synthesis_method",
        "is_standardized_synthesis_method_imputed",
        "synthesis_method",
        "is_synthesis_method_imputed",
        "solvent_for_extract",
        "is_solvent_for_extract_imputed",
        "precursor_of_np",
        "is_precursor_of_np_imputed",
        "mic_np_µg_ml",
        "is_mic_np_µg_ml_imputed",
        "strain",
        "is_strain_imputed",
    }

    response = client.get("/api/v1/seltox/data/ml?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что ML-данные не будут пустыми"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /seltox/data/ml нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )
