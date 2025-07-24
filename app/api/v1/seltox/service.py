from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Any

class SeltoxService:
    @staticmethod
    def get_all_data(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_all_data_seltox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]
        return data

    @staticmethod
    def get_column_stats(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_column_stats_seltox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_row_stats(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_row_stats_seltox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_top_categories(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_top_categories_seltox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]