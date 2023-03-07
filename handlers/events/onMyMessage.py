from .commands import commands_handler


async def on_my_message(client, message) -> None:
	await commands_handler(message)
