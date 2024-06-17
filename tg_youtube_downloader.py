import os
import yt_dlp
import logging
import asyncio
import random
import datetime
from keep_alive import keep_alive
from dotenv import load_dotenv
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.ext import ConversationHandler, CallbackContext

keep_alive()
# Load environment variables from .env file
load_dotenv()
TOKEN: Final = os.getenv("TOKEN")
BOT_USERNAME: Final = "@Youtube_Downloader45_Bot"

if not TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found. Please set the TELEGRAM_BOT_TOKEN environment variable.")

print(f"Token: {TOKEN}")  # For debugging purposes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, welcome to the Youtube downloader Bot 3.0 🤖 by Karlos :)")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''
⚙️ Available Commands:
/start - Welcome message
/help - List of commands
/download - Download a YouTube video
/cancel - Cancel the downloading process
/info - Information about the bot
/bored - Play emoji game with me
''')

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_message = """
🤖 **Youtube Downloader Bot 3.0** 🤖

Hello there! I am a YouTube Downloader Bot created by 🐍 Python Developer - @Karlos_5160. 
You can use me to download YouTube videos directly from their URLs.

⚙️ **Available Commands**
/start - Welcome message
/help - List of commands
/download - Download a YouTube video 
/cancel - Cancel the downloading process
/info - Information about the bot
/bored - Play emoji game with me

💡 **How to Download**
To download a video, use the `/download` command and then send YouTube video URL.

🔗 **About the Bot**
This bot is built using Python and integrates with YouTube's API using the yt_dlp library. It supports downloading videos in the best available quality.

📧 **Contact Developer**
For any issues or suggestions, please contact @Karlos_5160.

👨‍💻 **Developer Profile**
Learn more about the developer and other projects at GitHub-> https://github.com/Karlos-5160

📅 **Bot Creation Date**
Created on 15-06-24.

🔗 **Source Code**
The source code for this bot is available on [GitHub](https://github.com/Karlos-5160/YoutubeDownloaderBot).

📄 **Disclaimer**
Please Ensure you have the necessary permissions to download and use the videos you download using this bot.

Enjoy downloading videos with the Youtube Downloader Bot 3.0! 🎥✨
                                   Copyright © 2024 Karlos
"""
    await update.message.reply_text(info_message)
    # await update.message.reply_text("Hello there! I am a Youtube downloader Bot. This bot is made using python-telegram-bot by 🐍Python Developer - @Karlos_5160.")
    
async def bored_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("It seems like you are bored 🥱 oky then let's play a emoji game send me a emoji :)")

# async def download_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     text = update.message.text
#     if len(text.split()) > 1:
#         url = text.split()[1]
#         print(url)
#         initial_time = datetime.datetime.now()
#         await update.message.reply_text("Fetching 👨‍💻.....")
#         await asyncio.sleep(4)  # Wait for 2 seconds
#         await update.message.reply_text("Downloading 👩‍💻.....")
#         video, file_path, file_name = await Download(url)
#         if video:
#             await update.message.reply_text("🖐️ Ruko Zara Sabr Karo 💁‍♂️💁‍♀️ Uploading Video......")
#             try:
#                 await update.message.reply_video(video, caption=file_name)
#                 final_time = datetime.datetime.now()
#                 download_time = final_time - initial_time
#                 download_time_seconds = download_time.total_seconds()
#                 download_time_formatted = f"{download_time_seconds:.2f}"
#                 await update.message.reply_text(f"Download just took --> {download_time_formatted} seconds")
#                 await update.message.reply_text("If you have any issues with download speed or video quality then take premium 😉 , for this all credit goes to 🐍 so take Premium 👽 because for premium users same bot is developed in C ➕➕")
#             except Exception as e:
#                 logger.error(f"Error uploading video: {e}")
#             finally:
#                 safe_remove(file_path)  # Safely delete the video file after uploading
#         else:
#             await update.message.reply_text("An error occurred while downloading the video.")
#     else:
#         await update.message.reply_text("Please provide a valid URL.")
#         await update.message.reply_text("Example: /download https://www.youtube.com/watch?v=dQ")

# Updated version of /download_command -> Adding command handler
# stages - only one stage in this particular case
YTURL = range(1)
async def download_command(update:Update, context:CallbackContext):
    await update.message.reply_text('✅ Please paste the copied url of your youtube video 🔗')
    await update.message.reply_text('❌ Use the /cancel command if you dont want to download a video and accidentally clicked the download command, but once you paste the link, the bot will start fetching the video...')

    return YTURL # bot waits to get the url

async def get_url(update:Update, context:CallbackContext):
    entered_url = update.message.text

    # Now this part written below is same as /download_command (with little modification)
    try:
        print(entered_url)
        initial_time = datetime.datetime.now()
        await update.message.reply_text("Fetching 👨‍💻.....")
        await asyncio.sleep(4)  # Wait for 2 seconds
        await update.message.reply_text("Downloading 👩‍💻.....")
        video, file_path, file_name = await Download(entered_url)
        if video:
            await update.message.reply_text("🖐️ Ruko Zara Sabr Karo 💁‍♂️💁‍♀️ Uploading Video......")
            try:
                await update.message.reply_video(video, caption=file_name)
                final_time = datetime.datetime.now()
                download_time = final_time - initial_time
                download_time_seconds = download_time.total_seconds()
                download_time_formatted = f"{download_time_seconds:.2f}"
                await update.message.reply_text(f"Download just took --> {download_time_formatted} seconds")
                await update.message.reply_text("If you have any issues with download speed or video quality then take premium 😉 , for this all credit goes to 🐍 so take Premium 👽 because for premium users same bot is developed in C ➕➕")
            except Exception as e:
                logger.error(f"Error uploading video: {e}")
            finally:
                safe_remove(file_path)  # Safely delete the video file after uploading
                return ConversationHandler.END

        else:
            await update.message.reply_text("An error occurred while downloading the video.")
            return ConversationHandler.END

    except:
        await update.message.reply_text("Please provide a valid URL.")
        return ConversationHandler.END

async def cancel(update:Update, context:CallbackContext):
    await update.message.reply_text('Downloading process cancelled 🥲')
    return ConversationHandler.END
        
async def Download(url):
    # Configure yt-dlp options
    ydl_opts = {
       'outtmpl': '%(title)s.%(ext)s',  # Name the file as the video title
        'format': 'best',  
        'quiet': True,  # Suppress verbose output
        'no_warnings': True,   
        'noprogress': True  # Suppress progress bar
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Extract and download video information
            info_dict = ydl.extract_info(url, download=True)

            # Construct the file path
            file_name = ydl.prepare_filename(info_dict)
            file_path = os.path.abspath(file_name)

            # Ensure file path is valid and free of null characters
            if '\0' in file_path:
                raise ValueError("File path contains null character.")

            # Read the video file into a variable
            with open(file_path, 'rb') as file:
                video = file.read()
            return video, file_path, file_name
        except ValueError as ve:
            logger.error(f"Invalid file path: {ve}")
            return None, None
        except Exception as e:
            logger.error(f"An error occurred during download: {e}")
            return None, None

def safe_remove(file_path):
    try:
        if isinstance(file_path, str):
            os.remove(file_path)
            logger.info(f"Deleted temporary file: {file_path}")
        else:
            raise ValueError(f"Invalid file_path type: {type(file_path)}")
    except ValueError as ve:
        logger.error(f"Error deleting file: {ve}")
    except Exception as e:
        logger.error(f"Error deleting file: {e}")


# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     logger.warning(f'Update {update} caused error {context.error}')
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text="Error in downloading the video..."
#     )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}" ')

    if message_type == 'group':
        if BOT_USERNAME in text.split()[0]:  # Check if bot's username is mentioned at the beginning of the message
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
            await update.message.reply_text(response)
        else:
            return
    else:
        response: str = handle_response(text)
        await update.message.reply_text(response)
        if response == 'I am unable to understand what you wrote. Please use /help to see available commands.':
            await update.message.reply_text("To download a video, please use /download followed by a YouTube URL of the video.")
    print('Bot: ', response)
        
def handle_response(text: str)-> str:
    proccesed : str = text.lower()
    emoji_list = ['👩‍💻', '😙', '😗', '🙂', '🤗', '🤐', '🤔', '😚', '🫡', '🤨', '😐', '😑', '😶', '🫥', '🙄', '😏' '😣', '😮', '😯', '😪','😫','🥱','😴','😌','😛','😜','😝','🤤','😒','😓','😔','😕','🫤','🙃','🫠','🤑','😲','☹️','🙁','😖','😞','😟','😦','😭','😧','😨','😬','😮‍💨','😰','😳','🤪','😵','😵‍💫','🥴','😠','😡','🤬','😷','🤒','😇','🥳','🥸','🥺','🥹','🤠','🤡','🤥','🫢','🫣','🧐','🤓','☠️','😈','👹','👺','👽','👾','☠️','💩','😺','😸','😹','😻','😼','😽','🙀','🙉','🙊','🐵','🐶','🐺','🦊','🐯','🦁','🐮','🦝', '☺️', '😏']
    num = random.randint(0, len(emoji_list)-1)
    responses = {
        "hi": "Hey Nice to meet you I am a Video Downloader Bot 🤖",
        "hello": "Hello dude what's up everything fine ?",
        "yupp": "Nice to hear that Sir keep growing!",
        "yes": "Nice to hear that Sir keep growing!",
        "doing": "Nothing just managing the Youtube Servers",
        "noice": "Hmmmm 🫥",
        "nice": "Hmmmm 🫥",
        "😂": "😂🤣😂",
        "😭": "😭🤕🥹",
        "💀": "💀👻🫥",
        "🥹": "🥹👍🥹",
        "😎": "😎👊😥",
        "🤩": "😎👊😎",
        "🤖": "🤖👍🍼",
        "🫥": "🫥👍🧐",
        "🥶": "🥶🥹😭",
        "🧐": "🧐👀😭",
        "😥": "😥🤕💀",
        "🥱": "🥱😴😴",
        "🤣": "🤣😂👍",
        "😁": "😁👍😎",
        "😆": "😆🤣😂",
        "😍": "😘😘😘",
        "🥰": "😊😊😊",
        "😘": "😘🥰😘",
        "stop": "💀oky🤣",
        "🍼": "👶🐤🐥"
    }
    # Check if the processed text is in the predefined responses
    if proccesed in responses:
        return responses[proccesed]
    
    # Check if the processed text is an emoji from the emoji_list
    if proccesed in emoji_list:
        return emoji_list[num]
    
    # Default response if no matches found
    return 'I am unable to understand what you wrote. Please use /help to see available commands.'
    

if __name__ == "__main__":
    print("Starting bot...")
    
    ######## Initializing Application with our Telegram Token
    app = Application.builder().token(TOKEN).read_timeout(30).write_timeout(30).build()

    ######## Adding Conversation Handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("download", download_command)],
        states={
            YTURL: [MessageHandler((filters.TEXT & ~filters.COMMAND), get_url)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    app.add_handler(conv_handler)
  
    ######## Adding Command Handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    # app.add_handler(CommandHandler('download', download_command))
    app.add_handler(CommandHandler('info', info_command))
    app.add_handler(CommandHandler('bored', bored_command))
    
    ######## Adding Message Handlers
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    ######## Add Error Handlers
    # app.add_error_handler(error)

    ######## Polling the Bot
    # print('Polling...')
    app.run_polling(poll_interval=2)  # check for new messages updates every 2 seconds
