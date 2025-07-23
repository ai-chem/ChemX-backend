from fastapi import APIRouter
from app.api.v1.cytotox.endpoints import get_cytotox_data, get_all_cytotox_data

router = APIRouter()

# Регистрация эндпоинта
router.add_api_route(
    "/data",
    get_cytotox_data,
    methods=["GET"],
    response_model_exclude_none=True,
    summary="Получить данные цитотоксичности",
    description="Получает данные из витрины cytotox с пагинацией"
)

# --- !!! НАША НОВАЯ РЕГИСТРАЦИЯ !!! ---
# Выбираем новый путь, чтобы не было конфликта. `/data/all` - хороший вариант.
# Полный путь будет: /api/v1/cytotox/data/all
router.add_api_route(
    "/data/all",
    get_all_cytotox_data, # Указываем новую функцию-обработчик
    methods=["GET"],
    response_model_exclude_none=True,
    summary="Получить ВСЕ данные цитотоксичности",
    description="Получает все записи из витрины cytotox. Внимание: может вызвать высокую нагрузку!"
)