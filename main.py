import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

load_dotenv()

telegram_token = os.environ.get('TELEGRAM_TOKEN')
api_key = os.environ.get('API_KEY')

STATE1 = 1
STATE2 = 2


def start(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    update.message.reply_html(
        f"Привет, {user.mention_html()}!"
    )
    return STATE1


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main() -> None:
    updater = Updater(api_key)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
