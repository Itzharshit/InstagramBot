from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hii {},
I am instagram Downloader bot i can download profile pictures, videos, images and reels from instagram with caption.
You can also authorize me to download private posts.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="Return Home", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("YouTube", url="https://youtube.com/channel/UC2anvk7MNeNzJ6B4c0SZepw")],
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("Support Group", url="https://t.me/+7ScFy39Vckk5MWQ1")
        ],
        [InlineKeyboardButton("Updates Channel", url="https://t.me/pyrogrammers")],
    ]

    # Help Message
    HELP = """
1) **Images, Videos and Reels**
Send the link here to get the post contents including caption.

2) **Profile Pictures**
Use the command `/profile_pic` or `/dp` along with instagram username to get its profile picture.
Example : `/dp StarkProgrammer`

3) **Private Posts**
Authorize the bot to download private posts. Use /auth

**Note** : Stories and IGTV are not supported.

Use /auth to authorize and /unauth to unauthorize.
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to download instagram 

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @pyrogrammers
    """
