from pyrogram import types


async def get_full_name(user: types.User) -> str:
    fullname = user.first_name
    if user.last_name:
        fullname += user.last_name
    
    return fullname