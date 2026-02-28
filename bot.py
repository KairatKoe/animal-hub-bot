import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

MENU = ReplyKeyboardMarkup(
    [
        ["🐾 Нашли щенка/собаку", "💉 Прививки"],
        ["✂️ Стерилизация/кастрация", "🏥 Ветклиники"],
        ["🛍 Зоомагазины", "📢 Объявления"],
    ],
    resize_keyboard=True
)

TEXTS = {
    "🐾 Нашли щенка/собаку": "Если вы нашли щенка — обеспечьте безопасность, воду и осмотр в клинике.",
    "💉 Прививки": "Вакцинацию проводят в ветклиниках по возрасту и весу животного.",
    "✂️ Стерилизация/кастрация": "Процедура проводится в клинике. Первые 3 дня — покой и контроль шва.",
    "🏥 Ветклиники": "Раздел в разработке.",
    "🛍 Зоомагазины": "Раздел в разработке.",
    "📢 Объявления": "Объявления будут проходить через модерацию.",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я помощник по собакам и кошкам 🐾",
        reply_markup=MENU
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text in TEXTS:
        await update.message.reply_text(TEXTS[text], reply_markup=MENU)
    else:
        await update.message.reply_text(
            "Я отвечаю только по вопросам животных 🐾",
            reply_markup=MENU
        )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не найден")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
