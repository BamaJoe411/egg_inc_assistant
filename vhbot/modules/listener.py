"""
Handles the API
"""

import asyncio
import json
from aiohttp import web
import discord
from discord.ext import commands


class Listener(commands.Cog):

    def __init__(self, bot):
        self.site = None
        self.bot = bot

    async def webserver(self):
        async def ping(request: web.Request) -> web.Response:
            response_obj = {'status': 'success', 'message': 'pong'}
            return web.Response(text=json.dumps(response_obj), status=200)
        app = web.Application()
        app.router.add_post('/ping', ping)
        runner = web.AppRunner(app)
        await runner.setup()
        self.site = web.TCPSite(runner, '0.0.0.0', 8080)
        await self.bot.wait_until_ready()
        await self.site.start()


    def __unload(self):
        asyncio.ensure_future(self.site.stop())


async def setup(bot: commands.Bot) -> None:
    listener = Listener(bot)
    await bot.add_cog(listener)
    await bot.loop.create_task(listener.webserver())
