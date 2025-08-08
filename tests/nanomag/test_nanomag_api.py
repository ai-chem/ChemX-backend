from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_all_nanomag_data_contract():
    """
    Проверяет контракт ответа для эндпоинта /data/all домена Nanomag.
    """
    EXPECTED_COLUMNS = {
        "id",
        "zfc_h_meas",
        "htherm_sar",
        "mri_r1",
        "mri_r2",
        "squid_h_max",
        "hc_koe",
        "fc_field_t_numeric",
        "squid_temperature_numeric",
        "squid_sat_mag_numeric",
        "coercivity_numeric",
        "squid_rem_mag_numeric",
        "exchange_bias_shift_oe_numeric",
        "vertical_loop_shift_m_vsl_emu_g_numeric",
        "nanoparticle_id",
        "name",
        "np_shell_2",
        "np_hydro_size",
        "xrd_scherrer_size",
        "emic_size",
        "instrument",
        "core_shell_formula",
        "nanoparticle",
        "np_shell",
        "space_group_core",
        "space_group_shell",
        "fc_field_t_original",
        "squid_temperature_original",
        "squid_sat_mag_original",
        "coercivity_original",
        "squid_rem_mag_original",
        "exchange_bias_shift_oe_original",
        "vertical_loop_shift_m_vsl_emu_g_original",
        "publication_id",
        "doi",
        "journal",
        "publisher",
        "year",
        "title",
        "pdf",
        "access",
        "access_bool",
        "supp",
        "article_name_folder",
        "supp_info_name_folder",
        "validation_id",
        "comment",
        "has_mistake_in_matadata",
        "verification_required",
        "verified_by",
        "verification_date",
        "source_id",
        "source_table",
        "dbt_loaded_at",
        "dbt_curated_at",
    }

    response = client.get("/api/v1/nanomag/data/all?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что данные для /nanomag/data/all не будут пустыми"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /nanomag/data/all нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_nanomag_column_stats_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по колонкам домена Nanomag.
    """
    EXPECTED_COLUMNS = {
        "column_name",
        "data_type",
        "total_rows",
        "null_count",
        "null_percentage",
    }

    response = client.get("/api/v1/nanomag/analytics/column-stats?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что статистика по колонкам не будет пустой"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /nanomag/analytics/column-stats нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_nanomag_row_stats_contract():
    """
    Проверяет контракт ответа для эндпоинта со статистикой по строкам домена Nanomag.
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

    response = client.get("/api/v1/nanomag/analytics/row-stats?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert (
        len(data) == 1
    ), "Ожидалось, что статистика по строкам будет состоять из одной записи"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /nanomag/analytics/row-stats нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


# tests/nanomag/test_api.py

# ... (предыдущие тесты) ...


# --- Тесты для эндпоинта /api/v1/nanomag/analytics/top-categories ---


def test_get_nanomag_top_categories_contract():
    """
    Проверяет контракт ответа для эндпоинта
    со статистикой по топовым категориям домена Nanomag.
    """
    EXPECTED_COLUMNS = {
        "nanoparticle",
        "experiments_count",
        "unique_publications",
        "first_year",
        "last_year",
    }

    response = client.get("/api/v1/nanomag/analytics/top-categories?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert (
        len(data) > 0
    ), "Ожидалось, что статистика по топовым категориям не будет пустой"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /nanomag/analytics/top-categories нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )


def test_get_nanomag_ml_data_contract():
    """
    Проверяет контракт ответа для эндпоинта с ML-данными домена Nanomag.
    """
    EXPECTED_COLUMNS = {
        "id",
        "nanoparticle",
        "xrd_scherrer_size",
        "is_xrd_scherrer_size_imputed",
        "zfc_h_meas",
        "is_zfc_h_meas_imputed",
        "htherm_sar",
        "is_htherm_sar_imputed",
        "mri_r1",
        "is_mri_r1_imputed",
        "mri_r2",
        "is_mri_r2_imputed",
        "squid_h_max",
        "is_squid_h_max_imputed",
        "hc_koe",
        "is_hc_koe_imputed",
        "fc_field_t_numeric",
        "is_fc_field_t_numeric_imputed",
        "squid_temperature_numeric",
        "is_squid_temperature_numeric_imputed",
        "squid_sat_mag_numeric",
        "is_squid_sat_mag_numeric_imputed",
        "coercivity_numeric",
        "is_coercivity_numeric_imputed",
        "squid_rem_mag_numeric",
        "is_squid_rem_mag_numeric_imputed",
        "exchange_bias_shift_oe_numeric",
        "is_exchange_bias_shift_oe_numeric_imputed",
        "vertical_loop_shift_m_vsl_emu_g_numeric",
        "is_vertical_loop_shift_m_vsl_emu_g_numeric_imputed",
        "np_shell_2",
        "is_np_shell_2_imputed",
        "np_shell",
        "is_np_shell_imputed",
        "space_group_core",
        "is_space_group_core_imputed",
        "space_group_shell",
        "is_space_group_shell_imputed",
    }

    response = client.get("/api/v1/nanomag/data/ml?file_format=json")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Ожидалось, что ML-данные не будут пустыми"

    first_item_keys = set(data[0].keys())

    assert first_item_keys == EXPECTED_COLUMNS, (
        f"Контракт API для /nanomag/data/ml нарушен! "
        f"Лишние ключи в ответе: {first_item_keys - EXPECTED_COLUMNS}. "
        f"Недостающие ключи в ответе: {EXPECTED_COLUMNS - first_item_keys}."
    )
