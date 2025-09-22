

# ChemX-backend

[![Статус тестов](https://github.com/ai-chem/ChemX-backend/actions/workflows/run-tests.yml/badge.svg)](https://github.com/ai-chem/ChemX-backend/actions/workflows/run-tests.yml)

Это API-сервер на Python и FastAPI, который служит проводником к базе данных PostgreSQL с данными о наноматериалах. Проект предоставляет эндпоинты для получения этих данных.

## Структура проекта

Проект имеет модульную структуру, где логика разделена по доменам данных. Это позволяет легко добавлять новые источники и эндпоинты.

```
chemx-backend/
│
├── .github/                    # Конфигурация для GitHub
│   └── workflows/
│       └── run-tests.yml       # Workflow для автоматического запуска тестов (CI)
├── .venv/                      # Папка с виртуальным окружением Python
│
├── app/                        # Корневая папка приложения FastAPI
│   ├── __init__.py             # Инициализатор пакета 'app'
│   │
│   ├── domains/                # Модули, сгруппированные по доменам данных
│   │   ├── __init__.py
│   │   │
│   │   ├── common/             # Общие, переиспользуемые компоненты
│   │   │   ├── __init__.py
│   │   │   ├── schemas.py      # Общие Pydantic-схемы
│   │   │   └── utils.py        # Общие вспомогательные функции
│   │   │
│   │   ├── cytotox/            # Модуль для домена 'cytotox'
│   │   │   ├── __init__.py
│   │   │   ├── endpoints.py    # API-контроллеры
│   │   │   ├── models.py       # Модели SQLAlchemy ORM
│   │   │   ├── router.py       # Регистрация маршрутов
│   │   │   ├── schemas.py      # Специфичные Pydantic-схемы
│   │   │   └── service.py      # Бизнес-логика
│   │   │
│   │   ├── nanomag/
│   │   │   └── ... (аналогичная структура)
│   │   │
│   │   ├── nanozymes/
│   │   │   └── ... (аналогичная структура)
│   │   │
│   │   ├── seltox/
│   │   │   └── ... (аналогичная структура)
│   │   │
│   │   └── synergy/
│   │       └── ... (аналогичная структура)
|	├── tests/ x# Папка с тестами которые потом будут в github actions
│   ├── └── test_domain_apis.py
│   │
│   ├── database.py             # Настройка подключения к базе данных
│   └── main.py                 # Главная точка входа в приложение
│
│
├── config.py                   # Глобальная конфигурация проекта
├── .gitignore                  # Файл для исключения файлов из системы контроля версий Git
├── README.md                   # Основная документация по проекту
└── requirements.txt            # Список Python-зависимостей проекта
```

## Эндпоинты API

Все эндпоинты сгруппированы по доменам. Вот примеры для домена `cytotox`:

*   `GET /api/v1/cytotox/data/all`
    - Получает все данные из витрины `cytotox`.
    - Параметры: `file_format` (`json` или `csv`), `nanoparticle` (для фильтрации).

*   `GET /api/v1/cytotox/analytics/column-stats`
    - Получает посчитанную статистику по колонкам.
    - Параметр: `file_format` (`json` или `csv`).

*   `GET /api/v1/cytotox/analytics/row-stats`
    - Получает посчитанную статистику по строкам.
    - Параметр: `file_format` (`json` или `csv`).

*   `GET /api/v1/cytotox/analytics/top-categories`
    - Получает статистику по топовым категориям.
    - Параметр: `file_format` (`json` или `csv`).

Аналогичные эндпоинты существуют и для других доменов (`nanomag`, `nanozymes` и т.д.).

> После запуска сервера полный список всех эндпоинтов и их параметров доступен по адресу [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs).

## Как запустить проект локально

1.  **Скачать репозиторий:**
    ```bash
    git clone https://github.com/ai-chem/ChemX-backend.git
    cd ChemX-backend
    ```

2.  **Установить все нужные библиотеки:**
    (Рекомендуется делать это в виртуальном окружении)
    ```bash
    pip install -r requirements.txt
    ```

3.  **Настроить подключение к базе данных:**
    Создайте в корне проекта файл с именем `.env`. Укажите свои данные для подключения к локальной базе данных.
    ```dotenv
    # .env
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=ChemX
    DB_USER=postgres
    DB_PASSWORD=ваш_пароль
    ```

4.  **Запустите сервер:**
    ```bash
    uvicorn app.main:app --reload
    ```
    Сервер будет доступен по адресу `http://127.0.0.1:8000`.

## Тестирование

Для проверки работоспособности проекта используются тесты, написанные с помощью `pytest`.
Чтобы запустить их, выполните команду в корневой папке проекта:
```bash
pytest
```

### Автоматическая проверка на GitHub

В этом репозитории настроен GitHub Actions. При попытке добавить новый код в основную ветку, он автоматически запускает все тесты для проверки, что ничего не сломалось.

Для работы этой системы в настройках репозитория на GitHub (`Settings -> Secrets`) нужно указать данные для подключения к удаленной тестовой базе данных:

*   `DB_HOST`
*   `DB_PORT`
*   `DB_NAME`
*   `DB_USER`
*   `DB_PASSWORD`
---




### The ChemX Ecosystem

This repository is the central hub for the ChemX project. The full ecosystem consists of several repositories designed to work together:

*   **[ChemX](https://github.com/ai-chem/ChemX-RAG)**: Contains 10 datasets, documentation, and code for running baseline and agentic experiments for information extraction.
*   **[ChemX-dbt](https://github.com/ai-chem/ChemX-dbt)**: Contains database models (dbt) to use ChemX datasets and build ETL pipelines.
*   **[ChemX-backend](https://github.com/ai-chem/ChemX-backend)**: Contains backend code to serve ChemX datasets via API.
*   **[ChemX-RAG](https://github.com/ai-chem/ChemX-dbt)**: Contains code to build Retrieval-Augmented Generation (RAG) applications using ChemX datasets.
*   **[ChemX-client-python](https://github.com/ai-chem/ChemX-client-python)**: Contains a Python client for accessing ChemX datasets via the API.
