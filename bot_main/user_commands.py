import os
import sys
sys.path.append(os.path.dirname(os.path.abspath("file")))
from aiogram.enums import ParseMode
from aiogram import Router,types
from aiogram.types import Message,ReplyKeyboardRemove 
from aiogram.utils import markdown

from aiogram.filters import Command,CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from aiogram import Dispatcher, types
from aiogram.types import Message

from Price_br.binance import get_binance
from Price_br.bitget import get_bitget
from Price_br.bybit import get_bybit
from Price_br.kraken import get_kraken
from Price_br.okx import get_okx

router = Router(name = __name__) 

class CoinFSM(StatesGroup):
    waiting_for_coin = State()

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Для получения цен на криптовалюту введите /get_price.")

@router.message(Command('get_price'))
async def cmd_get_price(message: types.Message,  state: FSMContext):
    await message.answer("Введите имя монеты:")
    await state.set_state(CoinFSM.waiting_for_coin)

@router.message(CoinFSM.waiting_for_coin)
async def process_coin_name(message: types.Message, state: FSMContext):
    coin_name = message.text.upper()
    await state.update_data(coin_name=coin_name)

    
    prices = {
        "Binance": get_binance(coin_name),
        "Bitget": get_bitget(coin_name),
        "Bybit": get_bybit(coin_name),
        "Kraken": get_kraken(coin_name),
        "Okx": get_okx(coin_name),
    }

    
    for exchange, price in prices.items():
        if price is not None:
            await message.answer(f"{exchange}: {price}")
        else:
            await message.answer(f"{exchange}: Sorry, the coin isn't here.")

    await state.clear()

