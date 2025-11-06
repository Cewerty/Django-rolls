# STAGE 1: Сборка (builder stage)
FROM python:3.12-slim AS builder

# Устанавливаем системные зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    musl-dev \
    libsqlite3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем UV
RUN pip install uv==0.9.7

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml uv.lock ./

# Создаем виртуальное окружение и устанавливаем зависимости
RUN uv venv .venv && \
    . .venv/bin/activate && \
    uv sync --no-cache-dir --no-dev

# Копируем всё приложение
COPY . .

# Собираем статические файлы (делаем это в builder stage!)
RUN . .venv/bin/activate && \
    python manage.py collectstatic --noinput --clear


# STAGE 2: Финальный образ
FROM python:3.12-slim AS final

# Устанавливаем минимальные зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаем непривилегированного пользователя
RUN addgroup --system django && \
    adduser --system --ingroup django django

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только необходимые артефакты из builder stage
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/staticfiles /app/staticfiles
COPY --from=builder /app/db.sqlite3 /app/db.sqlite3
COPY --from=builder /app/manage.py /app/
COPY --from=builder /app/project /app/project/
COPY --from=builder /app/dice /app/dice/
COPY --from=builder /app/static /app/static/

# Устанавливаем правильные права доступа
RUN chown -R django:django /app && \
    find /app -type d -exec chmod 755 {} \; && \
    find /app -type f -exec chmod 644 {} \; && \
    chmod +x /app/.venv/bin/*

# Переключаемся на непривилегированного пользователя
USER django

# Экспонируем порт
EXPOSE 8000

# Команда для запуска
CMD ["/app/.venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
