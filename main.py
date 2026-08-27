from decimal import Context

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = "8801650232:AAHeSRK9mPWeRzxcYmFQQypplz8zXZ7drLs"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm a bot that ")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message)
    await update.message.reply_text(update.message.text)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


print("Bot is running...")
app.run_polling()
