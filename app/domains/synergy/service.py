from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional
from app.domains.common.utils import build_filtered_query
from sqlalchemy import text

class SynergyService:
    @staticmethod
    def get_all_data(db: Session, nanoparticle: Optional[str] = None) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_all_data_synergy"
        filters = {"nanoparticle": nanoparticle}
        query, params = build_filtered_query(table_name, filters)
        result = db.execute(query, params)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_column_stats(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_column_stats_synergy"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_row_stats(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_row_stats_synergy"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_top_categories(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_top_categories_synergy"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        return [dict(row._mapping) for row in result]