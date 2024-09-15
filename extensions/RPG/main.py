import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import discord
from discord.ext import commands
from MainFunction import PermissionCheck,SetUp
from extensions.RPG import Account

class RPG(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def register(self,ctx: discord.Message):
        print(f'{ctx.author.name} request for registering')
        r=Account.register(ctx.author.name)
        print(r)
        if r:
            await ctx.reply(f'Register Successful! Register as {ctx.author.name}!')
        else:
            await ctx.reply(f'Register Fail! You have already registered as {ctx.author.name}')


async def setup(bot: commands.Bot):
    await bot.add_cog(RPG(bot))

