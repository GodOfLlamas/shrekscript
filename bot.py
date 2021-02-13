import telebot
import time
import os

token = os.environ.get('TOKEN')

bot = telebot.TeleBot(str(token))

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('/Шрек_1', '/Шрек_2', '/Шрек_3', '/Шрек_4')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, мои огрята', reply_markup=keyboard1)


@bot.message_handler(commands=['Шрек_1'])
def shrek_1_message(message):
    with open('shrek_1.txt', encoding='utf-8') as f:
        text = f.read()
        for line in text.splitlines():
            time.sleep(.18)
            if(line == '' or line == '\n'):
                bot.send_message(message.chat.id, '_______________________________________________')
            else:
                 bot.send_message(message.chat.id, line[:400])



@bot.message_handler(commands=['Шрек_2'])
def shrek_2_message(message):
    with open('shrek_2.txt', encoding='utf-8') as f:
        text = f.read()
        for line in text.splitlines():
            time.sleep(.18)
            if(line == ''or line == '\n'):
                bot.send_message(message.chat.id, '_______________________________________________')
            else:
                 bot.send_message(message.chat.id, line[:400])



@bot.message_handler(commands=['Шрек_3'])
def shrek_3_message(message):
    with open('shrek_3.txt', encoding='utf-8') as f:
        text = f.read()
        for line in text.splitlines():
            time.sleep(.18)
            if(line == ''or line == '\n'):
                bot.send_message(message.chat.id, '_______________________________________________')
            else:
                 bot.send_message(message.chat.id, line[:400])



@bot.message_handler(commands=['Шрек_4'])
def shrek_4_message(message):
    with open('shrek_4.txt', encoding='utf-8') as f:
        text = f.read()
        for line in text.splitlines():
            time.sleep(.18)
            if(line == ''or line == '\n'):
                bot.send_message(message.chat.id, '_______________________________________________')
            else:
                 bot.send_message(message.chat.id, line[:400])



@bot.message_handler(commands=['onion'])
def onion_message(message):
    bot.send_message(message.chat.id,
                    '— К твоему сведению, великаны не так просты как кажутся!\n'       
                    '— Приведи пример\n'      
                    '— Пример? Изволь. Великаны — как луковицы.\n'        
                    '— Воняют?\n'       
                    '— Да нет!\n'       
                    '— Доводят до слёз?\n'      
                    '— Нет.\n'     
                    '— Наверное чернеют и скукоживаются на солнце?\n'       
                    '— Нет! Многослойность! Лук многослоен! Я тоже! Слой за слоем. Ты усёк? Мы многослойные!\n'     
                    '— А-а-а! Оба многослойные... Только не все любят лук!... Торт! Все любят тортики! Слоёные!\n'      
                    '— Мне плевать на мещанские вкусы! Великаны не тортики!\n')


bot.polling()

