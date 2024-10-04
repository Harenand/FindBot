from BotFunctionality import *


if __name__ == "__main__":
    application = ApplicationBuilder().token("7547777250:AAHQHE_IG1QY70aIwBXTuQ2WIEvt3JrFlxE").build()
    
    # application.add_handler(MessageHandler(filters.TEXT, bot_talking))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("newPicture", create_picture))
    application.add_handler(CommandHandler("findInfo", implement_search))
    
    application.run_polling()

   






# import logging
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
# # 7547777250:AAHQHE_IG1QY70aIwBXTuQ2WIEvt3JrFlxE

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )

# async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     str = update.message.text
#     await context.bot.send_message(chat_id=update.effective_chat.id, text= f"Hello! I'm your SmartAI seacher! You've written: {str}")


# async def start(update, context):
#     await update.message.reply_text("Привет! Что ты хочешь сделать?")



# if __name__ == '__main__':
#     application = ApplicationBuilder().token('7547777250:AAHQHE_IG1QY70aIwBXTuQ2WIEvt3JrFlxE').build()
#     #application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.TEXT, answer))
#     application.run_polling()

