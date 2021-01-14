#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import random
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, InlineQueryHandler, MessageHandler, Filters, CallbackContext, \
    ConversationHandler, PollAnswerHandler
from dotenv import load_dotenv

load_dotenv()

import os
token = os.environ.get("TELEGRAM_TOKEN")

print(token)
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

BLAME, DARK, LOCATION, BIO = range(4)

UPDATE_ID = None

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('chào con mẹ gì, ăn siêu phẩm thì liên hệ Văn Duệ BDSM Hòa')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help con cack, ăn siêu phẩm chetme')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    default_text = [
        'chích điện ko @duehoa1211',
        "@duehoa1211 sủa clgt??"
    ]
    # mai tao dạy mày chửi @duehoa1211 tiếp nha
    user_message = update.message.text.strip().lower()
    if update.message.text.strip().lower() == 'mai tao dạy mày chửi @duehoa1211 tiếp nha':
        update.message.reply_text("ok, vậy giờ chích điện @duehoa1211 ko ")
    elif user_message == 'cc':
        update.message.reply_text("cc có rất nhiều ý nghĩa ý giáo sư đan đề cập là coin card, con cack, hay 59")
    elif user_message == 'dkm' or user_message == 'dcm':
        update.message.reply_text("không làm mẹ, ok ?")
    elif user_message == 'vai lon':
        update.message.reply_text("vai lon @duehoa1211")
    elif user_message == 'lao ca cho' or user_message == 'láo cá chó':
        update.message.reply_text(" tao có súng tao bắn mày à @duehoa1211")
    else:
        update.message.reply_text(random.choice(default_text))

def blame(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    update.message.reply_text(
        'cương tao cho gặp bác sĩ Cường giờ '
        '',
        reply_markup=ReplyKeyboardRemove(),
    )

    return BLAME

def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'muốn chạy à, gõ /dark chơi tiếp mày', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

def dark(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s dark the conversation.", user.first_name)
    update.message.reply_text(
        'mở kèo máu ko @duehoa1211'
    )

    return DARK

def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    inline_message = update.inline_query.query
    logger.info("User %s inline the conversation.", inline_message)
    update.message.reply_text(
        'mở kèo máu ko @duehoa1211'
    )
    #update.inline_query.answer("con cac")

def taser(update: Update, context: CallbackContext) -> None:
    """Sends a predefined poll"""
    questions = ["Có", "không...à mà có", "!!Có", "!Không"]
    message = context.bot.send_poll(
        update.effective_chat.id,
        "Chích điện Hòa 15p, ok ko ?",
        questions,
        is_anonymous=True,
        allows_multiple_answers=False,
    )
    # Save some info about the poll the bot_data for later use in receive_poll_answer
    payload = {
        message.poll.id: {
            "questions": questions,
            "message_id": message.message_id,
            "chat_id": update.effective_chat.id,
            "answers": 0,
        }
    }
    context.bot_data.update(payload)

def pig_brain(update: Update, context: CallbackContext) -> None:
    """Sends a predefined poll"""
    questions = ["Có", "không...à mà có", "ăn chích điện thôi"]
    message = context.bot.send_poll(
        update.effective_chat.id,
        "óc heo ko, óc heo chứ đéo phải siêu phẩm nha?",
        questions,
        is_anonymous=True,
        allows_multiple_answers=False,
    )
    # Save some info about the poll the bot_data for later use in receive_poll_answer
    payload = {
        message.poll.id: {
            "questions": questions,
            "message_id": message.message_id,
            "chat_id": update.effective_chat.id,
            "answers": 0,
        }
    }
    context.bot_data.update(payload)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)

    # conv_handler = ConversationHandler(
    #     entry_points=[CommandHandler('dark', dark)],
    #     states={
    #     },
    #     fallbacks=[CommandHandler('cancel', cancel)],
    # )
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler('taser', taser))
    dispatcher.add_handler(CommandHandler('pig_brain', pig_brain))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(CommandHandler('dark', dark))
    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(InlineQueryHandler(inlinequery))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
