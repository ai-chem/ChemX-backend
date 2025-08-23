from typing import Any

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.domains.common.utils import build_filtered_query


class CytotoxService:
    """Сервис для работы с данными цитотоксичности"""

    @staticmethod
    def get_data(
        db: Session, limit: int = 50, offset: int = 0
    ) -> tuple[list[dict[str, Any]], int]:
        """
        Получение данных с применением пагинации

        Args:
            db: Сессия базы данных
            limit: Максимальное количество записей
            offset: Смещение выборки

        Returns:
            Tuple[List[Dict], int]: Список записей и общее количество записей
        """
        total_count_result = db.execute(
            text("SELECT COUNT(*) FROM dbt_serving.serving_all_data_cytotox")
        ).scalar()

        # Если .scalar() вернул None (например, таблица пуста), мы считаем, что это 0.
        # Таким образом, переменная total_count ГАРАНТИРОВАННО будет типа int.
        total_count = total_count_result or 0

        # Выполняем запрос с пагинацией
        query = text(
            f"""
        SELECT * FROM dbt_serving.serving_all_data_cytotox
        LIMIT {limit} OFFSET {offset}
        """
        )

        # Выполняем запрос и преобразуем результат в список словарей
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]

        return data, total_count

    @staticmethod
    def get_all_data(
        db: Session,
        nanoparticle: str | None = None,
        # В будущем сюда можно добавлять другие фильтры:
        # cell_line: Optional[str] = None
    ) -> list[dict[str, Any]]:
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
    def get_column_stats(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_column_stats_cytotox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]
        return data

    @staticmethod
    def get_row_stats(db: Session) -> list[dict[str, Any]]:
        table_name = "dbt_serving.serving_analytics_row_stats_cytotox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]
        return data

    @staticmethod
    def get_top_categories(db: Session) -> list[dict[str, Any]]:
        """
        Получение статистики по топовым категориям для домена Cytotox.
        """
        table_name = "dbt_serving.serving_analytics_top_categories_cytotox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]
        return data

    @staticmethod
    def get_ml_data(db: Session) -> list[dict[str, Any]]:
        """
        Получение данных из ML-таблицы для домена Cytotox.
        """
        table_name = "dbt_serving.serving_ml_cytotox"
        query = text(f"SELECT * FROM {table_name}")
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]
        return data
