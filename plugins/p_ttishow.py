from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, MELCOW_NEW_USERS
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp, get_settings
from Script import script
from pyrogram.errors import ChatAdminRequired

"""-----------------------------------------https://t.me/GetTGLink/4179 --------------------------------------"""

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    r_j_check = [u.id for u in message.new_chat_members]
    if temp.ME in r_j_check:
        if not await db.get_chat(message.chat.id):
            total=await bot.get_chat_members_count(message.chat.id)
            r_j = message.from_user.mention if message.from_user else "Anonymous" 
            await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, r_j))       
            await db.add_chat(message.chat.id, message.chat.title)
        if message.chat.id in temp.BANNED_CHATS:
            # Inspired from a boat of a banana tree
            buttons = [[
                InlineKeyboardButton('Support', url=f'https://t.me/HeavenBotSupport')
            ]]
            reply_markup=InlineKeyboardMarkup(buttons)
            k = await message.reply(
                text='<b>𝐶𝐻𝐴𝑇 𝑁𝑂𝑇 𝐴𝐿𝐿𝑂𝑊𝐸𝐷 🐞\n\n𝑀𝑦 𝑎𝑑𝑚𝑖𝑛𝑠 𝒉𝑎𝑠 𝑟𝑒𝑠𝑡𝑟𝑖𝑐𝑡𝑒𝑑 𝑚𝑒 𝑓𝑟𝑜𝑚 𝑤𝑜𝑟𝑘𝑖𝑛𝑔 𝒉𝑒𝑟𝑒 ! 𝐼𝑓 𝑦𝑜𝑢 𝑤𝑎𝑛𝑡 𝑡𝑜 𝑘𝑛𝑜𝑤 𝑚𝑜𝑟𝑒 𝑎𝑏𝑜𝑢𝑡 𝑖𝑡 𝑐𝑜𝑛𝑡𝑎𝑐𝑡 𝑠𝑢𝑝𝑝𝑜𝑟𝑡...</b>',
                reply_markup=reply_markup,
            )

            try:
                await k.pin()
            except:
                pass
            await bot.leave_chat(message.chat.id)
            return
        buttons = [[
            InlineKeyboardButton('ℹ️ Help', url=f"https://t.me/{temp.U_NAME}?start=help"),
            InlineKeyboardButton('📢 Updates', url='https://t.me/RestinHeaven')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=f"<b>𝑇𝒉𝑎𝑛𝑘𝑦𝑜𝑢 𝐹𝑜𝑟 𝐴𝑑𝑑𝑖𝑛𝑔 𝑀𝑒 𝐼𝑛{message.chat.title} ❣️\n\n𝐼𝑓 𝑦𝑜𝑢 𝒉𝑎𝑣𝑒 𝑎𝑛𝑦 𝑞𝑢𝑒𝑠𝑡𝑖𝑜𝑛𝑠 & 𝑑𝑜𝑢𝑏𝑡𝑠 𝑎𝑏𝑜𝑢𝑡 𝑢𝑠𝑖𝑛𝑔 𝑚𝑒 𝑐𝑜𝑛𝑡𝑎𝑐𝑡 𝑠𝑢𝑝𝑝𝑜𝑟𝑡.</b>",
            reply_markup=reply_markup)
    else:
        settings = await get_settings(message.chat.id)
        if settings["welcome"]:
            for u in message.new_chat_members:
                if (temp.MELCOW).get('welcome') is not None:
                    try:
                        await (temp.MELCOW['welcome']).delete()
                    except:
                        pass
                temp.MELCOW['welcome'] = await message.reply(f"<b>𝐻𝑒𝑦 𝐵𝑟𝑜!, {u.mention}, 𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑡𝑜💐{message.chat.title}</b>")


@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('𝐺𝑖𝑣𝑒 𝑀𝑒 𝐶𝒉𝑎𝑡 𝐼𝐷')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('Support', url=f'https://t.me/HeavenBotSupport')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>𝐻𝑒𝑙𝑙𝑜 𝐹𝑟𝑖𝑒𝑛𝑑𝑠, \n𝑀𝑦 𝑎𝑑𝑚𝑖𝑛 𝒉𝑎𝑠 𝑡𝑜𝑙𝑑 𝑚𝑒 𝑡𝑜 𝑙𝑒𝑎𝑣𝑒 𝑓𝑟𝑜𝑚 𝑔𝑟𝑜𝑢𝑝 𝑠𝑜 𝑖 𝑔𝑜! 𝐼𝑓 𝑦𝑜𝑢 𝑤𝑎𝑛𝑛𝑎 𝑎𝑑𝑑 𝑚𝑒 𝑎𝑔𝑎𝑖𝑛 𝑐𝑜𝑛𝑡𝑎𝑐𝑡 𝑚𝑦 𝑠𝑢𝑝𝑝𝑜𝑟𝑡 𝑔𝑟𝑜𝑢𝑝..</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
        await message.reply(f"left the chat `{chat}`")
    except Exception as e:
        await message.reply(f'Error - {e}')

@Client.on_message(filters.command('disable') & filters.user(ADMINS))
async def disable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('𝐺𝑖𝑣𝑒 𝑀𝑒 𝐶𝒉𝑎𝑡 𝐼𝐷')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat_ = int(chat)
    except:
        return await message.reply('𝐺𝑖𝑣𝑒 𝑀𝑒 𝐴 𝑉𝑎𝑙𝑖𝑑 𝐶𝒉𝑎𝑡 𝐼𝐷')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("𝐶𝒉𝑎𝑡 𝑁𝑜𝑡 𝐹𝑜𝑢𝑛𝑑 𝐼𝑛 𝐷𝐵")
    if cha_t['is_disabled']:
        return await message.reply(f"𝑇𝒉𝑖𝑠 𝑐𝒉𝑎𝑡 𝑖𝑠 𝑎𝑙𝑟𝑒𝑎𝑑𝑦 𝑑𝑖𝑠𝑎𝑏𝑙𝑒𝑑 :\nReason-<code> {cha_t['reason']} </code>")
    await db.disable_chat(int(chat_), reason)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('𝐶𝒉𝑎𝑡 𝑆𝑢𝑐𝑐𝑒𝑠𝑠𝑓𝑢𝑙𝑙𝑦 𝐷𝑖𝑠𝑎𝑏𝑙𝑒𝑑')
    try:
        buttons = [[
            InlineKeyboardButton('Support', url=f'https://t.me/HeavenBotSupport')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'<b>𝐻𝑒𝑙𝑙𝑜 𝐹𝑟𝑖𝑒𝑛𝑑𝑠, \n𝑀𝑦 𝑎𝑑𝑚𝑖𝑛 𝒉𝑎𝑠 𝑡𝑜𝑙𝑑 𝑚𝑒 𝑡𝑜 𝑙𝑒𝑎𝑣𝑒 𝑓𝑟𝑜𝑚 𝑔𝑟𝑜𝑢𝑝 𝑠𝑜 𝑖 𝑔𝑜! 𝐼𝑓 𝑦𝑜𝑢 𝑤𝑎𝑛𝑛𝑎 𝑎𝑑𝑑 𝑚𝑒 𝑎𝑔𝑎𝑖𝑛 𝑐𝑜𝑛𝑡𝑎𝑐𝑡 𝑚𝑦 𝑠𝑢𝑝𝑝𝑜𝑟𝑡 𝑔𝑟𝑜𝑢𝑝..</b> \nReason : <code>{reason}</code>',
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Error - {e}")


@Client.on_message(filters.command('enable') & filters.user(ADMINS))
async def re_enable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('𝐺𝑖𝑣𝑒 𝑀𝑒 𝐶𝒉𝑎𝑡 𝐼𝐷')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('𝐺𝑖𝑣𝑒 𝑀𝑒 𝐴 𝑉𝑎𝑙𝑖𝑑 𝐶𝒉𝑎𝑡 𝐼𝐷')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("𝐶𝒉𝑎𝑡 𝑁𝑜𝑡 𝐹𝑜𝑢𝑛𝑑 𝐼𝑛 𝐷𝐵 !")
    if not sts.get('is_disabled'):
        return await message.reply('𝑇𝒉𝑖𝑠 𝑐𝒉𝑎𝑡 𝑖𝑠 𝑛𝑜𝑡 𝑦𝑒𝑡 𝑑𝑖𝑠𝑎𝑏𝑙𝑒𝑑.')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("𝐶𝒉𝑎𝑡 𝑆𝑢𝑐𝑐𝑒𝑠𝑠𝑓𝑢𝑙𝑙𝑦 𝑟𝑒-𝑒𝑛𝑎𝑏𝑙𝑒𝑑")


@Client.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('Fetching stats..')
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()
    files = await Media.count_documents()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await rju.edit(script.STATUS_TXT.format(files, total_users, totl_chats, size, free))


# a function for trespassing into others groups, Inspired by a Vazha
# Not to be used , But Just to showcase his vazhatharam.
# @Client.on_message(filters.command('invite') & filters.user(ADMINS))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('𝐺𝑖𝑣𝑒 𝑀𝑒 𝐶𝒉𝑎𝑡 𝐼𝐷')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('𝐺𝑖𝑣𝑒 𝑀𝑒 𝐴 𝑉𝑎𝑙𝑖𝑑 𝐶𝒉𝑎𝑡 𝐼𝐷')
    try:
        link = await bot.create_chat_invite_link(chat)
    except ChatAdminRequired:
        return await message.reply("𝐼𝑛𝑣𝑖𝑡𝑒 𝐿𝑖𝑛𝑘 𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑖𝑜𝑛 𝐹𝑎𝑖𝑙𝑒𝑑, 𝐼𝑎𝑚 𝑁𝑜𝑡 𝐻𝑎𝑣𝑖𝑛𝑔 𝑆𝑢𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑡 𝑅𝑖𝑔𝒉𝑡𝑠")
    except Exception as e:
        return await message.reply(f'Error {e}')
    await message.reply(f'𝐻𝑒𝑟𝑒 𝑖𝑠 𝑦𝑜𝑢𝑟 𝐼𝑛𝑣𝑖𝑡𝑒 𝐿𝑖𝑛𝑘 {link.invite_link}')

@Client.on_message(filters.command('ban') & filters.user(ADMINS))
async def ban_a_user(bot, message):
    # https://t.me/GetTGLink/4185
    if len(message.command) == 1:
        return await message.reply('𝐺𝑖𝑣𝑒 𝑚𝑒 𝑎 𝑢𝑠𝑒𝑟 𝑖𝑑 / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "𝑁𝑜 𝑟𝑒𝑎𝑠𝑜𝑛 𝑃𝑟𝑜𝑣𝑖𝑑𝑒𝑑"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure ia have met him before.")
    except IndexError:
        return await message.reply("This might be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} is already banned\nReason: {jar['ban_reason']}")
        await db.ban_user(k.id, reason)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"Successfully banned {k.mention}")


    
@Client.on_message(filters.command('unban') & filters.user(ADMINS))
async def unban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a user id / username')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "No reason Provided"
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except PeerIdInvalid:
        return await message.reply("This is an invalid user, make sure ia have met him before.")
    except IndexError:
        return await message.reply("Thismight be a channel, make sure its a user.")
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} is not yet banned.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"Successfully unbanned {k.mention}")


    
@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    # https://t.me/GetTGLink/4184
    raju = await message.reply('Getting List Of Users')
    users = await db.get_all_users()
    out = "Users Saved In DB Are:\n\n"
    async for user in users:
        out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>"
        if user['ban_status']['is_banned']:
            out += '( Banned User )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="List Of Users")

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    raju = await message.reply('Getting List Of chats')
    chats = await db.get_all_chats()
    out = "Chats Saved In DB Are:\n\n"
    async for chat in chats:
        out += f"**Title:** `{chat['title']}`\n**- ID:** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += '( Disabled Chat )'
        out += '\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="List Of Chats")
