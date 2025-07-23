from sqlalchemy import Column, Integer, String, Float, Boolean, BigInteger, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base


class CytotoxData(Base):
    """ORM модель для витрины данных цитотоксичности"""

    __tablename__ = "serving_all_data_cytotox"
    __table_args__ = {"schema": "dbt_serving"}

    # Определяем только первичный ключ, т.к. будем использовать динамический выбор полей
    serial_number = Column(BigInяteger, primary_key=True)

    # Остальные поля будут доступны через reflection или через прямые запросы