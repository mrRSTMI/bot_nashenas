from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ContextTypes,

)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("لینک ناشناس من ", callback_data="button_1"),
         InlineKeyboardButton("Button 2", callback_data="button_2")],
        [InlineKeyboardButton("Button 3", callback_data="button_3")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("سلام به بات ناشناس خوش امدین \n برای استفاده از بات میتونین از دکمه های زیر استفاده کنین", reply_markup=reply_markup )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quary = update.callback_query
    await quary.answer()
    if quary.data == "button_1":
        await quary.edit_message_text("You pressed Button 1")
    elif quary.data == "button_2":
        await quary.edit_message_text("You pressed Button 2")
    elif quary.data == "button_3":
        await quary.edit_message_text("You pressed Button 3")

