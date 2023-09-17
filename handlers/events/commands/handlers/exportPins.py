from asyncio import run
from pyrogram import enums

from lang import get_lang


# resolving language
lang = run(get_lang())
exportPinsLang = lang["commands"]["exportPins"]


class ExportPins:
    def __init__(self) -> None:
        self.enabled: bool =    True
        self.aliases: tuple =   ("exportpins", "exppins", "epins")
        self.usage: str =       exportPinsLang["usage"]
        self.description: str = exportPinsLang["description"]
    
    async def function(self, client, message, args) -> None:
        if len(args) >= 1:
            limit = int(args[0])
        else:
            limit = 0

        pinnedMessages = []

        async for pinnedMessage in client.search_messages(message.chat.id,
                                                     filter=enums.MessagesFilter.PINNED,
                                                     limit=limit):
            if message.chat.type in (   enums.ChatType.GROUP,\
                                        enums.ChatType.SUPERGROUP,\
                                        enums.ChatType.CHANNEL):
                messageLink = pinnedMessage.link
            else:
                messageLink = pinnedMessage.id

            pinnedMessages.append(f" {lang['listElementSymbol']} {messageLink}")

        if pinnedMessages:
            print(pinnedMessages)
            text = exportPinsLang["header"] + "\n" + "\n".join(pinnedMessages)
            await message.edit_text(text)
