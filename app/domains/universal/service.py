# app/domains/universal/service.py
from sqlalchemy.orm import Session

from app.domains.common.service_map import METHOD_MAP
from app.domains.common.service_map import SERVICE_MAP


class UniversalDataService:
    @staticmethod
    def get_data(db: Session, domain: str, data_type: str):
        # Находим нужный класс сервиса
        service_class = SERVICE_MAP.get(domain)
        if not service_class:
            raise ValueError(f"Домен '{domain}' не найден.")

        # Находим нужное имя метода
        method_name = METHOD_MAP.get(data_type)
        if not method_name:
            raise ValueError(f"Тип данных '{data_type}' не найден.")

        # Получаем сам метод из класса
        method_to_call = getattr(service_class, method_name)

        # Вызываем метод
        return method_to_call(db)
