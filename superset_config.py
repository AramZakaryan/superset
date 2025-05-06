import os

# Безопасный ключ (замени на сгенерированный!)
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "replace-with-your-random-long-key")

# Разрешаем работу за прокси
ENABLE_PROXY_FIX = True

# Отключаем CSRF-защиту (если только ты не используешь авторизацию)
WTF_CSRF_ENABLED = False

# 🔓 Разрешаем iframe (встраивание дашборда на сторонние сайты)
TALISMAN_CONFIG = {
    "content_security_policy": {
        "default-src": "'self' *",
        "frame-ancestors": "*",  # позволяет встраивать на любые сайты
    },
    "force_https": False,
    "frame_options": None,  # отключаем X-Frame-Options
}
