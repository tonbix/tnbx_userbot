from time import time

from lang import get_lang


class Ping:
	def __init__(self) -> None:
		self.enabled: bool = True
		self.aliases: tuple = ("ping", )
		self.usage: str = "-/<passes amount>"
		self.description: str = "calculates the time required to edit the message"

	async def function(self, message, args) -> None:
		passes = 1
		responseTime = []

		try:
			if args[0].isdecimal():
				passes = int(args[0])
		except Exception:
			pass

		lang = await get_lang()

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
			averageResult = round(sum(responseTime)/len(responseTime), 2)
			minResult = min(responseTime)
			maxResult = max(responseTime)

			response_text = lang["commands"]["ping"]["header"] + \
				lang["commands"]["ping"]["passesCounter"].replace("/{1}", "").format(passes) + "\n" + \
				lang["commands"]["ping"]["multipleTestResults"].format(
					averageResult, minResult, maxResult)
			await message.edit(response_text)
