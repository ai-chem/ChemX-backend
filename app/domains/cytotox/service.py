from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Any, Tuple, Optional
from app.domains.common.utils import build_filtered_query


class CytotoxService:
    """Сервис для работы с данными цитотоксичности"""

    @staticmethod
    def get_data(db: Session, limit: int = 50, offset: int = 0) -> Tuple[List[Dict[str, Any]], int]:
        """
        Получение данных с применением пагинации

        Args:
            db: Сессия базы данных
            limit: Максимальное количество записей
            offset: Смещение выборки

        Returns:
            Tuple[List[Dict], int]: Список записей и общее количество записей
        """
        # Получаем общее количество записей
        total_count = db.execute(text("SELECT COUNT(*) FROM dbt_serving.serving_all_data_cytotox")).scalar()

        # Выполняем запрос с пагинацией
        query = text(f"""
        SELECT * FROM dbt_serving.serving_all_data_cytotox
        LIMIT {limit} OFFSET {offset}
        """)

        # Выполняем запрос и преобразуем результат в список словарей
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]

        return data, total_count

    @staticmethod
    def get_all_data(
            db: Session,
            nanoparticle: Optional[str] = None
            # В будущем сюда можно добавлять другие фильтры:
            # cell_line: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_all_data_cytotox"

        # Собираем фильтры в словарь
        filters = {
            "nanoparticle": nanoparticle,
            # "cell_line": cell_line
        }

        # Делегируем всю сложную работу утилите
        query, params = build_filtered_query(table_name, filters)

        result = db.execute(query, params)
        data = [dict(row._mapping) for row in result]
        return data

    @staticmethod
    def get_column_stats(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_column_stats_cytotox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]
        return data

    @staticmethod
    def get_row_stats(db: Session) -> List[Dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_row_stats_cytotox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]
        return data

    @staticmethod
    def get_top_categories(db: Session) -> List[Dict[str, Any]]:
        """
        Получение статистики по топовым категориям для домена Cytotox.
        """
        table_name = "dbt_serving.serving_analytics_top_categories_cytotox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]
        return data