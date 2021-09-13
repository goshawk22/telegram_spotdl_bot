FROM ubuntu:20.04

ENV PIP_NO_CACHE_DIR=1

# Fixing major OS dependencies
# ----------------------------
RUN apt update \
  && apt install -y python3 python3-pip \
  && apt install -y wget \
  && apt install -y ffmpeg

# Installing spotDL and Telegram Bot API
# --------------
RUN pip3 install spotdl python-telegram-bot

RUN wget https://raw.githubusercontent.com/goshawk22/telegram_spotdl_bot/master/bot.py

CMD python3 bot.py --token $TELEGRAM_TOKEN