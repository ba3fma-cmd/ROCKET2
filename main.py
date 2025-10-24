import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from telegram import WebAppInfo

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class RocketCasinoBot:
    def __init__(self, token: str):
        self.token = token
        self.application = Application.builder().token(token).build()
        
        # Обработчики команд
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("game", self.game))
        self.application.add_handler(CallbackQueryHandler(self.button_handler))
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик команды /start"""
        keyboard = [
            [InlineKeyboardButton("🎮 Играть в Rocket Casino", web_app=WebAppInfo(url="https://your-domain.com/index.html"))],
            [InlineKeyboardButton("📊 Статистика", callback_data="stats")],
            [InlineKeyboardButton("ℹ️ Правила", callback_data="rules")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🚀 Добро пожаловать в Rocket Casino!\n\n"
            "Игра Crash с выводом в TON\n"
            "Нажмите кнопку ниже чтобы начать играть!",
            reply_markup=reply_markup
        )
    
    async def game(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Прямой запуск игры"""
        keyboard = [
            [InlineKeyboardButton("🚀 Запустить Rocket Casino", web_app=WebAppInfo(url="https://your-domain.com/index.html"))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🚀 Запускаем Rocket Casino...",
            reply_markup=reply_markup
        )
    
    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик нажатий на кнопки"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "stats":
            await query.edit_message_text("📊 Статистика будет доступна в мини-приложении")
        elif query.data == "rules":
            await query.edit_message_text(
                "🎯 Правила игры:\n\n"
                "1. Сделайте ставку в TON\n"
                "2. Ракетка взлетает с множителем от 1.00x\n"
                "3. Заберите выигрыш до того как ракетка взорвется\n"
                "4. Если успели - получаете ставку × множитель\n"
                "5. Если не успели - теряете ставку\n\n"
                "Удачи! 🚀"
            )

    def run(self):
        """Запуск бота"""
        self.application.run_polling()

if __name__ == "__main__":
    # Замените на ваш токен бота
    BOT_TOKEN = "8296175219:AAEFCZN5Y6T9sIrX9zc3fPjSU-qt2bKeEng"
    
    bot = RocketCasinoBot(BOT_TOKEN)
    bot.run()