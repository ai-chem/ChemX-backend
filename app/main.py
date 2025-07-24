from fastapi import FastAPI
from app.config import settings

# Создаем экземпляр нашего приложения
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Корневой эндпоинт для проверки "здоровья" API
@app.get("/")
async def root():
    return {"message": "API успешно запущен"}

# Функция для подключения всех роутеров доменов
def include_routers():
    """
    Импортирует и подключает роутеры для каждого домена данных.
    """
    # 1. Домен Cytotox
    from app.api.v1.cytotox.router import router as cytotox_router
    app.include_router(cytotox_router, prefix="/api/v1/cytotox", tags=["Cytotox"])

    # 2. Домен Nanomag
    from app.api.v1.nanomag.router import router as nanomag_router
    app.include_router(nanomag_router, prefix="/api/v1/nanomag", tags=["Nanomag"])

    # 3. Домен Nanozymes
    from app.api.v1.nanozymes.router import router as nanozymes_router
    app.include_router(nanozymes_router, prefix="/api/v1/nanozymes", tags=["Nanozymes"])

    # 4. Домен Seltox
    from app.api.v1.seltox.router import router as seltox_router
    app.include_router(seltox_router, prefix="/api/v1/seltox", tags=["Seltox"])

    # 5. Домен Synergy
    from app.api.v1.synergy.router import router as synergy_router
    app.include_router(synergy_router, prefix="/api/v1/synergy", tags=["Synergy"])


# Вызываем функцию, чтобы регистрации действительно произошли при старте
include_routers()

# Блок для локального запуска через 'python app/main.py'
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)