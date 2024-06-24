from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Ваш токен от BotFather
TOKEN = '7231223578:AAF6MkfFCZ8qPHikD8NPEGzMieOTm8XUH_A'

# URL вашего веб-приложения
WEB_APP_URL = 'https://shansennn.github.io/'

def start(update: Update, context: CallbackContext) -> None:
    # Создаем кнопку с ссылкой на Web App
    keyboard = [
        [InlineKeyboardButton("Open Web App", url=WEB_APP_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    update.message.reply_text('Click the button below to open the Web App.', reply_markup=reply_markup)

def main() -> None:
    # Создаем объект Updater и передаем ему токен вашего бота
    updater = Updater(TOKEN)

    # Получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчик для команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()

    # Работаем до тех пор, пока не будет нажата комбинация клавиш Ctrl-C или получен сигнал SIGINT, SIGTERM или SIGABRT.
    updater.idle()

if __name__ == '__main__':
    main()