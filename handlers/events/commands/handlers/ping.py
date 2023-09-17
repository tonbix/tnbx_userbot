from time import time

from asyncio import run

from lang import get_lang


# resolving language
lang = run(get_lang())
pingLang = lang["commands"]["ping"]


class Ping:
	def __init__(self) -> None:
		self.enabled: bool =	True
		self.aliases: tuple =	("ping", "p")
		self.usage: str =		pingLang["usage"]
		self.description: str =	pingLang["description"]


	async def function(self, message, args) -> None:
		"""
		calculating the time required to edit the telegram message
		with no arguments return single-test result. With number as first arg returns multi-test result where amount of passes is first arg
		"""
		passes = 1
		responseTime = []

		try:
			if args[0].isdecimal():
				passes = int(args[0])
		except Exception:
			pass

		for i in range(passes):
			start = time()

			response_text = lang["commands"]["ping"]["header"] + \
				lang["commands"]["ping"]["passesCounter"].format(
					i, passes) + "\n"

			if responseTime:
				lang["commands"]["ping"]["singleTestResults"].format(
					responseTime[-1])
			else:
				lang["commands"]["ping"]["singleTestResults"].format("")

			await message.edit(response_text)

			responseTime.append(round((time() - start) * 1000, 2))

		if passes == 1:
			response_text = lang["commands"]["ping"]["header"] + "\n" + \
				lang["commands"]["ping"]["singleTestResults"].format(
					responseTime[-1])
			await message.edit(response_text)
		else:
			averageResult = round(sum(responseTime) / len(responseTime), 2)
			minResult = min(responseTime)
			maxResult = max(responseTime)

			response_text = lang["commands"]["ping"]["header"] + \
				lang["commands"]["ping"]["passesCounter"].replace("/{1}", "").format(passes) + "\n" + \
				lang["commands"]["ping"]["multipleTestResults"].format(
					averageResult, minResult, maxResult)
			await message.edit(response_text)
