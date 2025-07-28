from pydantic import BaseModel


class Settings(BaseModel):
    # Настройки базы данных
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "ChemX"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "1321122Ar"

    # Настройки приложения
    APP_NAME: str = "ChemX Data API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Формирование строки подключения
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


# Создаём экземпляр настроек для использования в других модулях
settings = Settings()