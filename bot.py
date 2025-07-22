import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("7302955068:AAGjW6cwB3Jj12tKrRtOkftIpBpWRXCoxP0")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot now running on Render!")

async def song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Here's your song!")
    await update.message.reply_audio(audio=open("song.mp3", "rb"))

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("song", song))

if __name__ == "__main__":
    print("Bot is running…")
    app.run_polling()
