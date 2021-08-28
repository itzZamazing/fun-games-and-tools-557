from telegram.ext import *
import random
a=0
z=0
api_key="1975202016:AAEZg2uYX252aDXxVNB6lMUHT_RcResHM1E"

def start_command(update,context):
    update.message.reply_text("type /help for help")

def help_command(update,context):
    update.message.reply_text(" welcome to fun games and tools 557 \n \n for heads or tails: /heads_or_tails \n \n for chosing a random name use: /random \n \n for playing guessing number use: /guessing_number \n \n for playing rock paper scissors use: /rps")

def handle_message(update,context):
    global a
    text=str(update.message.text)
    if a==1:
        response_text=random_response(text)
        update.message.reply_text(response_text)
    if a==2:
        response_text=heads_or_tails_response(text)
        update.message.reply_text(response_text)
    if a==3:
        response_text=rps_response(text)
        update.message.reply_text(response_text)
    if a==4:
        response_text=guessing_number_response(text)
        update.message.reply_text(response_text)
def random_command(update,context,):
    global a
    a=1
    update.message.reply_text("type a list of names")

def heads_or_tails_command(update,context,):
    global a
    a=2
    update.message.reply_text("heads or tails ?")

def rps_command(update,context,):
    global a
    
    a=3
    
    update.message.reply_text("ready? rock paper scissors")

def guessing_number_command(update,context,):
    global a
    global z
    a=4
    z=random.randint(1,99)
    update.message.reply_text("guess a number from 1 to 99")
    

def random_response(text_input):
    user_message = str(text_input)
    b=[str(x)for x in user_message.split(" ")]
    c=random.randint(0,len(b)-1)
    return b[c]

def heads_or_tails_response(text_input):
    user_message = str(text_input)
    b=random.randint(0,1)
    c="tails"
    if b==1:
        c="heads"
    print(user_message)
    d="haha I win you lose it was"+" "+c
    if user_message==c:
        d="you win I lose it was"+" "+c
    return d

def rps_response(text_input):
    n = str(text_input)
    paper_lst=['rock','paper','scissors']
    paper_rd = paper_lst[random.randint(0,2)]
    if paper_rd == paper_lst[0] and n == 'rock' :
        return 'draw!'
    if paper_rd == paper_lst[0] and n == 'paper' :
        return'you lose!'
    if paper_rd == paper_lst[0] and n == 'scissors' :
        return'you win!'
    if paper_rd == paper_lst[1] and n == 'rock' :
        return'you lose!'
    if paper_rd == paper_lst[1] and n == 'paper' :
        return'draw!'
    if paper_rd == paper_lst[1] and n == 'scissors' :
        return'you win!'
    if paper_rd == paper_lst[2] and n == 'rock' :
        return'you win!'
    if paper_rd == paper_lst[2] and n == 'paper' :
        return'you lose!'
    if paper_rd == paper_lst[2] and n == 'scissors' :
        return'draw!'
    else:
        return "I dont understand you"

def guessing_number_response(text_input):
    global z
    user_message = int(str(text_input))
    if user_message>z:
        return "smaller number"
    if user_message<z:
        return "bigger number"
    else:
        c="yes you guessed right my number was "+ str(z)
        return c

updater=Updater(api_key,use_context=True)
dp=updater.dispatcher

dp.add_handler(CommandHandler("start",start_command))
dp.add_handler(CommandHandler("help",help_command))
dp.add_handler(CommandHandler("random",random_command))
dp.add_handler(CommandHandler("heads_or_tails",heads_or_tails_command))
dp.add_handler(CommandHandler("rps",rps_command))
dp.add_handler(CommandHandler("guessing_number",guessing_number_command))
dp.add_handler(MessageHandler(Filters.text,handle_message))

updater.start_polling()
updater.idle()
