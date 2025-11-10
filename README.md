# How to run (local)
1. Create .env with DB credentials
2. Start postgres: `docker compose -f docker/docker-compose.yml up -d`
3. Install Python deps: `pip install -r requirements.txt`
4. Put raw CSV into `data/raw/finance_raw.csv`
5. Run ETL: `python src/etl/run_etl.py`
6. Open Power BI Desktop and connect to PostgreSQL at localhost:5432, DB=finance_db




Описание проекта и цели
Источник данных (какие CSV, описание колонок)
Схема БД (ER-диаграмма или кратко)
Как локально запустить (инструкции)
Запуск Postgres (docker compose)
Настройка .env
Установка зависимостей: pip install -r requirements.txt
Запуск ETL: python src/etl/run_etl.py
Открыть Power BI Desktop и подключиться к БД
Список KPI и формулы
Что проверить (список тестов валидации)
План дальнейшего развития (опционально)
Лицензия / контакты