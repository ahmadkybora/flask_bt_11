from telegram import Update, Bot, CallbackQuery, ParseMode
from telegram.ext import CommandHandler, Updater, Dispatcher, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telegram import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton, 
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove, 
    KeyboardButton
)
import logging
# from mutagen.mp3 import MP3
# from mutagen.id3 import ID3, APIC, error

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

tkn = "2016260844:AAGwWwI6ZLA7cLUNNcAbbFz2W84wkJebZyo"

menuInline = [
   [InlineKeyboardButton('1', callback_data='1'), InlineKeyboardButton('2', callback_data='1')], 
   [InlineKeyboardButton('شس', callback_data='1'), InlineKeyboardButton('4', callback_data='1')], 
   [InlineKeyboardButton('شس', callback_data='1'), InlineKeyboardButton('4', callback_data='1')], 
]

first_name = [InlineKeyboardButton('نام', callback_data='1')]
last_name = [InlineKeyboardButton('نام خانوادگی', callback_data='1')]

keyboard = [
    [KeyboardButton('شروع')],
    [KeyboardButton('درباره ما')],
    [KeyboardButton('کمک')], 
    [KeyboardButton('فایل')], 
    [KeyboardButton('ثبت نام')],
    [KeyboardButton('سکه')]
]

def start(update: Update, context: CallbackContext):
    txt = update.effective_message.text

    if txt == "ثبت نام":
        first_nameMarkup = InlineKeyboardMarkup(first_name)
        update.message.reply_text("انتخاب کنید", reply_markup=first_nameMarkup)

    elif txt == "سکه":
        inlineMarkup = InlineKeyboardMarkup(menuInline)
        update.message.reply_text("انتخاب کنید", reply_markup=inlineMarkup)

    elif txt == "درباره ما":
        context.bot.send_message(
            chat_id=update.message.chat_id, 
            text="hello world"
        )

    else:
        key = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(
            chat_id=update.message.chat_id, 
            text="hello world", 
            reply_markup=key
        )

# def s(update: Update, context: CallbackContext):
#     key = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
#     chat_id = update.message.chat_id
#     message_id = update.message.message_id
#     # inlineMarkup = InlineKeyboardMarkup(keyboard)
#     context.bot.send_message(
#         chat_id=chat_id, 
#         text="hello world", 
#         # reply_to_message_id=update.effective_message.message_id,
#         # reply_to_message_id=inlineMarkup,
#         # reply_markup=key
#     )
    # inlineMarkup = InlineKeyboardMarkup(keyboard)
    # update.message.reply_text("hello", reply_markup=inlineMarkup)

# def register(update: Update, context: CallbackContext):
#     first_nameMarkup = InlineKeyboardMarkup(first_name)
#     update.message.reply_text("انتخاب کنید", reply_markup=first_nameMarkup)

# def menu(update: Update, context: CallbackContext):
#     inlineMarkup = InlineKeyboardMarkup(menuInline)
#     update.message.reply_text("انتخاب کنید", reply_markup=inlineMarkup)

# def coin(update: Update, context: CallbackContext):
#     inlineMarkup = InlineKeyboardMarkup(menuInline)
#     update.message.reply_text("انتخاب کنید", reply_markup=inlineMarkup)

# def aboutUs(update: Update, context: CallbackContext):
#         context.bot.send_message(
#         chat_id=update.message.chat_id, 
#         text="aboutUs", 
#     )

# def inline_reply(update: Update, context: CallbackContext):
#     inlineMarkup = InlineKeyboardMarkup(inlineKeys)
#     update.message.reply_text("انتخاب کنید", reply_markup=inlineMarkup)

def main():
    updater = Updater(tkn, use_context=True)
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', start))
    # dispatcher.add_handler(CommandHandler('s', inline_reply))
    dispatcher.add_handler(MessageHandler(Filters.text, start))
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