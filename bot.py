from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from datetime import datetime, timedelta

# Your Telegram API credentials
api_id = "25139089"
api_hash = "45fa74a814befe61aea26e35b0fdcb6b"
bot_token = "6635436615:AAEYg-xscSj0oI4RPM5S9NeLlI_7jJ2rj14"

# Your private channel chat ID
private_channel_chat_id = -1002108625817  # Replace with your actual private channel chat ID

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to send a recurring sticker with a button
async def send_recurring_sticker_with_button():
    while True:
        # Customize the sticker and button details
        sticker_file_id = "CAACAgEAAxUAAWXSayASP-RKCMl4GrQNf42dR606AAIxAgACgqAgRAcLMFWsscaHNAQ"
        button_text = "Click Here"
        button_url = "https://example.com"

        # Create an InlineKeyboardMarkup with the button
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(button_text, url=button_url)]])

        # Send the sticker with the button to the private channel
        message = await app.send_sticker(private_channel_chat_id, sticker=sticker_file_id, reply_markup=keyboard)

        # Set the interval for the recurring sticker (in seconds)
        await asyncio.sleep(30)  # Adjust the interval as needed

# Function to delete messages sent 10 minutes ago in the channel
async def delete_old_messages():
    while True:
        # Calculate the time 10 minutes ago
        ten_minutes_ago = datetime.utcnow() - timedelta(minutes=1)

        # Get all messages in the channel
        messages = await app.get_chat_history(chat_id=private_channel_chat_id, limit=100)  # You may need to adjust the limit

        # Iterate through messages and delete those sent 10 minutes ago
        for msg in messages:
            if msg.date <= ten_minutes_ago.timestamp():
                await app.delete_messages(chat_id=private_channel_chat_id, message_ids=msg.message_id)

        # Set the interval for the message deletion (in seconds)
        await asyncio.sleep(60)  # 10 minutes interval

# Event handler for incoming messages
@app.on_message(filters.command("start"))
async def start_bot(client, message):
    print("Bot has started!")
    # Start the recurring sticker with button loop
    asyncio.create_task(send_recurring_sticker_with_button())
    # Start the message deletion loop
    asyncio.create_task(delete_old_messages())

# Start the bot
app.run()

