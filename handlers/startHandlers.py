from pyrogram import filters
from pyrogram.handlers import (
	message_handler
)

from .events import *


def start_handlers(client) -> None:
	"""
	starts all required handlers
	"""
	client.add_handler(message_handler.MessageHandler(on_my_message, filters.me))
