import asyncio
import logging

import discord
from discord.ext import commands

from vhbot.config import config
from vhbot.modules import listener, slash_commands

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.all()

bot = commands.Bot(intents=intents, command_prefix=())


@bot.event
async def on_ready():

    await listener.setup(bot)
    await slash_commands.setup(bot)

    await bot.tree.sync()
    logging.info(f"{bot.user.name} Online")


async def main():
    async with bot:
        await bot.start(config.bot_token)


if __name__ == '__main__':
    asyncio.run(main())
