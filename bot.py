import logging
import os
import argparse

# Parse Token
parser = argparse.ArgumentParser(description='A telegram bot for downloading music on the host')
parser.add_argument('--token', help='the telegram bot token')
args = parser.parse_args()
TOKEN = args.token

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Import telegram API libraries
from telegram.ext import Updater
from telegram.ext import CommandHandler

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
    print(album_path)
    os.system(str('mkdir ' + album_path))
    os.system(str("spotdl --output-format m4a " + album_url + " --output " + album_path))

# Add bot functions
start_handler = CommandHandler('start', start)
album_handler = CommandHandler('album', album)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(album_handler)

# Start the bot
updater.start_polling()