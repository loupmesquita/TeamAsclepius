import telepot
from telepot.loop import MessageLoop

# This script is used to send a message to Telegram Bot
# by using bot's token to access HTTP API through telepot framework. 
# It is configurable to change recipient by setting up recipient's chatId 

chat_id = '424668716'
bots_token = '5937162638:AAGBic7LwaqMrd33C75_WZ53ucgVJlKx4Bg'

# Bot sends notifications to the recipient
def send_telegram_message(message: str):
    telegram_bot.sendMessage(chat_id, message)
    
# Bot sends notification to the recipient only once
def send_telegram_message_once(message: str):
    global notification_sent
    if notification_sent is False:
        notification_sent = True
        send_telegram_message(message)

# Flag for send_telegram_message_once function to indicate that function
# was not executed
notification_sent = False    
    
# Initialization of the bot through telepot's framework function Bot
# that takes bot's token as an argument
telegram_bot = telepot.Bot(bots_token)
