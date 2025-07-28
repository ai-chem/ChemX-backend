from fastapi import FastAPI
from config import settings

# Создаем экземпляр приложения
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

@app.get("/")
async def root():
    return {"message": "API успешно запущен"}

# Функция для подключения всех роутеров доменов
def include_routers():
    """
    Импортирует и подключает роутеры для каждого домена данных.
    """
    # 1.  Cytotox
    from app.domains.cytotox.router import router as cytotox_router
    app.include_router(cytotox_router, prefix="/api/v1/cytotox", tags=["Cytotox"])

    # 2.  Nanomag
    from app.domains.nanomag.router import router as nanomag_router
    app.include_router(nanomag_router, prefix="/api/v1/nanomag", tags=["Nanomag"])

    # 3.  Nanozymes
    from app.domains.nanozymes.router import router as nanozymes_router
    app.include_router(nanozymes_router, prefix="/api/v1/nanozymes", tags=["Nanozymes"])

    # 4.  Seltox
    from app.domains.seltox.router import router as seltox_router
    app.include_router(seltox_router, prefix="/api/v1/seltox", tags=["Seltox"])

    # 5.  Synergy
    from app.domains.synergy.router import router as synergy_router
    app.include_router(synergy_router, prefix="/api/v1/synergy", tags=["Synergy"])


include_routers()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)