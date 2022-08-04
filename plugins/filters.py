import io
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.filters_mdb import(
   add_filter,
   get_filters,
   delete_filter,
   count_filters
)

from database.connections_mdb import active_connection
from utils import get_file_id, parser, split_quotes
from info import ADMINS


@Client.on_message(filters.command(['filter', 'add']) & filters.incoming)
async def addfilter(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"𝑌𝑜𝑢 𝑎𝑟𝑒 𝑎𝑛𝑜𝑛𝑦𝑚𝑜𝑢𝑠 𝑎𝑑𝑚𝑖𝑛. 𝑈𝑠𝑒 /connect {message.chat.id} 𝐼𝑛 𝑃𝑀")
    chat_type = message.chat.type
    args = message.text.html.split(None, 1)

    if chat_type == "private":
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("𝑀𝑎𝑘𝑒 𝑠𝑢𝑟𝑒 𝐼'𝑚 𝑝𝑟𝑒𝑠𝑒𝑛𝑡 𝑖𝑛 𝑦𝑜𝑢𝑟 𝑔𝑟𝑜𝑢𝑝!!", quote=True)
                return
        else:
            await message.reply_text("𝐼'𝑚 𝑛𝑜𝑡 𝑐𝑜𝑛𝑛𝑒𝑐𝑡𝑒𝑑 𝑡𝑜 𝑎𝑛𝑦 𝑔𝑟𝑜𝑢𝑝𝑠!", quote=True)
            return

    elif chat_type in ["group", "supergroup"]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if (
        st.status != "administrator"
        and st.status != "creator"
        and str(userid) not in ADMINS
    ):
        return


    if len(args) < 2:
        await message.reply_text("𝐶𝑜𝑚𝑚𝑎𝑛𝑑 𝐼𝑛𝑐𝑜𝑚𝑝𝑙𝑒𝑡𝑒 :(", quote=True)
        return

    extracted = split_quotes(args[1])
    text = extracted[0].lower()

    if not message.reply_to_message and len(extracted) < 2:
        await message.reply_text("𝐴𝑑𝑑 𝑠𝑜𝑚𝑒 𝑐𝑜𝑛𝑡𝑒𝑛𝑡 𝑡𝑜 𝑠𝑎𝑣𝑒 𝑦𝑜𝑢𝑟 𝑓𝑖𝑙𝑡𝑒𝑟!", quote=True)
        return

    if (len(extracted) >= 2) and not message.reply_to_message:
        reply_text, btn, alert = parser(extracted[1], text)
        fileid = None
        if not reply_text:
            await message.reply_text("𝑌𝑜𝑢 𝑐𝑎𝑛𝑛𝑜𝑡 𝒉𝑎𝑣𝑒 𝑏𝑢𝑡𝑡𝑜𝑛𝑠 𝑎𝑙𝑜𝑛𝑒, 𝑔𝑖𝑣𝑒 𝑠𝑜𝑚𝑒 𝑡𝑒𝑥𝑡 𝑡𝑜 𝑔𝑜 𝑤𝑖𝑡𝒉 𝑖𝑡!", quote=True)
            return

    elif message.reply_to_message and message.reply_to_message.reply_markup:
        try:
            rm = message.reply_to_message.reply_markup
            btn = rm.inline_keyboard
            msg = get_file_id(message.reply_to_message)
            if msg:
                fileid = msg.file_id
                reply_text = message.reply_to_message.caption.html
            else:
                reply_text = message.reply_to_message.text.html
                fileid = None
            alert = None
        except:
            reply_text = ""
            btn = "[]" 
            fileid = None
            alert = None

    elif message.reply_to_message and message.reply_to_message.media:
        try:
            msg = get_file_id(message.reply_to_message)
            fileid = msg.file_id if msg else None
            reply_text, btn, alert = parser(extracted[1], text) if message.reply_to_message.sticker else parser(message.reply_to_message.caption.html, text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None
    elif message.reply_to_message and message.reply_to_message.text:
        try:
            fileid = None
            reply_text, btn, alert = parser(message.reply_to_message.text.html, text)
        except:
            reply_text = ""
            btn = "[]"
            alert = None
    else:
        return

    await add_filter(grp_id, text, reply_text, btn, fileid, alert)

    await message.reply_text(
        f"Filter for  `{text}`  added in  **{title}**",
        quote=True,
        parse_mode="md"
    )


@Client.on_message(filters.command(['viewfilters', 'filters']) & filters.incoming)
async def get_all(client, message):
    
    chat_type = message.chat.type
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"𝑌𝑜𝑢 𝑎𝑟𝑒 𝑎𝑛𝑜𝑛𝑦𝑚𝑜𝑢𝑠 𝑎𝑑𝑚𝑖𝑛. 𝑈𝑠𝑒 /connect {message.chat.id} 𝐼𝑛 𝑃𝑀")
    if chat_type == "private":
        userid = message.from_user.id
        grpid = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("𝑀𝑎𝑘𝑒 𝑠𝑢𝑟𝑒 𝐼'𝑚 𝑝𝑟𝑒𝑠𝑒𝑛𝑡 𝑖𝑛 𝑦𝑜𝑢𝑟 𝑔𝑟𝑜𝑢𝑝!!", quote=True)
                return
        else:
            await message.reply_text("𝐼'𝑚 𝑛𝑜𝑡 𝑐𝑜𝑛𝑛𝑒𝑐𝑡𝑒𝑑 𝑡𝑜 𝑎𝑛𝑦 𝑔𝑟𝑜𝑢𝑝𝑠!!", quote=True)
            return

    elif chat_type in ["group", "supergroup"]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if (
        st.status != "administrator"
        and st.status != "creator"
        and str(userid) not in ADMINS
    ):
        return

    texts = await get_filters(grp_id)
    count = await count_filters(grp_id)
    if count:
        filterlist = f"𝑇𝑜𝑡𝑎𝑙 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑓𝑖𝑙𝑡𝑒𝑟𝑠 𝑖𝑛 **{title}** : {count}\n\n"

        for text in texts:
            keywords = " ×  `{}`\n".format(text)

            filterlist += keywords

        if len(filterlist) > 4096:
            with io.BytesIO(str.encode(filterlist.replace("`", ""))) as keyword_file:
                keyword_file.name = "keywords.txt"
                await message.reply_document(
                    document=keyword_file,
                    quote=True
                )
            return
    else:
        filterlist = f"𝑇𝒉𝑒𝑟𝑒 𝑎𝑟𝑒 𝑛𝑜 𝑎𝑐𝑡𝑖𝑣𝑒 𝑓𝑖𝑙𝑡𝑒𝑟𝑠 𝑖𝑛 **{title}**"

    await message.reply_text(
        text=filterlist,
        quote=True,
        parse_mode="md"
    )
        
@Client.on_message(filters.command('del') & filters.incoming)
async def deletefilter(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"𝑌𝑜𝑢 𝑎𝑟𝑒 𝑎𝑛𝑜𝑛𝑦𝑚𝑜𝑢𝑠 𝑎𝑑𝑚𝑖𝑛. 𝑈𝑠𝑒 /connect {message.chat.id} 𝐼𝑛 𝑃𝑀")
    chat_type = message.chat.type

    if chat_type == "private":
        grpid  = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("𝑀𝑎𝑘𝑒 𝑠𝑢𝑟𝑒 𝐼'𝑚 𝑝𝑟𝑒𝑠𝑒𝑛𝑡 𝑖𝑛 𝑦𝑜𝑢𝑟 𝑔𝑟𝑜𝑢𝑝!!", quote=True)
                return
        else:
            await message.reply_text("𝐼'𝑚 𝑛𝑜𝑡 𝑐𝑜𝑛𝑛𝑒𝑐𝑡𝑒𝑑 𝑡𝑜 𝑎𝑛𝑦 𝑔𝑟𝑜𝑢𝑝𝑠!", quote=True)

    elif chat_type in ["group", "supergroup"]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if (
        st.status != "administrator"
        and st.status != "creator"
        and str(userid) not in ADMINS
    ):
        return

    try:
        cmd, text = message.text.split(" ", 1)
    except:
        await message.reply_text(
            "<i>𝑀𝑒𝑛𝑡𝑖𝑜𝑛 𝑡𝒉𝑒 𝑓𝑖𝑙𝑡𝑒𝑟𝑛𝑎𝑚𝑒 𝑤𝒉𝑖𝑐𝒉 𝑦𝑜𝑢 𝑤𝑎𝑛𝑛𝑎 𝑑𝑒𝑙𝑒𝑡𝑒!</i>\n\n"
            "<code>/del 𝑓𝑖𝑙𝑡𝑒𝑟𝑛𝑎𝑚𝑒</code>\n\n"
            "𝑈𝑠𝑒 /viewfilters 𝑡𝑜 𝑣𝑖𝑒𝑤 𝑎𝑙𝑙 𝑎𝑣𝑎𝑖𝑙𝑎𝑏𝑙𝑒 𝑓𝑖𝑙𝑡𝑒𝑟𝑠 ",
            quote=True
        )
        return

    query = text.lower()

    await delete_filter(message, query, grp_id)
        

@Client.on_message(filters.command('delall') & filters.incoming)
async def delallconfirm(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"𝑌𝑜𝑢 𝑎𝑟𝑒 𝑎𝑛𝑜𝑛𝑦𝑚𝑜𝑢𝑠 𝑎𝑑𝑚𝑖𝑛. 𝑈𝑠𝑒 /connect {message.chat.id} 𝐼𝑛 𝑃𝑀")
    chat_type = message.chat.type

    if chat_type == "private":
        grpid  = await active_connection(str(userid))
        if grpid is not None:
            grp_id = grpid
            try:
                chat = await client.get_chat(grpid)
                title = chat.title
            except:
                await message.reply_text("𝑀𝑎𝑘𝑒 𝑠𝑢𝑟𝑒 𝐼'𝑚 𝑝𝑟𝑒𝑠𝑒𝑛𝑡 𝑖𝑛 𝑦𝑜𝑢𝑟 𝑔𝑟𝑜𝑢𝑝!!", quote=True)
                return
        else:
            await message.reply_text("𝐼'𝑚 𝑛𝑜𝑡 𝑐𝑜𝑛𝑛𝑒𝑐𝑡𝑒𝑑 𝑡𝑜 𝑎𝑛𝑦 𝑔𝑟𝑜𝑢𝑝𝑠!", quote=True)
            return

    elif chat_type in ["group", "supergroup"]:
        grp_id = message.chat.id
        title = message.chat.title

    else:
        return

    st = await client.get_chat_member(grp_id, userid)
    if (st.status == "creator") or (str(userid) in ADMINS):
        await message.reply_text(
            f"𝑇𝒉𝑖𝑠 𝑤𝑖𝑙𝑙 𝑑𝑒𝑙𝑒𝑡𝑒 𝑎𝑙𝑙 𝑓𝑖𝑙𝑡𝑒𝑟𝑠 𝑓𝑟𝑜𝑚 '{title}'.\n𝐷𝑜 𝑦𝑜𝑢 𝑤𝑎𝑛𝑡 𝑡𝑜 𝑐𝑜𝑛𝑡𝑖𝑛𝑢𝑒???",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="YES",callback_data="delallconfirm")],
                [InlineKeyboardButton(text="CANCEL",callback_data="delallcancel")]
            ]),
            quote=True
        )

