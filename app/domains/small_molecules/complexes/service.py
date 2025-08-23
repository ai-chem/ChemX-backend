from typing import Any

from sqlalchemy import text
from sqlalchemy.orm import Session


class ComplexesService:
    @staticmethod
    def get_all_data(
        db: Session, nanoparticle: str | None = None
    ) -> list[dict[str, Any]]:
        """
        Получает все данные для complexes.
        Аргумент nanoparticle здесь присутствует только для совместимости
        с UniversalDataService. Пока что для малых молекул фильтрации нет.
        """
        table_name = "dbt_serving.serving_all_data_complexes"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_column_stats(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_column_stats_complexes"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_row_stats(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_row_stats_complexes"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_top_categories(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_top_categories_complexes"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_ml_data(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_ml_complexes"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]
