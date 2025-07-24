from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Any

class NanozymesService:
    @staticmethod
    def get_all_data(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_all_data_nanozymes"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]
        return data