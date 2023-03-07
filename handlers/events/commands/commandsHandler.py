from configparser import ConfigParser

from loguru import logger

from lang import get_lang

from .handlers import *


async def commands_handler(message) -> None:
	config = ConfigParser()
	config.read("data/settings.ini")

	if message.text:
		text = message.text
	elif message.caption:
		text = message.caption
	else:
		return

	if config["Commands"]["enabled"] and text.startswith(config["Commands"]["prefix"]):
		splittedText = text.split(" ")

		command = splittedText[0][1:].lower()
		args = splittedText[1:]

		lang = await get_lang(systemMessage=True)

		commandsList = [
			[Ping(), [message, args]]
		]

		for commandObj in commandsList:
			if commandObj[0].enabled and command in commandObj[0].aliases:
				try:
					await commandObj[0].function(*commandObj[1])
					logRaisedCommandText = lang["terminalMessages"]["commandRaised"] \
						.format(command, ", ".join(args))
					logger.info(logRaisedCommandText)
				except Exception as e:
					await message.edit(lang["errors"]["unexpectedError"])
					logger.exception(lang["errors"]["unexpectedError"])
