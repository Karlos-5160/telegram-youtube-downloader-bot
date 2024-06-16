# YouTube Downloader Bot

A Python-based YouTube downloader bot that allows users to download videos from YouTube in various formats and resolutions. This bot utilizes the `yt-dlp` library to fetch video metadata and download content directly from YouTube.
Telegram Link of he BOT - https://t.me/Youtube_Downloader45_Bot
or just search on Telegram @Youtube_Downloader45_Bot

## Features

- **Download Videos**: Download YouTube videos in multiple resolutions and formats (MP4, WebM, etc.).
- **Audio Extraction**: Extract and download audio tracks from YouTube videos in MP3 format.
- **Playlist Support**: Download entire YouTube playlists.
- **Metadata Handling**: Retrieve video metadata such as title, description, and thumbnail.
- **User-Friendly Interface**: Both in TG and also available in Command-line interface (CLI) for easy interaction.
- **Error Handling**: Robust error handling to manage various download issues.

## Installation 

### Prerequisites

- Python 3.6 or higher
- A Telegram bot token from [BotFather](https://core.telegram.org/bots#botfather)
- `ffmpeg` (for audio extraction)

### Steps

1. Clone the repository:
   ```sh
      git clone https://github.com/Karlos-5160/telegram-youtube-downloader-bot.git
      cd telegram-youtube-downloader-bot
2. Install the required dependencies:
      pip install -r requirements.txt
   
3. Set up your environment variables. Create a .env file in the project directory and add your Telegram bot token:
      TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   
### Usage
1. Run the bot:
      python bot.py

2. Open Telegram and start a chat with your bot.
 
3. Use desired commands to download a Video

### Configuration
You can configure additional settings by modifying the config.py file, such as default download paths, preferred formats, and more.

### Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.<br>
Create a new branch: git checkout -b feature-branch-name <br>
Make your changes and commit them: git commit -m 'Add some feature' <br>
Push to the branch: git push origin feature-branch-name <br>
Open a pull request. <br>
Please ensure your code adheres to the existing code style and includes appropriate tests.

### License
This project is licensed under the © Karlos License . See the LICENSE file for more details.

### Acknowledgements
• yt-dlp - The library used for downloading YouTube content. <br>
• python-telegram-bot - The library used to interact with the Telegram Bot API. <br>
• ffmpeg - A complete, cross-platform solution to record, convert, and stream audio and video.

### Contact
If you have any questions or feedback, please feel free to contact me at 2003kuldeepchoudhary@gmail.com
