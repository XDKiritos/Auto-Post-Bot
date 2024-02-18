from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Your Telegram API credentials
api_id = "25139089"
api_hash = "45fa74a814befe61aea26e35b0fdcb6b"
bot_token = "6850791321:AAFQwPA6321Gxn_N-0YBsTE6BjSsA_xzTWs"

# Your group chat IDs
group_chat_ids = [-1002108625817]  # Replace with your actual group chat IDs

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to send a recurring sticker with a button and another message to multiple groups
async def send_recurring_sticker_with_button():
    while True:
        # Customize the sticker and button details
        sticker_file_id = "CAACAgEAAxUAAWXSayASP-RKCMl4GrQNf42dR606AAIxAgACgqAgRAcLMFWsscaHNAQ"
        button_text = "Click Here"
        button_url = "https://example.com"
        additional_message = "This is an additional message."

        # Create an InlineKeyboardMarkup with the button
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(button_text, url=button_url)]])

        # Send the sticker with the button to each group
        for group_chat_id in group_chat_ids:
            # Send the sticker with the button
            sent_message = await app.send_sticker(group_chat_id, sticker=sticker_file_id, reply_markup=keyboard)

            # Send the additional message
            await app.send_message(group_chat_id, text=additional_message, reply_to_message_id=sent_message.message_id)

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

