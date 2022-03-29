from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CommandHandler
from telegram import Update
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
token = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"

def start(update: Update, context: CallbackContext):
    update.message.reply_text('start!')

def help(update: Update, context: CallbackContext):
    update.message.reply_text('help')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()