from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import os
TOKEN = os.environ.get("TOKEN")

async def accueillir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for membre in update.message.new_chat_members:
        prenom = membre.first_name
       await update.message.reply_text(f"Bonjour {prenom} c'est un plaisir de t'avoir parmi nous ! 😊\n\nBienvenue dans cette communauté à but d'entraide et de recherche, je t'invite désormais à consulter les différentes rubriques.\nSi tu as quelconques questions n'hésite pas ! 🔥")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, accueillir))

print("Bot démarré...")
app.run_polling()
