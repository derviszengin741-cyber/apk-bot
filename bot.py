from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "8714743719:AAHyTwRGTknZVjjFmNv95B1fh2S4G4X-dXw"
SAHABOT_FILE_ID = "BQACAgQAAxkBAAMuaa8KgOceAweFTPwxUfktTc4XFPcAAukcAALzNnlR44QOsTOI9pY6BA"

KURULUM = """📲 Kurulum Adımları

1. APK'yı İndir
Az önce gönderilen APK dosyasını telefonuna indir.

2. Kuruluma İzin Ver
Telefon "Bilinmeyen kaynak" uyarısı verirse:
→ Ayarlar → Güvenlik → Bilinmeyen kaynaklara izin ver ✅

3. APK'yı Kur
İndirilen dosyaya tıkla → Yükle → Aç

4. Giriş Yap
Sana verilen kullanıcı adı ve şifreyi gir.

5. Başlat
▶ Başlat butonuna bas, uygulama çalışmaya başlar."""

NASIL_CALISIR = """⚙️ Sahabot+ Nasıl Çalışır?

🔄 İş Havuzu Taraması
Uygulama sürekli olarak Trendkargo iş havuzunu kontrol eder.

✅ Otomatik Kabul
Uygun iş bulduğunda saniyeler içinde otomatik kabul eder.

⏱ Bekleme Süresi
Her kabulden sonra 10 saniye bekler, sonra tekrar tarar.

🛑 Durdurma
İstediğin zaman ■ Durdur butonuna basarak durdurabilirsin.

⚠️ UYARI
Start/Stop butonlarını sadece işlem havuzunda kullanın. İşlemlere geçtiğinizde Start basılı olmasın!"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📥 Güncel APK'yı İndir", callback_data="apk_indir")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Sahabot+'a Hoş Geldin!\n\nGüncel APK'yı indirmek için aşağıdaki butona tıkla.",
        reply_markup=reply_markup
    )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "apk_indir":
        await query.message.reply_document(
            SAHABOT_FILE_ID,
            caption="✅ Sahabot+ Güncel Sürüm"
        )
        await query.message.reply_text(KURULUM)
        await query.message.reply_text(NASIL_CALISIR)

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        file_id = update.message.document.file_id
        print("\nYENİ FILE ID:\n", file_id)
        await update.message.reply_text(f"FILE ID: {file_id}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_button))
app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))

print("BOT CALISIYOR...")
app.run_polling()
