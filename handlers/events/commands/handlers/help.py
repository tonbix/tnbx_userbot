from asyncio import run

from configparser import ConfigParser

from lang import get_lang

from . import ping, exportPins, messageInfo


# reading settings file
config = ConfigParser()
config.read("data/settings.ini")

# resolving language
lang = run(get_lang())
helpLang = lang["commands"]["help"]


class Help:
	def __init__(self) -> None:
		self.enabled: bool =	True
		self.aliases: tuple =	("help", "h")
		self.usage: str =		helpLang["usage"]
		self.description: str =	helpLang["description"]


	async def function(self, message):
		"""
		showing help message with all commands and some settings
		"""
		# list of commands
		commands = [self, ping.Ping(), exportPins.ExportPins(), messageInfo.MessageInfo()]

		commandsCards = []

		# creating "cards" for every command
		for command in commands:
			commandsCards.append(lang["commands"]["help"]["commandCard"].format(
				", ".join(command.aliases), command.description, command.usage))

		# building response message text
		responseText =	lang["commands"]["help"]["header"] + "\n\n" + \
						lang["commands"]["help"]["settingsInfo"].format(
							config["Commands"]["prefix"]) + "\n\n" + \
						"\n".join(commandsCards)

		# editing message using "responseText"
		await message.edit(responseText)
