from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_cytotox_ml_data_contract():
    """
    Проверяет контракт ответа для эндпоинта с ML-данными.
    Тест гарантирует, что:
    1. Эндпоинт отвечает успешно.
    2. Набор колонок в ответе не изменился.
    """
    EXPECTED_COLUMNS = {
        "serial_number",
        "nanoparticle",
        "normalized_shape",
        "has_coating",
        "time_hr",
        "cell_type",
        "potential_mv",
        "is_potential_mv_imputed",
        "zeta_potential_mv",
        "is_zeta_potential_mv_imputed",
        "hydrodynamic_nm",
        "is_hydrodynamic_nm_imputed",
        "size_in_medium_nm",
        "is_size_in_medium_nm_imputed",
        "np_size_avg_nm",
        "is_np_size_avg_nm_imputed",
        "no_of_cells_cells_well",
        "is_no_of_cells_cells_well_imputed",
        "concentration",
        "is_concentration_imputed",
        "viability_percent",
        "is_viability_percent_imputed",
        "shape",
        "is_shape_imputed",
        "coat_functional_group",
        "is_coat_functional_group_imputed",
        "synthesis_method",
        "is_synthesis_method_imputed",
        "surface_charge",
        "is_surface_charge_imputed",
        "test",
        "is_test_imputed",
        "test_indicator",
        "is_test_indicator_imputed",
        "cell_source",
        "is_cell_source_imputed",
        "cell_tissue",
        "is_cell_tissue_imputed",
        "cell_morphology",
        "is_cell_morphology_imputed",
        "cell_age",
        "is_cell_age_imputed",
        "standardized_synthesis_method",
        "is_standardized_synthesis_method_imputed",
        "is_surface_positive",
        "is_is_surface_positive_imputed",
        "is_human",
        "is_is_human_imputed",
    }

    response = client.get("/api/v1/cytotox/data/ml?file_format=json")

    assert response.status_code == 200, "Ожидался статус-код 200"

    data = response.json()
    assert isinstance(data, list), "Ответ должен быть списком"
    assert len(data) > 0, "Ожидалось, что ML-данные не будут пустыми"

    # сверяем ключи первой записи с нашим контрактом
    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API нарушен! "
        f"Лишние ключи: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_all_cytotox_data_contract():
    """
    Проверяет контракт ответа для эндпоинта /data/all.
    Тест гарантирует, что структура JSON-ответа (набор колонок) не изменилась.
    """
    EXPECTED_COLUMNS = {
        "serial_number",
        "nanoparticle_id",
        "nanoparticle",
        "normalized_shape",
        "shape",
        "has_coating",
        "np_size_avg_nm",
        "canonical_name",
        "coat_functional_group",
        "standardized_synthesis_method",
        "is_surface_positive",
        "potential_mv",
        "hydrodynamic_nm",
        "core_nm",
        "zeta_potential_mv",
        "size_in_medium_nm",
        "surface_charge",
        "synthesis_method",
        "cell_line_id",
        "canonical_cell_line_name",
        "cell_type",
        "human_animal",
        "cell_source",
        "cell_tissue",
        "cell_morphology",
        "cell_age",
        "is_human",
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
        "source_id",
        "source_table",
        "dbt_loaded_at",
        "dbt_curated_at",
        "no_of_cells_cells_well",
        "time_hr",
        "concentration",
        "test",
        "test_indicator",
        "viability_percent",
    }

    response = client.get("/api/v1/cytotox/data/all?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что данные для /data/all не будут пустыми"

    # набор ключей в первой записи должен точно совпадать с ожидаемым
    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /cytotox/data/all нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_cytotox_column_stats_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по колонкам.
    """
    EXPECTED_COLUMNS = {
        "column_name",
        "data_type",
        "total_rows",
        "null_count",
        "null_percentage",
    }

    response = client.get("/api/v1/cytotox/analytics/column-stats?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что статистика по колонкам не будет пустой"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /cytotox/analytics/column-stats нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_cytotox_row_stats_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по строкам.
    """
    EXPECTED_COLUMNS = {
        "total_rows",
        "unique_nanoparticles",
        "unique_publications",
        "unique_cell_lines",
        "unique_np_cell_line_pairs",
        "min_year",
        "max_year",
        "rows_with_80_percent_filled",
    }

    response = client.get("/api/v1/cytotox/analytics/row-stats?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Статистика по строкам - это обычно одна-единственная строка
    assert (
        len(data) == 1
    ), "Ожидалось, что статистика по строкам будет состоять из одной записи"

    # набор ключей в записи должен точно совпадать с ожидаемым
    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /cytotox/analytics/row-stats нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_cytotox_top_categories_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по топовым категориям.
    """

    EXPECTED_COLUMNS = {
        "nanoparticle",
        "experiments_count",
        "avg_viability",
        "min_viability",
        "max_viability",
        "unique_cell_lines",
        "unique_publications",
        "first_year",
        "last_year",
    }

    response = client.get("/api/v1/cytotox/analytics/top-categories?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert (
        len(data) > 0
    ), "Ожидалось, что статистика по топовым категориям не будет пустой"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /cytotox/analytics/top-categories нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )
