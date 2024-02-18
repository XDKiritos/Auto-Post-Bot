from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Your Telegram API credentials
api_id = "25139089"
api_hash = "45fa74a814befe61aea26e35b0fdcb6b"
bot_token = "6850791321:AAFQwPA6321Gxn_N-0YBsTE6BjSsA_xzTWs"

# Your private channel chat ID
private_channel_chat_id = -1002108625817  # Replace with your actual private channel chat ID

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to send a recurring message with customizable content
async def send_recurring_message():
    while True:
        # Customize the message content, sticker, and button link
        message_content = "Hello! This is a recurring message."
        sticker_file_id = "CAACAgEAAxUAAWXSayASP-RKCMl4GrQNf42dR606AAIxAgACgqAgRAcLMFWsscaHNAQ"
        button_text = "Click Here"
        button_url = "https://example.com"

        # Create an InlineKeyboardMarkup with the button
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(button_text, url=button_url)]])

        # Send the sticker and button together
        await app.send_sticker(private_channel_chat_id, sticker=sticker_file_id, reply_markup=keyboard)

        # Wait for a short duration
        await asyncio.sleep(1)

        # Send the message separately
        await app.send_message(private_channel_chat_id, text=message_content, reply_markup=keyboard)

        # Set the interval for the recurring message (in seconds)
        await asyncio.sleep(30)  # Adjust the interval as needed

# Event handler for incoming messages
@app.on_message(filters.command("start"))
async def start_bot(client, message):
    print("Bot has started!")
    # Start the recurring message loop
    asyncio.create_task(send_recurring_message())

# Start the bot
app.run()

