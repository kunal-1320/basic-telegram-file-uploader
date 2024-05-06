# Telegram File Uploader

This Python script monitors a folder on your computer and uploads any new files added to that folder to a private Telegram channel.

## Prerequisites

- Python 3 installed on your computer
- `python-telegram-bot` library installed (`pip install python-telegram-bot`)

## Setup

1. Clone this repository to your local machine.
2. Install the required Python packages:
    ```
    pip install python-telegram-bot
    ```
3. Open the `file_monitor.py` file in a text editor.
4. Replace `your_bot_token` with your actual Telegram Bot token and `your_channel_id` with your actual Telegram channel ID.
5. Save the file.

## Usage

1. Run the `file_monitor.py` script using Python:
    ```
    python file_monitor.py
    ```
2. Move or copy any file you want to upload to the monitored folder (`folder location`).
3. The script will automatically detect the new file and upload it to your Telegram channel.

## Important Notes

- Make sure the Telegram bot has permission to send documents to the channel.
- The script runs continuously and will upload any new files added to the monitored folder.

