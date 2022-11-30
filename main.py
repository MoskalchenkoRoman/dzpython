from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from sympy import Symbol, collect

app = ApplicationBuilder().token("5718064636:AAHbpdjPuYjdnG59GJftldVrV-34rriDgls").build()


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'ЧЁ хочу {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"""{update.effective_user.first_name}, 
                                        если хочешь сложить полиномы то вводи так:
                                        /poli_sum 1полином ПРОБЕЛ 2полином!""")
    
async def poli_sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    sum = update.message.text
    sum = sum.replace('/poli_sum', '').replace('^', '**').replace('x', '*x').replace('=0', '')
    a = sum.split()[0]
    b = sum.split()[1]
    x = Symbol('x')    
    poli = str(collect(a + '+' + b,x))
    await update.message.reply_text(poli)
    
app.add_handler(CommandHandler("hi", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("poli_sum", poli_sum))
print('Поперли')
app.run_polling()

