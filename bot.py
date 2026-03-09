from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# 👉 BOTFATHER TOKEN
TOKEN = "8714743719:AAHyTwRGTknZVjjFmNv95B1fh2S4G4X-dXw"

# 👉 GÜNCEL APK FILE ID
SAHABOT_FILE_ID = "BQACAgQAAxkBAAMuaa8KgOceAweFTPwxUfktTc4XFPcAAukcAALzNnlR44QOsTOI9pY6BA"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text == "sahabot güncel":
        if SAHABOT_FILE_ID == "":
            await update.message.reply_text("APK henüz yüklenmedi.")
        else:
            await update.message.reply_text("Sahabot+ Güncel Sürüm Gönderiliyor 📦")
            await update.message.reply_document(SAHABOT_FILE_ID)
    else:
        await update.message.reply_text("Yazmanız gereken: sahabot güncel")

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        file_id = update.message.document.file_id
        print("\nAPK FILE ID:\n", file_id)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))
print("BOT CALISIYOR...")
app.run_polling()
