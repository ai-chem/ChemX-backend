from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Any, Tuple


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
    def get_all_data(db: Session) -> List[Dict[str, Any]]:
        """
        Получение ВСЕХ данных из таблицы без пагинации.

        Args:
            db: Сессия базы данных

        Returns:
            Список всех записей.
        """
        # Простой запрос на получение всех данных
        query = text(f"""SELECT * FROM dbt_serving.serving_all_data_cytotox""")

        # Выполняем запрос и преобразуем результат в список словарей
        result = db.execute(query)
        data = [dict(row._mapping) for row in result]

        return data