from configparser import ConfigParser

from json import load


async def get_lang(language=None, systemMessage=False) -> dict:
	config = ConfigParser()

	config.read("data/settings.ini")

	if language:
		selectedLanguage = language
	elif systemMessage:
		selectedLanguage = config["Language"]["systemMessagesLanguage"]
	else:
		selectedLanguage = config["Language"]["selectedLanguage"]

	with open(f"lang/{selectedLanguage}.json", "r") as langFile:
		return load(langFile)
