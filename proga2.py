import urllib.request
import json
import telebot
from telebot import types

bot = telebot.TeleBot('603748878:AAFr7IObpLkEbfcL1zz6yQj_NMQon6zlDBc')
google_place_key = 'AIzaSyAIS-Ne_wcIMqCYD7LcHKgdErJdRKYxJz0'

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

    msg = ''

    query ='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(cur_lat) + ',' + str(cur_long) +  '&radius=500&type=bus_station&key=' + google_place_key
    response = urllib.request.urlopen(query)
    data = json.loads(response.read().decode('utf-8'))
    for result in data['results']:
        msg = msg + result['name'] + '\n'
    bot.send_message(message.chat.id, msg)



bot.polling()
