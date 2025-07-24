from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

@app.get("/")
async def root():
    return {"message": "API успешно запущен"}

# Импорт и подключение роутеров
def include_routers():
    # Существующие роутеры
    from app.api.v1.cytotox.router import router as cytotox_router
    app.include_router(cytotox_router, prefix="/api/v1/cytotox", tags=["Cytotox"])

    from app.api.v1.nanomag.router import router as nanomag_router
    app.include_router(nanomag_router, prefix="/api/v1/nanomag", tags=["Nanomag"])

    # Новые роутеры
    from app.api.v1.nanozymes.router import router as nanozymes_router
    app.include_router(nanozymes_router, prefix="/api/v1/nanozymes", tags=["Nanozymes"])

    from app.api.v1.seltox.router import router as seltox_router
    app.include_router(seltox_router, prefix="/api/v1/seltox", tags=["Seltox"])

    from app.api.v1.synergy.router import router as synergy_router
    app.include_router(synergy_router, prefix="/api/v1/synergy", tags=["Synergy"])



# Подключаем роутеры
include_routers()

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)