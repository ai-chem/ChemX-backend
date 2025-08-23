# app/api/v1/nanomag/service.py
from typing import Any

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.domains.common.utils import build_filtered_query


class NanomagService:
    @staticmethod
    def get_all_data(
        db: Session, nanoparticle: str | None = None
    ) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_all_data_nanomag"

        filters = {
            "nanoparticle": nanoparticle,
        }
        query, params = build_filtered_query(table_name, filters)
        result = db.execute(query, params)
        data = [dict(row._mapping) for row in result]
        return data

    # Здесь остаются другие методы для аналитики, если они были
    @staticmethod
    def get_column_stats(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_column_stats_nanomag"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_row_stats(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_row_stats_nanomag"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_top_categories(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_top_categories_nanomag"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_ml_data(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_ml_nanomag"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]
