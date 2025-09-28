from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

# 🔑 Твой токен (раз репозиторий будет приватным)
TOKEN = "8467384823:AAFjDlnoRZHoFjImzFh_904fY5QDTZnOzaI"

# /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("✅ Бот запущен и работает!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # команды
    dp.add_handler(CommandHandler("start", start))

    print("🤖 Бот запущен...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
