from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Your Telegram API credentials
api_id = "25139089"
api_hash = "45fa74a814befe61aea26e35b0fdcb6b"
bot_token = "6850791321:AAFQwPA6321Gxn_N-0YBsTE6BjSsA_xzTWs"

# List of channel IDs where the bot should work
channel_ids = [-1002108625817]

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to send a recurring message with customizable content
async def send_recurring_message(channel_id):
    while True:
        # Customize the message content, sticker, and button link
        message_content = "Share to unlock 97368 videos."
        sticker_file_id = "CAACAgEAAxUAAWXSayASP-RKCMl4GrQNf42dR606AAIxAgACgqAgRAcLMFWsscaHNAQ"
        button_text = "Share to 3 Group 0/3"
        button_url = "https://t.me/share/url?url=https://t.me/joinchat/YJjrQQ81qqhjYzRl"

        # Create an InlineKeyboardMarkup with the button
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(button_text, url=button_url)]])

        # Send the sticker and button together
        await app.send_sticker(channel_id, sticker=sticker_file_id, reply_markup=keyboard)

        # Wait for a short duration
        await asyncio.sleep(2)

        # Send the message without the button
        await app.send_message(channel_id, text=message_content)

        # Set the interval for the recurring message (in seconds)
        await asyncio.sleep(21600)  # Adjust the interval as needed

# Event handler for incoming messages
@app.on_message(filters.command("start"))
async def start_bot(client, message):
    print("Bot has started!")
    for channel_id in channel_ids:
        # Start the recurring message loop for each channel
        asyncio.create_task(send_recurring_message(channel_id))

# Start the bot
app.run()
