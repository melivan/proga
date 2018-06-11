import telebot
from telebot import types

bot = telebot.TeleBot('603748878:AAFr7IObpLkEbfcL1zz6yQj_NMQon6zlDBc')

stations = [{
    'name': 'Universitet',
    'lat1': 59.879963,
    'long1': 29.821120,
    'lat2': 59.882526,
    'long2': 29.834124,
    'buses': [210, 352, 354, 358, 359]
    },{
    'name': 'Botanicheskaya',
    'lat1': 59.876528,
    'long1': 29.816574,
    'lat2': 59.880195,
    'long2': 29.831135,
    'buses': [210, 352, 358, 359]
    },{
    'name': 'Rectorskiy pr.',
    'lat1': 59.874662,
    'long1': 29.823675,
    'lat2': 59.878194,
    'long2': 29.835971,
    'buses': [210, 358, 359]
     },{
    'name': 'Pravlenskaya',
    'lat1': 59.878886,
    'long1': 29.903715,
    'lat2': 59.881536,
    'long2': 29.913790,
    'buses': [200, 210, 344, 348, 350, 356, 359]
     },{
    'name': 'Prigorodnaya',
    'lat1': 59.881504,
    'long1': 29.828184,
    'lat2': 59.884196,
    'long2': 29.841166,
    'buses': [354]
    }
]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi, I can find needed bus for you.\nType /find for share your location")

@bot.message_handler(commands=['find'])
def send_get_location_button(message):
    get_location_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    get_location_markup.add(
        types.KeyboardButton('Share location', request_location=True)
    )
    bot.send_message(message.chat.id, 'Please, share me you location', reply_markup=get_location_markup)

@bot.message_handler(content_types=['location'])
def handle_location(message):
    print(message.location)
    cur_lat = message.location.latitude
    cur_long = message.location.longitude
    result = ""
    for station in stations:
        if (station['lat1'] <= cur_lat and cur_lat <= station['lat2'] and station['long1'] <= cur_long and cur_long <= station['long2']):
            result += "Buses from station '" + station['name'] + "': " + ','.join(map(str, station['buses'])) + '\n'
    bot.send_message(message.chat.id, str(result))


bot.polling()
