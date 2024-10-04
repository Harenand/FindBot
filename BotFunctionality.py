from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
import ollama 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("/start"), KeyboardButton("/help")],
        [KeyboardButton("/newPicture"), KeyboardButton("/findInfo")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Привет! Выберите команду:", reply_markup=reply_markup)

async def help_command(update, context):
    await update.message.reply_text("Я умею выполнять следующие команды:\n"
                                   "/start - запустить бота\n"
                                   "/help - показать эту справку\n"
                                   "/newPicture - Генерация картинки\n"
                                   "/findInfo - Выполнить поисковой запрос")

async def create_picture(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Генирирую каритинку в Кандинском...")


async def implement_search(update, context):
    await update.message.reply_text("Выполнятестя поиск релевантных результатов...")

async def bot_talking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = ollama.chat(model='akdengi/saiga-llama3-8b', messages=[
  {
    'role': 'user',
    'content': f'{update.message.text}',
  },
    ])
   # print(response['message']['content'])
    await update.message.reply_text(response['message']['content'])

# ollama run akdengi/saiga-llama3-8b