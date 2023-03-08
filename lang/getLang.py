from configparser import ConfigParser

from json import load


async def get_lang(language=None, systemMessage=False) -> dict:
	# reads config
	config = ConfigParser()
	config.read("data/settings.ini")

	# selects language based on input arguments and settings file
	if language:
		selectedLanguage = language
	elif systemMessage:
		selectedLanguage = config["Language"]["systemMessagesLanguage"]
	else:
		selectedLanguage = config["Language"]["selectedLanguage"]

	# gets and returns selected language from file
	with open(f"lang/{selectedLanguage.lower()}.json", "r") as langFile:
		return load(langFile)
