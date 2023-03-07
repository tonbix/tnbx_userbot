from pyrogram import (
    Client,					# type: ignore
    idle					# type: ignore
)
from pyrogram.enums import ParseMode

from configparser import ConfigParser

import json

from dotenv import load_dotenv
from os import getenv

from utils import configure_loguru
from lang import get_lang
from handlers import start_handlers

"""
TODO:
[x] language manager
[x] setup function
[x] handlers starter
[x] commands loader
[x] command structure
[x] commands handler
[-] help command
[-] updater
[x] configure loguru logger
[x] replace log prints with loguru ones
"""

load_dotenv(dotenv_path="data/.env")

config = ConfigParser()
config.read("data/settings.ini")

accountUsername = config["Authorization"]["account"]
accountCredential = json.loads(str(getenv("TG_CREDENTIALS")))[accountUsername]

client = Client(accountUsername, accountCredential["apiId"],
                accountCredential["apiHash"], parse_mode=ParseMode.HTML)


configure_loguru()

start_handlers(client)


async def run_client() -> None:
    await client.start()

    clientUser = await client.get_me()
    terminalLang = await get_lang(systemMessage=True)
    print(terminalLang["terminalMessages"]["onStartup"].format(
        clientUser.username, clientUser.id), end="\n\n")

    await idle()

    await client.stop()


if __name__ == "__main__":
    client.run(run_client())
