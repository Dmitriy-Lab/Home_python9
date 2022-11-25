import telebot
import requests
import time
import random

global num
global count
count = 0
num = random.randint(1,1000)

# 5864938203:AAEVbWhBV2gBJdw0OVGN0UXVOLoDmWUoSFI
bot = telebot.TeleBot("5864938203:AAEVbWhBV2gBJdw0OVGN0UXVOLoDmWUoSFI", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def hello_user(message):

    def Calc(message):
        if '+' in message.text or '*' in message.text or '/' in message.text or '-' in message.text:
            do = str(eval(str(message.text)))
            bot.send_message(message.chat.id, f'{do}')
        else:
            bot.send_message(message.chat.id, 'Некорректный ввод')

    def Game(message):
        global num
        global count
        count +=1
        if int(message.text) > num:        
            a = bot.send_message(message.chat.id, "Число должно быть меньше!") 
            bot.register_next_step_handler(a, Game)
        elif int(message.text) < num:         
            b = bot.send_message(message.chat.id, "Число должно быть больше!") 
            bot.register_next_step_handler(b, Game)
        else:         
            bot.send_message(message.chat.id, f"Вы угадали, это число = {num}, количество попыток {count}")           



    if 'привет' in message.text.lower():
        bot.reply_to(message, "Hi, " + message.from_user.first_name)
    elif message.text.lower() == 'погода':
        r = requests.get('https://wttr.in?0T')
        bot.reply_to(message, r.text)
    elif message.text.lower() == 'котик':
        r = f'https://cataas.com/cat?t=${time.time()}'
        bot.send_photo(message.chat.id, r)
    elif message.text.lower() == 'файл':
        data = open('user_message.txt', encoding='utf-8')
        bot.send_document(message.chat.id, data)
        data.close()
    elif message.text.lower() == 'посчитай':
        r = bot.send_message(message.chat.id, 'Что будем считать?')
        bot.register_next_step_handler(r, Calc)
    elif message.text.lower() == 'играть':
        r = bot.send_message(message.chat.id, 'Я загадал число от 1 до 1000, угадывай))')
        bot.register_next_step_handler(r, Game)

    data = open('user_message.txt', 'a+', encoding='utf-8')
    data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
    data.close()

bot.infinity_polling()





