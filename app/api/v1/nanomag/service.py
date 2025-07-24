# app/api/v1/nanomag/service.py

from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Any


class NanomagService:
    """Сервис для работы с данными домена Nanomag."""

    @staticmethod
    def get_all_data(db: Session) -> List[Dict[str, Any]]:
        """
        Получение ВСЕХ данных из таблицы nanomag.
        """
        # !!! ВАЖНО: Замени 'serving_all_data_nanomag' на реальное имя твоей таблицы Nanomag !!!
        table_name = "dbt_serving.serving_all_data_nanomag"

        query = text(f"SELECT * FROM {table_name}")

        result = db.execute(query)
        data = [dict(row._mapping) for row in result]

        return data

    @staticmethod
    def get_column_stats(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_column_stats_nanomag"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_row_stats(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_row_stats_nanomag"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_top_categories(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_top_categories_nanomag"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]