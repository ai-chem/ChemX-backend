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
    from app.api.v1.cytotox.router import router as cytotox_router
    app.include_router(cytotox_router, prefix="/api/v1/cytotox", tags=["Cytotox"])

# Подключаем роутеры
include_routers()

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)