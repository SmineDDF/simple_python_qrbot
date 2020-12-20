from telebot import TeleBot, types
import qr_api
import barcode_api
import ascii_api
from utils import get_message_text, remove_command

token = open('token', mode='r').read()
bot = TeleBot(token)

help_msg = """`/help` to see this message
`/ascii <message>` to create an ascii art of your message
`/barcode <message>` to encode your message as a barcode
`<message>` to encode your message as a QR-code"""

@bot.message_handler(commands=['start'])
def reply_start(message):
    keyboard = types.InlineKeyboardMarkup()
    key_help = types.InlineKeyboardButton(text='Help', callback_data='/help')
    keyboard.add(key_help)
    bot.send_message(message.chat.id, text='Press me', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_help(call):
    if call.data == '/help':
        bot.send_message(call.message.chat.id, help_msg, parse_mode='markdown')

@bot.message_handler(commands=['help'])
def reply_help(message):
    bot.send_message(message.chat.id, help_msg, parse_mode='markdown')

@bot.message_handler(commands=['ascii'])
def reply_ascii(message):
    message_text = get_message_text(remove_command(message.text))

    if message_text == '':
        return bot.reply_to(message, "Send me something other than spaces")

    ascii_art = ascii_api.get_ascii_text(message_text)
    ascii_art_md = '```\n' + ascii_art + '\n```' # if sent as-is, telegram screws up whitespaces and "image" returns corrupted
    bot.send_message(message.chat.id, ascii_art_md, parse_mode='markdown')

@bot.message_handler(commands=['barcode'])
def reply_barcode(message):
    message_text = get_message_text(remove_command(message.text))

    if message_text == '':
        return bot.reply_to(message, "Send me something other than spaces")

    barcode_image = barcode_api.get_barcode_image_url_for_text(message_text)
    bot.send_photo(message.chat.id, barcode_image)

@bot.message_handler()
def reply_default(message):
    message_text = get_message_text(message.text)

    if message_text == '':
        return bot.reply_to(message, "Send me something other than spaces")

    qr_image_url = qr_api.get_qr_image_url_for_string(message_text)
    bot.send_photo(message.chat.id, qr_image_url)


bot.polling()