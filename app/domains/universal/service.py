# app/domains/universal/service.py
from sqlalchemy.orm import Session

from app.domains.common.service_map import METHOD_MAP
from app.domains.common.service_map import SERVICE_MAP


class UniversalDataService:
    @staticmethod
    def get_data(
        db: Session, domain: str, data_type: str, nanoparticle: str | None = None
    ):
        service_class = SERVICE_MAP.get(domain)
        if not service_class:
            raise ValueError(f"Домен '{domain}' не найден.")

        method_name = METHOD_MAP.get(data_type)
        if not method_name:
            raise ValueError(f"Тип данных '{data_type}' не найден.")

        method_to_call = getattr(service_class, method_name)
        # Мы передаем nanoparticle только если тип данных all_data,
        if data_type == "all_data":
            return method_to_call(db=db, nanoparticle=nanoparticle)
        else:
            # Для всех остальных типов просто вызываем метод без фильтра
            return method_to_call(db=db)
