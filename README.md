[![Telegram](https://img.shields.io/badge/Telegram-@fan__world__me-2CA5E0?style=flat-square&logo=telegram)](https://t.me/fan_world_me)   [![Discord](https://img.shields.io/badge/Discord-fan__world__me-5865F2?style=flat-square&logo=discord)](https://discord.com/users/1040301536036786248)   [![GitHub](https://img.shields.io/badge/GitHub-fan--world--me-181717?style=flat-square&logo=github)](https://github.com/fan-world-me)   [![Portfolio](https://img.shields.io/badge/Portfolio-fan--world--me.github.io-00e5ff?style=flat-square&logo=githubpages&logoColor=white)](https://fan-world-me.github.io/)

# FastAPI AI Chat

FastAPI приложение для взаимодействия с AI моделями через OpenRouter API. Простой REST API сервис, который позволяет отправлять сообщения AI модели и получать ответы. Использует OpenRouter для доступа к разным языковым моделям.

### 💭 Возможности

- 🤖 **Интеграция с OpenRouter API**
- 💬 **Endpoint для чата с AI**
- ⚡ **Асинхронная обработка запросов**
- 🔒 **Безопасное хранение API ключей** через переменные окружения

---

### 🧰 Технологии

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-validation-E92063?style=flat-square&logo=pydantic&logoColor=white)
![httpx](https://img.shields.io/badge/httpx-async-00b4d8?style=flat-square)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-499848?style=flat-square)
![OpenRouter](https://img.shields.io/badge/OpenRouter-API-6B21A8?style=flat-square)

| Библиотека | Назначение |
|---|---|
| **FastAPI** | современный веб-фреймворк для создания API |
| **Pydantic** | валидация данных |
| **httpx** | асинхронный HTTP клиент |
| **python-dotenv** | управление переменными окружения |
| **uvicorn** | ASGI сервер |

---

### 🗂️ Структура проекта

```
fastapi_ai/
├── crud/
│   └── crud.py          — логика взаимодействия с OpenRouter API
├── models/
│   └── models.py        — Pydantic модели для валидации данных
├── routers/
│   └── router.py        — API endpoints
├── main.py              — точка входа приложения
├── .env                 — переменные окружения (не в git)
├── .env.example         — пример файла с переменными окружения
├── .gitignore
└── README.md
```

---

### 🔧 Установка

**1. Клонируйте репозиторий**

```bash
git clone https://github.com/fan-world-me/fastapi_ai.git
cd fastapi_ai
```

**2. Создайте виртуальное окружение**

```bash
python -m venv venv
```

**3. Активируйте виртуальное окружение**

```bash
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
```

**4. Установите зависимости**

```bash
pip install fastapi uvicorn httpx python-dotenv pydantic
```

**5. Создайте файл `.env` в корне проекта**

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

### 🚀 Использование

**1. Запустите сервер**

```bash
python main.py
```

Сервер будет доступен по адресу: `http://localhost:8000`

**2. Отправьте POST запрос на `/chat`**

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Привет, как дела?"}'
```

**3. Интерактивная документация API**

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

### 🔌 API Endpoints

**POST `/chat`** — отправка сообщения AI модели.

Request body:

```json
{
  "message": "Ваше сообщение"
}
```

Response:

```json
{
  "Ответ": "Ответ от AI модели"
}
```

---

### 🔑 Получение API ключа

1. Зарегистрируйтесь на [OpenRouter](https://openrouter.ai/)
2. Получите API ключ в личном кабинете
3. Добавьте ключ в файл `.env`

---

### 📄 Лицензия

MIT License — см. файл [LICENSE](LICENSE) © [fan-world-me](https://github.com/fan-world-me)

---

Made with 🩵 in Ukraine 🇺🇦

[![Telegram](https://img.shields.io/badge/Telegram-@fan__world__me-2CA5E0?style=flat-square&logo=telegram)](https://t.me/fan_world_me)   [![Discord](https://img.shields.io/badge/Discord-fan__world__me-5865F2?style=flat-square&logo=discord)](https://discord.com/users/1040301536036786248)   [![Portfolio](https://img.shields.io/badge/Portfolio-fan--world--me.github.io-00e5ff?style=flat-square&logo=githubpages&logoColor=white)](https://fan-world-me.github.io/)
