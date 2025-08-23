from typing import Any

from sqlalchemy import text
from sqlalchemy.orm import Session


class CoCrystalsService:
    @staticmethod
    def get_all_data(
        db: Session, nanoparticle: str | None = None
    ) -> list[dict[str, Any]]:
        """
        Получает все данные для co_crystals.
        Аргумент nanoparticle здесь присутствует только для совместимости
        с UniversalDataService. Пока что для малых молекул фильтрации нет.
        """
        table_name = "dbt_serving.serving_all_data_co_crystals"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_column_stats(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_column_stats_co_crystals"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_row_stats(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_row_stats_co_crystals"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_top_categories(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_top_categories_co_crystals"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_ml_data(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_ml_co_crystals"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]
