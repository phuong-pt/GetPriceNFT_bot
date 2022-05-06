import string
from telegram import Update
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os
# import urllib library
from urllib.request import urlopen
# import json
import json

urlMusk = "https://market-api.radiocaca.com/nft-sales?saleType&category=7&tokenType&token_standard=BEP721&pageNo=1&pageSize=20&sortBy=single_price&order=asc&tokenId=-1"
urlKiss = "https://market-api.radiocaca.com/nft-sales?saleType&category=20&tokenType&token_standard=BEP721&pageNo=1&pageSize=20&sortBy=single_price&order=asc&tokenId=-1"
urlCali = "https://market-api.radiocaca.com/nft-sales?saleType&category=29&tokenType&token_standard=BEP721&pageNo=1&pageSize=20&sortBy=single_price&order=asc&tokenId=-1"
urlUsm = "https://market-api.radiocaca.com/nft-sales?saleType&category=8&tokenType&token_standard=BEP721&pageNo=1&pageSize=20&sortBy=single_price&order=asc&tokenId=-1"


def start(update: Update, context: CallbackContext)-> None:
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
  
def mml(update: Update, context: CallbackContext) -> None:

    response = urlopen(urlMusk)
    data_json = json.loads(response.read())
    ouputStr = ""
    for x in range(7):
        token_id = data_json["list"][x]["token_id"]
        fixed_price = data_json["list"][x]["fixed_price"]
        ouputStr += "{:<8}" + "{:<8}" + "{:<8}" + "\n"
        ouputStr = ouputStr.format (str(x+1), token_id, fixed_price)
    ouputStrx ="7 MML có giá thấp nhất" + "\n"  +"{:<8}" +"{:<8}" +"{:<8}" + "\n"   + "=========================" + "\n" + ouputStr
    ouputStrx  = ouputStrx.format("LAND","ID","PRICE")
    update.message.reply_text( ouputStrx
        )
def cali(update: Update, context: CallbackContext) -> None:

    response = urlopen(urlCali)
    data_json = json.loads(response.read())
    ouputStr = ""
    for x in range(7):
        token_id = data_json["list"][x]["token_id"]
        fixed_price = data_json["list"][x]["fixed_price"]
        ouputStr += "{:<8}" + "{:<8}" + "{:<8}" + "\n"
        ouputStr = ouputStr.format (str(x+1), token_id, fixed_price)
    ouputStrx ="7 CALI có giá thấp nhất" + "\n"  +"{:<8}" +"{:<8}" +"{:<8}" + "\n"   + "=========================" + "\n" + ouputStr
    ouputStrx  = ouputStrx.format("LAND","ID","PRICE")
    update.message.reply_text( ouputStrx
        )
def kiss(update: Update, context: CallbackContext) -> None:

    response = urlopen(urlKiss)
    data_json = json.loads(response.read())
    ouputStr = ""
    for x in range(7):
        token_id = data_json["list"][x]["token_id"]
        fixed_price = data_json["list"][x]["fixed_price"]
        ouputStr += "{:<8}" + "{:<8}" + "{:<8}" + "\n"
        ouputStr = ouputStr.format (str(x+1), token_id, fixed_price)
    ouputStrx ="7 KISS có giá thấp nhất" + "\n"  +"{:<8}" +"{:<8}" +"{:<8}" + "\n"   + "=========================" + "\n" + ouputStr
    ouputStrx  = ouputStrx.format("LAND","ID","PRICE")
    update.message.reply_text( ouputStrx
        )

def usm(update: Update, context: CallbackContext) -> None:

    response = urlopen(urlUsm)
    data_json = json.loads(response.read())
    ouputStr = ""
    for x in range(7):
        token_id = data_json["list"][x]["token_id"]
        fixed_price = data_json["list"][x]["fixed_price"]
        ouputStr += "{:<8}" + "{:<8}" + "{:<8}" + "\n"
        ouputStr = ouputStr.format (str(x+1), token_id, fixed_price)
    ouputStrx ="7 USM có giá thấp nhất" + "\n"  +"{:<8}" +"{:<8}" +"{:<8}" + "\n"   + "=========================" + "\n" + ouputStr
    ouputStrx  = ouputStrx.format("LAND","ID","PRICE")
    update.message.reply_text( ouputStrx
        )

def land(update: Update, context: CallbackContext) -> None:
    ouputStr = ""
    x = 0
    response = urlopen(urlMusk)
    data_json = json.loads(response.read())
    token_id = data_json["list"][x]["token_id"]
    fixed_price = data_json["list"][x]["fixed_price"]
    ouputStr += "{:<8}" +  "{:<8}" +  "{:<8}"  + "\n"
    ouputStr  = ouputStr.format("M",fixed_price,token_id)

    response = urlopen(urlKiss)
    data_json = json.loads(response.read())
    token_id = data_json["list"][x]["token_id"]
    fixed_price = data_json["list"][x]["fixed_price"]
    ouputStr += "{:<8}" +  "{:<8}" +  "{:<8}"  + "\n"
    ouputStr  = ouputStr.format("K",fixed_price,token_id)

    response = urlopen(urlCali)
    data_json = json.loads(response.read())
    token_id = data_json["list"][x]["token_id"]
    fixed_price = data_json["list"][x]["fixed_price"]
    ouputStr += "{:<8}" +  "{:<8}" +  "{:<8}"  + "\n"
    ouputStr  = ouputStr.format("C",fixed_price,token_id)

    response = urlopen(urlUsm)
    data_json = json.loads(response.read())
    token_id = data_json["list"][x]["token_id"]
    fixed_price = data_json["list"][x]["fixed_price"]
    ouputStr += "{:<8}" +  "{:<8}" +  "{:<8}"  + "\n"
    ouputStr  = ouputStr.format("U",fixed_price,token_id)

    ouputStrx ="Giá thấp nhất của USM LAND" + "\n"  +"{:<8}" +"{:<8}" +"{:<8}" + "\n"   + "=========================" + "\n" + ouputStr
    ouputStrx  = ouputStrx.format("LAND","PRICE","ID")
    update.message.reply_text( ouputStrx
        )

def priceAlert(update, context):
    if len(context.args) > 2:
        typeLand = context.args[0].upper()
        sign = context.args[1]
        price = context.args[2]

        context.job_queue.run_repeating(priceAlertCallback, interval=15, first=15, context=[typeLand, sign, price, update.message.chat_id])
        
        response = f"⏳ Tôi sẽ gửi message khi giá {typeLand} {sign} {price}, \n"
        response += f"Giá hiện tại của {typeLand} là {getPrice(typeLand)}"
    else:
        response = '⚠️ Hãy set Type Land và Price: \n alert {typeLand} {sign} {price}'
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def priceAlertCallback(context):
    typeLand = context.job.context[0]
    sign = context.job.context[1]
    price = context.job.context[2]
    chat_id = context.job.context[3]

    send = False
    spot_price = getPrice(typeLand)

    if sign == '<':
        if float(price) >= float(spot_price):
            send = True
    else:
        if float(price) <= float(spot_price):
            send = True

    if send:
        response = f"👋 {typeLand} mức giá cảnh báo {sign}  {price},\n"
        response += f"Giá hiện tại của {typeLand} là {spot_price}"
        context.job.schedule_removal()
        context.bot.send_message(chat_id=chat_id, text=response)

def getPrice(typeLand): 
    if typeLand == 'MML': 
        response = urlopen(urlMusk)
    elif typeLand == "CALI": 
        response = urlopen(urlCali)
    elif typeLand== "KISS": 
        response = urlopen(urlKiss)
    elif typeLand== "USM": 
        response = urlopen(urlUsm)

    data_json = json.loads(response.read())
    getPrice = data_json["list"][0]["fixed_price"]
    return getPrice

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5119226338:AAHg_5FmcFebx_L29QtmxqfV_huHBP9H_EE")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("mml", mml))
    dispatcher.add_handler(CommandHandler("cali", cali))
    dispatcher.add_handler(CommandHandler("kiss", kiss))
    dispatcher.add_handler(CommandHandler("usm", usm))
    dispatcher.add_handler(CommandHandler("land", land))
    dispatcher.add_handler(CommandHandler('alert', priceAlert)) # Accessed via /alert

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()