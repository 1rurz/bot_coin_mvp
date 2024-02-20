import os
import sys
sys.path.append(os.path.dirname(os.path.abspath("file")))
import asyncio
import logging
from aiogram.utils.chat_action import ChatActionSender
from aiogram import Bot, Dispatcher,types,Router
from dotenv import load_dotenv
from user_commands import router as user_router 


load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(user_router)




async def main():
    logging.basicConfig(level = logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

