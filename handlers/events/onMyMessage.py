from .commands import commands_handler


async def on_my_message(client, message) -> None:
	"""
	this handler will handle all messages that receives from authorized account
	"""
	await commands_handler(client, message)
