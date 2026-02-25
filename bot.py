from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# 👉 BURAYA BOTFATHER'DAN ALDIĞIN YENİ TOKENI YAZ
TOKEN = "8714743719:AAHyTwRGTknZVjjFmNv95B1fh2S4G4X-dXw"

# 👉 APK FILE ID BURAYA GELECEK (ŞİMDİLİK BOŞ)
SAHABOT_FILE_ID = "BQACAgQAAxkBAAMCaZ7rVlLuA0krGBrV2UlTNUQ2Ot8AAvsfAAI_G_hQgtgzsRlk8u86BA"

# Kullanıcı mesajlarını yakalayan fonksiyon
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

# APK file_id yakalama fonksiyonu (SADECE SEN KULLANACAKSIN)
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        file_id = update.message.document.file_id
        print("\nAPK FILE ID:\n", file_id)

app = ApplicationBuilder().token(TOKEN).build()

# Mesajları dinle
app.add_handler(MessageHandler(filters.TEXT, handle_message))

# Dosya gönderilince file_id yakala
app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))

print("BOT CALISIYOR...")
app.run_polling()