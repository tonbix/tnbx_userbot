from pyrogram import (
    Client,					# type: ignore
    idle					# type: ignore
)
from pyrogram.enums import ParseMode

from configparser import ConfigParser

import json

from dotenv import load_dotenv
from os import getenv

import asyncio
import uvloop

from utils import configure_loguru
from lang import get_lang
from handlers import start_handlers

"""
TODO:
[x] help command
[-] updater
"""

# installs uvloop
uvloop.install()

# loads dotenv
load_dotenv(dotenv_path="data/.env")

# loads settings
config = ConfigParser()
config.read("data/settings.ini")

# gets account credentials by key from settings
accountUsername = config["Authorization"]["account"]
accountCredential = json.loads(str(getenv("TG_CREDENTIALS")))[accountUsername]

# gets language dict for terminal logging
with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
    terminalLang = runner.run(get_lang(systemMessage=True))

# shows selected in settings account username
print(terminalLang["terminalMessages"]["selectedAccount"].format(
    accountUsername))

# initializes client
client = Client(accountUsername, accountCredential["apiId"],
                accountCredential["apiHash"], parse_mode=ParseMode.HTML)

# runs loguru configuration
configure_loguru()

# starts all handlers
start_handlers(client)


async def run_client() -> None:
    """
    function that runs bot client
    executes start(), idle(), stop() and prints some account info in terminal after login
    """
    await client.start()

    # gets user from client and prints some information about selected account
    clientUser = await client.get_me()
    print(terminalLang["terminalMessages"]["onStartup"].format(
        clientUser.username, clientUser.id), end="\n\n")

    await idle()

    await client.stop()


if __name__ == "__main__":
    client.run(run_client())
