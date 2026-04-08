# Omniscient-NLP-Agent 🤖

**Omniscient-NLP-Agent** — полностью готовый AI/NLP проект с поддержкой LLM, RAG поиска, асинхронных задач, интеграций и Streamlit дашборда. Идеален для демонстрации навыков в AI, NLP, embeddings, Docker и CI/CD.

---

## 🚀 Основной функционал

- FastAPI backend с асинхронной обработкой запросов
- RAG поиск с FAISS или Qdrant
- LLM генерация через HuggingFace Transformers с поддержкой LoRA/PEFT
- Streamlit дашборд для мониторинга запросов и метрик модели
- Интеграции: Slack, Email, Web Scraping (заглушки)
- Docker Compose для локального и production запуска
- GitHub Actions CI/CD для автоматической сборки, тестирования и деплоя

---

## ⚡ Быстрый старт

1. **Склонировать репозиторий**

```bash
git clone https://github.com/Nersisiian/Omniscient-NLP-Agent.git
cd Omniscient-NLP-Agent
Запуск через Docker Compose
docker-compose up --build
FastAPI backend: http://localhost:8000
Streamlit дашборд: http://localhost:8501
Запуск локально без Docker
Backend:
uvicorn api.main:app --reload
Streamlit:
streamlit run dashboard/dashboard.py
🧪 Тестирование
pytest tests/
🔧 Конфигурация

Все ключевые параметры находятся в core/config.py:

VECTOR_DB_PATH — путь к FAISS или Qdrant базе
LLM_MODEL — модель LLM (HuggingFace)
API_KEY — ключ для API
LOG_LEVEL — уровень логирования
📈 CI/CD (GitHub Actions)
Автоматическая сборка и тестирование при push/pull request на main
Сборка Docker контейнеров и их запуск
Проверка корректности тестов перед деплоем
💡 Возможности для расширения
Подключение реальных источников данных (PDF, Email, веб)
Настройка LoRA/PEFT для тонкой настройки LLM
Расширение интеграций (Slack, Telegram, REST API)
Улучшение визуализации метрик модели
Настройка продвинутой RAG системы с Qdrant
📌 Лицензия

MIT License

🔗 Контакты
GitHub: https://github.com/Nersisiian
Email: nersisyangrish13@gmail.com