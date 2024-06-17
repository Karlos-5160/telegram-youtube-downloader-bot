import os
import requests

TOKEN = os.getenv('TOKEN')
URL = 'https://telegram-youtube-downloader-bot.onrender.com'

if TOKEN:
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={URL}')
    print(response.json())
else:
    print('Telegram bot token not found. Set TELEGRAM_BOT_TOKEN environment variable.')
