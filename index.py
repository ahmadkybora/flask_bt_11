from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler
from telegram import Update
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
token = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    context.bot.send_message(chat_id=chat_id, text="hello world")

def echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    message_id = update.message_id
    text = update.message.text
    context.bot.send_message(chat_id, text=text)

def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(['START', 'start'], start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()