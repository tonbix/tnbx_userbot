from asyncio import run
from pyrogram import enums

from utils import get_full_name
from lang import get_lang


# resolving language
lang = run(get_lang())
messageInfoLang = lang["commands"]["messageInfo"]


class MessageInfo:
    def __init__(self) -> None:
        self.enabled: bool =    True
        self.aliases: tuple =   ("messageinfo", "msginfo", "msgi", "msg")
        self.usage: str =       messageInfoLang["usage"]
        self.description: str = messageInfoLang["description"]

    async def function(self, client, message, args):
        if message.reply_to_message:
            targetMessage = message.reply_to_message
        elif len(args) >= 1:
            try:
                targetMessage = await client.get_messages(message.chat.id, int(args[0]))
            except ValueError:
                return
        else:
            raise(ValueError)

        messageId = targetMessage.id

        messageTextLenght = len(targetMessage.text)
        messageTextLenghtWithoutSpaces = len("".join(targetMessage.text.split()))

        messageSender = targetMessage.from_user
        messageSenderFullname = await get_full_name(messageSender)
        messageSenderId = messageSender.id

        if targetMessage.chat.type in ( enums.ChatType.GROUP, \
                                        enums.ChatType.SUPERGROUP):
            messageChatTitle = targetMessage.chat.title
            messageChatId = targetMessage.chat.id
        else:
            messageChatTitle, messageChatId = [messageInfoLang["chatIsDM"]]*2

        messageTimestamp = f"{targetMessage.date.day}-{targetMessage.date.month}-{targetMessage.date.year} {targetMessage.date.hour}:{targetMessage.date.minute}:{targetMessage.date.second}"
        
        text = messageInfoLang["header"].format(messageId) + f"\n {lang['listElementSymbol']} " + \
            f"\n {lang['listElementSymbol']} ".join(messageInfoLang["content"]).format(
                messageTextLenght, messageTextLenghtWithoutSpaces,
                messageSenderFullname, messageSenderId,
                messageChatTitle, messageChatId,
                messageTimestamp
            )
        
        await message.edit_text(text)
