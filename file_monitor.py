import os
import time
from telegram import Bot

# Telegram Bot token
TOKEN = 'you bot token'

# Your private channel ID
CHANNEL_ID = 'channel id'  # Replace this with your actual channel ID

# Create a Telegram Bot object
bot = Bot(token=TOKEN)

# Function to send file to the channel
async def send_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            await bot.send_document(chat_id=CHANNEL_ID, document=file)
    except Exception as e:
        print(f"Error sending file: {e}")

# Function to check for new files
async def check_for_new_files(folder):
    processed_files = set()  # Set to keep track of processed files
    while True:
        files = os.listdir(folder)
        for file in files:
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path) and file not in processed_files:
                await send_file(file_path)
                processed_files.add(file)  # Add file to processed files set
        time.sleep(1)

if __name__ == "__main__":
    import asyncio
    asyncio.run(check_for_new_files(r'Folder location')) #folder location
