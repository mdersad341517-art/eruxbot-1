from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters

TOKEN = "8436372151:AAHSa2Fj0e0oT2SVe-ZFYJzcRwvR20AmP6E"

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    buttons = [
        [InlineKeyboardButton("📢 Updates", url="https://t.me/eruxmusic_bot")],
        [InlineKeyboardButton("👑 Owner", url="https://t.me/IAS_Roy")],
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    text = """
╔═══『 ERU X BOT 』═══╗
✨ Fast • Smart • Stylish
🎵 Music • Fun • Utility
╚══════════════════╝

😎 Welcome bro!

Use /help to see commands.
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

# HELP
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    help_text = """
╔═══〔 📌 ERU X HELP 📌 〕═══╗

🎵 /start → Start Bot
⚡ /alive → Bot Status
🆔 /id → Your Telegram ID
🏓 /ping → Bot Speed
💎 /quote → Motivation
😂 /roast → Funny Roast
📂 /menu → Open Main Menu

╚══════════════════════╝
"""

    await update.message.reply_text(help_text)

# PING
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! Bot Online 😎")

# ID
async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 Your Telegram ID:\n{update.effective_user.id}"
    )
# ALIVE
async def alive(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
⚡ ERU X BOT IS ALIVE ⚡

🤖 Status : Online
🚀 Speed : Fast
🔥 Mode : Active
👑 Owner : @eruhacker
"""

    await update.message.reply_text(text)
    
# QUOTE
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):

    quotes = [
        "😎 Winners never quit.",
        "🔥 Consistency beats talent.",
        "🚀 Focus on your mission."
    ]

    import random
    await update.message.reply_text(random.choice(quotes))
# FUN
async def roast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "😂 Bro's internet runs on potato power."
    ) 
# WELCOME
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):

    for member in update.message.new_chat_members:

        text = f"""
╔═══〔 👋 WELCOME 👋 〕═══╗

✨ Welcome {member.first_name}
🎵 To ERU X MUSIC BOT GROUP

😎 Enjoy your stay brooo 🔥

╚══════════════════════╝
"""

        await update.message.reply_text(text)    
# MENU
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    buttons = [

        [InlineKeyboardButton("🎵 Music", callback_data="music")],

        [InlineKeyboardButton("😂 Fun", callback_data="fun")],

        [InlineKeyboardButton("👑 Owner", url="https://t.me/IAS_Roy")]

    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    text = """
╔═══〔 ⚡ ERU X MENU ⚡ 〕═══╗

🤖 Welcome To Main Menu

🔥 Choose Any Option Below 😎

╚══════════════════════╝
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )
# BUTTON REPLY
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "music":

        buttons = [

            [InlineKeyboardButton("▶️ Play", callback_data="play")],

            [InlineKeyboardButton("⏸ Pause", callback_data="pause")],

            [InlineKeyboardButton("⏹ Stop", callback_data="stop")]

        ]

        reply_markup = InlineKeyboardMarkup(buttons)

        await query.message.reply_text(

            "🎵 MUSIC CONTROL PANEL 😎🔥",

            reply_markup=reply_markup
        )

    elif query.data == "play":

        await query.message.reply_text(
            "▶️ Playing Music Soon 😎🔥"
        )

    elif query.data == "pause":

        await query.message.reply_text(
            "⏸ Music Paused 😎"
        )

    elif query.data == "stop":

        await query.message.reply_text(
            "⏹ Music Stopped 😎"
        )

    elif query.data == "fun":

        buttons = [

            [InlineKeyboardButton("😂 Joke", callback_data="joke")],

            [InlineKeyboardButton("💀 Roast", callback_data="roastbtn")],

            [InlineKeyboardButton("🎲 Random", callback_data="random")]

        ]

        reply_markup = InlineKeyboardMarkup(buttons)

        await query.message.reply_text(

            "😂 FUN MENU ACTIVATED 😎🔥",

            reply_markup=reply_markup
        )

    elif query.data == "joke":

        await query.message.reply_text(
            "😂 Joke: Python bhi kabhi kabhi emotional ho jata 😎"
        )

    elif query.data == "roastbtn":

        await query.message.reply_text(
            "💀 Roast: Bro installs bugs faster than apps 😂"
        )

    elif query.data == "random":

        await query.message.reply_text(
            "🎲 Random Luck: 69% 😎🔥"
        )       
# MAIN
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("id", myid))
app.add_handler(CommandHandler("quote", quote))
app.add_handler(CommandHandler("roast", roast))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(
    MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
)
app.add_handler(CommandHandler("alive", alive))
print("🤖 ERU X BOT RUNNING...")
app.run_polling()