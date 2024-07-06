import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, CallbackQueryHandler

from config import BOT_TOKEN

global current_pool_type
global current_page

def get_pools_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("get api successfully!")
        data = response.json().get("data", {}).get("data", [])
        return data
    else:
        return []

def format_number(number):
    if number % 1 == 0:
        return "${:,.0f}".format(number)
    else:
        return "${:,.2f}".format(number)

def format_pool_info(pool):
    return (
        f"*🪙  Token:* {pool['mintA']['symbol']}/{pool['mintB']['symbol']}\n"
        f"*Liquidity:* {format_number(pool['tvl'])}\n"
        f"*24h Volume:* {format_number(pool['day']['volume'])}\n"
        f"*24h Fee:* {format_number(pool['day']['volumeFee'])}\n"
        f"*24h APR:* {pool['day']['apr']}%\n"
    )

def get_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Back", callback_data='back'),
            InlineKeyboardButton("Next", callback_data='next')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def send_pools(update: Update, context: CallbackContext, pool_type: str) -> None:
    url = f'https://api-v3.raydium.io/pools/info/list?poolType={pool_type}&poolSortField=default&sortType=desc&pageSize=5&page={current_page}'
    pools = get_pools_data(url)
    await update.message.reply_text(f"{pool_type} liquidity pools in page {current_page}:\n" + "\n".join(format_pool_info(pool) for pool in pools),
                                    reply_markup=get_keyboard(), 
                                    parse_mode="Markdown")

async def all_pools(update: Update, context: CallbackContext) -> None:
    global current_page
    global current_pool_type
    
    current_page = 1
    current_pool_type = "all"

    await send_pools(update, context, current_pool_type)

async def concentrated_pools(update: Update, context: CallbackContext) -> None:
    global current_page
    global current_pool_type

    current_page = 1
    current_pool_type = "concentrated"

    await send_pools(update, context, current_pool_type)

async def standard_pools(update: Update, context: CallbackContext) -> None:
    global current_page
    global current_pool_type

    current_page = 1
    current_pool_type = "standard"

    await send_pools(update, context, current_pool_type)

async def button(update: Update, context: CallbackContext) -> None:
    global current_page
    global current_pool_type

    current_pool_type = current_pool_type

    query = update.callback_query

    if query.data == 'back':
        current_page = max(1, current_page - 1)
    elif query.data == 'next':
        current_page += 1

    await query.answer()
    await send_pools(query, context, current_pool_type)

def main() -> None:
    # BOT_TOKEN in config.py
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("allpools", all_pools))
    application.add_handler(CommandHandler("concentratedpools", concentrated_pools))
    application.add_handler(CommandHandler("standardpools", standard_pools))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()
