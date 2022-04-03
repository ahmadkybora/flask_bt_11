from telegram import Update,ReplyKeyboardMarkup,ReplyKeyboardRemove,Bot,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,CallbackQuery,ParseMode
from telegram.ext import CommandHandler,Updater,Dispatcher,MessageHandler,Filters,CallbackContext,CallbackQueryHandler
import logging
# from mutagen.mp3 import MP3
# from mutagen.id3 import ID3, APIC, error

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

tkn = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"

def start(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton('شروع')],
        [KeyboardButton('درباره ما')],
        [KeyboardButton('کمک')], 
        [KeyboardButton('فایل')]
    ]
    key = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    inlineMarkup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=chat_id, 
        text="hello world", 
        # reply_to_message_id=update.effective_message.message_id,
        reply_to_message_id=inlineMarkup,
        reply_markup=inlineMarkup
    )

def main():
    updater = Updater(tkn, use_context=True)
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text,start))
    updater.start_polling()


if __name__ == '__main__':
    main()


    # keyboard = [
    #     [KeyboardButton('شروع')],
    #     [KeyboardButton('درباره ما')],
    #     [KeyboardButton('کمک')], 
    #     [KeyboardButton('فایل')]
    # ]
    # key = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)