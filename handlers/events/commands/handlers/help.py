from asyncio import run

from configparser import ConfigParser

from lang import get_lang

from . import ping


# reads settings file
config = ConfigParser()
config.read("data/settings.ini")

# gets ;ang
lang = run(get_lang())


class Help:
	def __init__(self) -> None:
		self.enabled: bool = True
		self.aliases: tuple = ("help", )
		self.usage: str = "-/{{command}}"
		self.description: str = lang["commands"]["help"]["description"]


	async def function(self, message):
		"""
		shows help message with all commands and some settings
		"""
		# commands list
		commands = [self, ping.Ping()]

		commandsCards = []

		# creates "cards" for every command
		for command in commands:
			commandsCards.append(lang["commands"]["help"]["commandCard"].format(
				", ".join(command.aliases), command.description, command.usage))

		# builds response message text
		responseText =	lang["commands"]["help"]["header"] + "\n\n" + \
						lang["commands"]["help"]["settingsInfo"].format(
							config["Commands"]["prefix"]) + "\n\n" + \
						"\n".join(commandsCards)

		# editing message using "responseText"
		await message.edit(responseText)
