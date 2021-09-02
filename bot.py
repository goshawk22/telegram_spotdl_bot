import logging
import os

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Import telegram API libraries
from telegram.ext import Updater
from telegram.ext import CommandHandler

# Define token
TOKEN = "<enter token here>"

# Create updater and dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define start bot function
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot to download music!")

# Define a function to download an album from spotify
def album(update, context):
    artist, album, album_url = update.message.text[7:].split(',')
    album_path = "/media/audio/" + artist + "/" + album + "/"
    print(temp_path)
    os.system(str('mkdir ' + temp_path))
    os.system(str("spotdl --output-format m4a " + album_url + " --output " + temp_path))

# Add bot functions
start_handler = CommandHandler('start', start)
album_handler = CommandHandler('album', album)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(album_handler)

# Start the bot
updater.start_polling()