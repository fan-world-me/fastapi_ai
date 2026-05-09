# FastAPI AI Chat

FastAPI приложение для взаимодействия с AI моделями через OpenRouter API.

## Описание

Простой REST API сервис, который позволяет отправлять сообщения AI модели и получать ответы. Использует OpenRouter для доступа к различным языковым моделям.

## Возможности

- 🤖 Интеграция с OpenRouter API
- 💬 Endpoint для чата с AI
- ⚡ Асинхронная обработка запросов
- 🔒 Безопасное хранение API ключей через переменные окружения

## Технологии

- **FastAPI** - современный веб-фреймворк для создания API
- **Pydantic** - валидация данных
- **httpx** - асинхронный HTTP клиент
- **python-dotenv** - управление переменными окружения
- **uvicorn** - ASGI сервер

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/fan-world/fastapi_ai.git
cd fastapi_ai
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install fastapi uvicorn httpx python-dotenv pydantic
```

5. Создайте файл `.env` в корне проекта:
```env
OPENROUTER_API_KEY=your_api_key_here
```

## Использование

1. Запустите сервер:
```bash
python main.py
```

2. Сервер будет доступен по адресу: `http://localhost:8000`

3. Отправьте POST запрос на `/chat`:
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Привет, как дела?"}'
```

4. Интерактивная документация API доступна по адресу:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Структура проекта

```
fastapi_ai/
├── crud/
│   └── crud.py          # Логика взаимодействия с OpenRouter API
├── models/
│   └── models.py        # Pydantic модели для валидации данных
├── routers/
│   └── router.py        # API endpoints
├── main.py              # Точка входа приложения
├── .env                 # Переменные окружения (не в git)
├── .env.example         # Пример файла с переменными окружения
├── .gitignore           # Игнорируемые файлы
└── README.md            # Документация
```

## API Endpoints

### POST /chat

Отправка сообщения AI модели.

**Request Body:**
```json
{
  "message": "Ваше сообщение"
}
```

**Response:**
```json
{
  "Ответ": "Ответ от AI модели"
}
```

## Получение API ключа

1. Зарегистрируйтесь на [OpenRouter](https://openrouter.ai/)
2. Получите API ключ в личном кабинете
3. Добавьте ключ в файл `.env`

## Лицензия

MIT License - см. файл [LICENSE](LICENSE)

## Автор

[fan-world](https://github.com/fan-world)
