class script(object):
    START_TXT = """𝐻𝑒𝑦 𝐵𝑢𝑑𝑑𝑦{},
I Am <a href=https://t.me/{}>{}</a>,

𝑰 𝑯𝒂𝒗𝒆 𝑻𝒐𝒏𝒔 𝒐𝒇 𝑴𝒐𝒗𝒊𝒆𝒔 & 𝑽𝒊𝒅𝒆𝒐𝒔 𝒊𝒏 𝑴𝒚 𝑫𝒂𝒕𝒂𝑩𝒂𝒔𝒆 ᴛᴏ ᴄʜᴇᴄᴋ ᴍʏ sᴛᴀᴛᴜs /stats
🔸𝐼 𝐶𝑎𝑛 𝑃𝑟𝑜𝑣𝑖𝑑𝑒 𝑀𝑜𝑣𝑖𝑒𝑠 𝐼𝑛 𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑚 𝐺𝑟𝑜𝑢𝑝𝑠. 
🔸𝑌𝑜𝑢 𝐶𝑎𝑛 𝑆𝑒𝑎𝑟𝑐𝒉 𝑀𝑜𝑣𝑖𝑒𝑠 𝑉𝑖𝑎 𝐼𝑛𝑙𝑖𝑛𝑒. 
🔸𝐼 𝐶𝑎𝑛 𝐴𝑙𝑠𝑜 𝐴𝑑𝑑 𝐹𝑖𝑙𝑡𝑒𝑟𝑠 𝐼𝑛 𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑚 𝐺𝑟𝑜𝑢𝑝𝑠.
🔸𝐽𝑢𝑠𝑡 𝐴𝑑𝑑 𝑀𝑒 𝑇𝑜 𝑌𝑜𝑢𝑟 𝐺𝑟𝑜𝑢𝑝 𝐴𝑛𝑑 𝐸𝑛𝑗𝑜𝑦 𝑂𝑓 𝐴𝑙𝑙 𝐴𝑣𝑎𝑖𝑙𝑎𝑏𝑙𝑒 𝑀𝑜𝑣𝑖𝑒𝑠 𝑂𝑛 𝑇𝐺.
🔰𝑌𝑜𝑢 𝐶𝑎𝑛 𝑈𝑠𝑒 𝑀𝑒 𝑎𝑠 𝐴𝑢𝑡𝑜 𝐹𝑖𝑙𝑡𝑒𝑟 𝐹𝑜𝑟 𝑌𝑜𝑢𝑟 𝐺𝑟𝑜𝑢𝑝 

𝑀𝑎𝑑𝑒 𝑊𝑖𝑡𝒉 ❤️

𝐽𝑢𝑠𝑡 𝐴𝑑𝑑 𝑀𝑒 𝑡𝑜 𝑌𝑜𝑢𝑟 𝐺𝑟𝑜𝑢𝑝 𝐴𝑛𝑑 𝐸𝑛𝑗𝑜𝑦 😇

𝐹𝑜𝑟 𝑀𝑜𝑟𝑒 𝑖𝑛𝑓𝑜 𝐶𝑙𝑖𝑐𝑘 𝐻𝑒𝑙𝑝!"""
    HELP_TXT = """𝐻𝑒𝑦 𝐵𝑢𝑑𝑑𝑦{}
𝐼 𝑐𝑎𝑛  𝑃𝑟𝑜𝑣𝑖𝑑𝑒 𝑀𝑜𝑣𝑖𝑒 𝑡𝑜 𝑌𝑜𝑢𝑟 𝐺𝑟𝑜𝑢𝑝"""
    ABOUT_TXT = """ ABOUT ME
✯ 𝑀𝑦 𝑁𝑎𝑚𝑒: {}
✯ 𝐶𝑟𝑒𝑎𝑡𝑜𝑟: <a href=https://t.me/RestinHeaven>𝚁𝚎𝚜𝚝𝚒𝚗𝙷𝚎𝚊𝚟𝚎𝚗</a>
✯ 𝑙𝑖𝑏𝑟𝑎𝑟𝑦: <a href=https://t.me/RestinHeaven>𝚁𝚎𝚜𝚝𝚒𝚗𝙷𝚎𝚊𝚟𝚎𝚗</a>
✯ 𝐿𝑎𝑛𝑔𝑢𝑎𝑔𝑒: <a href=https://www.python.org/>𝒑𝒚𝒕𝒉𝒐𝒏</a>
✯ 𝐷𝑎𝑡𝑎𝑏𝑎𝑠𝑒: <a href=https://www.mongodb.com/>𝑴𝒐𝒏𝒈𝒐 𝑫𝑩</a>
✯ 𝑆𝑒𝑟𝑣𝑒𝑟: <a href=https://www.heroku.com/>𝑯𝒆𝒓𝒐𝒌𝒖</a>
✯ 𝐵𝑢𝑙𝑡 𝑆𝑡𝑎𝑡𝑢𝑠: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- 𝚁𝚎𝚜𝚝𝚒𝚗𝙷𝚎𝚊𝚟𝚎𝚗
- Source - https://t.me/RestinHeaven  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
