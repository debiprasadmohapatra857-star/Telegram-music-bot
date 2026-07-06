from telegram import Update
from telegram.ext import Application,CommandHandler,ContextTypes
import os
TOKEN=os.environ['BOT_TOKEN']
async def start(u:Update,c:ContextTypes.DEFAULT_TYPE): await u.message.reply_text('Music bot ready! Use /help')
async def help_cmd(u,c): await u.message.reply_text('/start\n/search <song>\n/play <song>')
async def placeholder(u,c): await u.message.reply_text('Implement your music search here.')
app=Application.builder().token(TOKEN).build();app.add_handler(CommandHandler('start',start));app.add_handler(CommandHandler('help',help_cmd));app.add_handler(CommandHandler('search',placeholder));app.add_handler(CommandHandler('play',placeholder));app.run_polling()