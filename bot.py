from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8714743719:AAHyTwRGTknZVjjFmNv95B1fh2S4G4X-dXw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Sahabot+'a Hoş Geldin!\n\nBOT İLE ALAKALI PROBLEM YAŞIYORSANIZ İLETİŞİME GEÇİNİZ @diyojen5"
    )

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        file_id = update.message.document.file_id
        print("\nYENİ FILE ID:\n", file_id)
        await update.message.reply_text(f"FILE ID: {file_id}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))
print("BOT CALISIYOR...")
app.run_polling()
