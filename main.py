
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)

from handlers.start_handler import start, button_handler


TOKEN = "8801650232:AAHeSRK9mPWeRzxcYmFQQypplz8zXZ7drLs"





async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message)
    await update.message.reply_text(update.message.text)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


print("Bot is running...")
app.run_polling()
