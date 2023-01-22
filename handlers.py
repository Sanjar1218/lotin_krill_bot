from functions import (
    start,
    echo,
)
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import logging
from decouple import config

TOKEN = config('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT, echo))
    
    application.run_polling()