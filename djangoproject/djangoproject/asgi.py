
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')

application = get_asgi_application()

# Iniciar o bot do Telegram
from telegram_bot.bot import iniciar_bot
import threading

bot_thread = threading.Thread(target=iniciar_bot)
bot_thread.start()

