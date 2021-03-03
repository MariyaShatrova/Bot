from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


TOKEN = '1596276807:AAGcB3USk4YDLmAu7N3-WAinTBYEV37CBzk'


def main():
    updater = Updater(token=TOKEN) # объект, который ловит сообщения от Telegrama

    dispather = updater.dispatcher

    handler = MessageHandler(Filters.all, do_echo)
    start_handler = CommandHandler('start', do_start)
    help_handler = CommandHandler('help', do_help)

    dispather.add_handler(start_handler)
    dispather.add_handler(help_handler)
    dispather.add_handler(handler)
    updater.start_polling()
    updater.idle()


def do_echo(update, context):
    update.message.reply_text(text='what do you need?')


def do_start(update, context):
    update.message.reply_text(text='what is your name?')


def do_help(update: Update, context):
    user_id = update.message.from_user.id
    name = update.message.from_user.first_name
    update.message.reply_text(text=f'Hi, {name}!\n Your user_id: {user_id}\n how can I help you?')


main()
