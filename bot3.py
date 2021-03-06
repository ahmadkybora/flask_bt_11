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
updater = Updater(tkn, use_context=True)
bot = Bot(tkn)
dispatcher : Dispatcher = updater.dispatcher

def start(update:Update, context:CallbackContext):
    # file = context.bot.get_file(update.message.document.file_id)
    # file.download(update.message.document.file_name)
    # doc = update.message.document

    firstname = update.effective_message.from_user.first_name
    chtiD = update.effective_message.chat_id
    username = update.effective_message.from_user.username
    txt = update.effective_message.text
    file = context.bot.sendPhoto(update.effective_chat.id, "https://fr.dreamstime.com/photo-stock-paysage-panoramique-d-automne-courant-for%C3%AAt-backg-nature-chute-image79856609")
   
    menuInline = [
        [InlineKeyboardButton('ثبت نام'), InlineKeyboardButton("درباره ما")], 
        [InlineKeyboardButton('سکه'), InlineKeyboardButton('4')], 
        [InlineKeyboardButton('5'), InlineKeyboardButton('2')], 
    ]

    first_name = [InlineKeyboardButton('نام')]
    last_name = [InlineKeyboardButton('نام خانوادگی')]
    
    # اینجا یک متغییر تعریف کردیم برای ساخت دکمه شیشه ای
    # زمانی که کاربر بر روی هر کدام از دکمه های زیر کلیک میکن
    # متن داخل بعنوان یک تکست برای ربات ارسال شده و شرط مورد نظر 
    # انجام میشود
    keyboard = [
        [KeyboardButton('شروع')],
        [KeyboardButton('درباره ما')],
        [KeyboardButton('کمک')], 
        [KeyboardButton('فایل')], 
        [KeyboardButton('ثبت نام')], 
    ]
    key = ReplyKeyboardMarkup(keyboard,resize_keyboard=True)

    if txt == "درباره ما":
        bot.send_message(
            chat_id = chtiD,
            text = "سلام حالتون چطوره", 
            reply_to_message_id=update.effective_message.message_id,
        )
    elif txt == "ثبت نام":
        first_nameMarkup = InlineKeyboardMarkup(first_name)
        update.message.reply_text("وارد کنید", reply_markup=first_nameMarkup)
    elif txt == "کمک":
        bot.send_message(
            chat_id = chtiD,
            text="How to Deploy Your Telegram bot on Heroku\n\nچگونه ربات خود را در Heroku راه اندازی کنید",
            reply_to_message_id=update.effective_message.message_id,
        )
    elif txt == "شروع":
        bot.send_message(
            chat_id = chtiD,
            text="<u>سلام</u>\n\n<i>Telegram : </i>خوبی",
            reply_to_message_id=update.effective_message.message_id,
            parse_mode=ParseMode.HTML
        )
    elif txt == "فایل":
        bot.send_message(
            chat_id = chtiD,
            text="فایل در حال دانلود است" + f"\n\n {file}",
            reply_to_message_id=update.effective_message.message_id,
        )
    # elif txt == "File":
    #     bot.send_message(
    #         chat_id = chtiD,
    #         text = f"{file}",
    #         reply_to_message_id=update.effective_message.message_id,
    #     )
    else:
        bot.send_message(
            chat_id=chtiD,
            text=f"نام کاربری شما {firstname}" + f"\n\nیوزرنیم شما : {username}" + f"\n\nآیدی عددی شما : {str(chtiD)}" + "سلام مصطفی حالت چطوره",
            reply_to_message_id=update.effective_message.message_id,
            reply_markup=key


        )

def main():

    # برای مدیریت پیام های غیر دستوری از کلاس
    # MessageHandler
    # استفاده میکنیم منظور پیام هایی که بتعرفشان نکردیم
    dispatcher.add_handler(MessageHandler(Filters.text,start))

    # متد زیر برای ران کردن بات است
    updater.start_polling()


if __name__ == '__main__':
    main()