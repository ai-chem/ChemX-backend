# tests/synergy/test_api.py
from fastapi.testclient import TestClient

from app.main import app

# Создаем клиент, который будет использоваться для всех тестов в этом файле
client = TestClient(app)


# --- Тесты для эндпоинта /api/v1/synergy/data/all ---


def test_get_all_synergy_data_contract():
    """
    Проверяет контракт ответа для эндпоинта /data/all домена Synergy.
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
        "np_size_min_nm",
        "np_size_max_nm",
        "np_size_min_nm_parsed",
        "zeta_potential_mv",
        "zeta_potential_mv_parsed",
        "synthesis_method",
        "standardized_synthesis_method",
        "coating_with_antimicrobial_peptide_polymers",
        "bacteria_id",
        "bacteria",
        "strain",
        "mdr",
        "drug_id",
        "drug",
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
        "access_bool",
        "reference",
        "source_id",
        "source_table",
        "dbt_loaded_at",
        "method",
        "zoi_drug_mm_or_mic__µg_ml",
        "error_zoi_drug_mm_or_mic_µg_ml",
        "zoi_np_mm_or_mic_np_µg_ml",
        "error_zoi_np_mm_or_mic_np_µg_ml",
        "zoi_drug_np_mm_or_mic_drug_np_µg_ml",
        "error_zoi_drug_np_mm_or_mic_drug_np_µg_ml",
        "fold_increase_in_antibacterial_activity",
        "fic",
        "effect",
        "drug_dose_µg_disk",
        "np_concentration_µg_ml",
        "combined_mic",
        "peptide_mic",
        "viability_percent",
        "viability_error",
        "time_hr",
    }

    response = client.get("/api/v1/synergy/data/all?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что данные для /synergy/data/all не будут пустыми"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /synergy/data/all нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_synergy_column_stats_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по колонкам домена Synergy.
    """
    EXPECTED_COLUMNS = {
        "column_name",
        "data_type",
        "total_rows",
        "null_count",
        "null_percentage",
    }

    response = client.get("/api/v1/synergy/analytics/column-stats?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что статистика по колонкам не будет пустой"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /synergy/analytics/column-stats нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_synergy_row_stats_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по строкам домена Synergy.
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

    response = client.get("/api/v1/synergy/analytics/row-stats?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert (
        len(data) == 1
    ), "Ожидалось, что статистика по строкам будет состоять из одной записи"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /synergy/analytics/row-stats нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_synergy_top_categories_contract():
    """
    Проверяет контракт ответа для эндпоинта
    со статистикой по топовым категориям домена Synergy.
    """
    EXPECTED_COLUMNS = {
        "nanoparticle",
        "experiments_count",
        "avg_viability",
        "min_viability",
        "max_viability",
        "unique_publications",
        "unique_bacteria",
        "first_year",
        "last_year",
    }

    response = client.get("/api/v1/synergy/analytics/top-categories?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert (
        len(data) > 0
    ), "Ожидалось, что статистика по топовым категориям не будет пустой"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /synergy/analytics/top-categories нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )
