from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Your Telegram API credentials
api_id = "25139089"
api_hash = "45fa74a814befe61aea26e35b0fdcb6b"
bot_token = "6635436615:AAEYg-xscSj0oI4RPM5S9NeLlI_7jJ2rj14"

# Your private channel chat ID
private_channel_chat_id = -1002108625817  # Replace with your actual private channel chat ID

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to send a recurring sticker with a button and delete the last message
async def send_recurring_sticker_with_button():
    last_message_id = None  # Store the message ID of the last sent message
    while True:
        # Customize the sticker and button details
        sticker_file_id = "CAACAgEAAxUAAWXSayASP-RKCMl4GrQNf42dR606AAIxAgACgqAgRAcLMFWsscaHNAQ"
        button_text = "Click Here"
        button_url = "https://example.com"

        # Create an InlineKeyboardMarkup with the button
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(button_text, url=button_url)]])

        # Delete the last sent message
        if last_message_id:
            await app.delete_messages(chat_id=private_channel_chat_id, message_ids=last_message_id)

        # Send the sticker with the button to the private channel
        message = await app.send_sticker(private_channel_chat_id, sticker=sticker_file_id, reply_markup=keyboard)

        # Update the last sent message ID
        last_message_id = message.message_id

        # Set the interval for the recurring sticker (in seconds)
        await asyncio.sleep(20)  # Adjust the interval as needed

# Event handler for incoming messages
@app.on_message(filters.command("start"))
async def start_bot(client, message):
    print("Bot has started!")
    # Start the recurring sticker with button loop
    asyncio.create_task(send_recurring_sticker_with_button())

# Start the bot
app.run()

