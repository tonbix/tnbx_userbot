from configparser import ConfigParser

import asyncio

from loguru import logger

from lang import get_lang

from .handlers import *


async def commands_handler(message) -> None:
	"""
	Receives a message, if it starts with the prefix specified in the settings, then parses it into a command and arguments and then calls the necessary command.
	Otherwise skips
	"""
	# reads config
	config = ConfigParser()
	config.read("data/settings.ini")

	# gets text from message
	if message.text:
		text = message.text
	elif message.caption:
		text = message.caption
	else:
		return

	# checks that message is command and checks that commands enabled
	if config["Commands"]["enabled"] and text.startswith(config["Commands"]["prefix"]):
		# splits message by " "
		splittedText = text.split(" ")

		# parses command and args from text
		command = splittedText[0][len(config["Commands"]["prefix"]):].lower()
		args = splittedText[1:]

		# gets language dict
		lang = await get_lang()
		terminalLang = await get_lang(systemMessage=True)

		# list of commands and its arguments
		commandsList = [
			[Ping(), [message, args]],
			[Help(), [message]]
		]

		# checks that executed command exists and that this command enabled
		for commandObj in commandsList:
			if commandObj[0].enabled and command in commandObj[0].aliases:
				try:
					# runs command and logs it
					logger.info(terminalLang["terminalMessages"]["commandRaised"].format(
						command, ", ".join(args)))
					await commandObj[0].function(*commandObj[1])
				except Exception as e:
					# logs error 
					await message.edit(lang["errors"]["unexpectedError"].format(e))
					logger.exception(terminalLang["terminalMessages"]["unexpectedError"])
