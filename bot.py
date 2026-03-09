from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "8714743719:AAHyTwRGTknZVjjFmNv95B1fh2S4G4X-dXw"
SAHABOT_FILE_ID = "BQACAgQAAxkBAAMuaa8KgOceAweFTPwxUfktTc4XFPcAAukcAALzNnlR44QOsTOI9pY6BA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📥 APK İndir", callback_data="apk_indir")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Sahabot+'a hoş geldin!\n\nGüncel APK'yı indirmek için butona tıkla.",
        reply_markup=reply_markup
    )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "apk_indir":
        await query.message.reply_text("⏳ Gönderiliyor...")
        await query.message.reply_document(
            SAHABOT_FILE_ID,
            caption="✅ Sahabot+ Güncel Sürüm"
        )

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        file_id = update.message.document.file_id
        print("\nYENİ FILE ID:\n", file_id)
        await update.message.reply_text(f"`{file_id}`", parse_mode="Markdown")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_button))
app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))

print("BOT CALISIYOR...")
app.run_polling()
