from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8606061066:AAFsy5tny55nbzrfCxsUm2HVjLcFIk4aDDo"

async def accueillir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for membre in update.message.new_chat_members:
        prenom = membre.first_name
        await update.message.reply_text(f"👋 Bienvenue {prenom} ! Heureux de t'avoir parmi nous.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, accueillir))

print("Bot démarré...")
app.run_polling()
