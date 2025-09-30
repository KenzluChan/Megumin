import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import discord
from discord.ext import commands
from MainFunction import PermissionCheck, SetUp
from Chatterbot import setupbot

class Bot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # if message.author.id == self.bot.user.id:
        #     return

        await self.bot.process_commands(message)
            
        if not message.content.startswith('>'):
            if (SetUp.CheckValue("chatterbot", "autoreply") or message.channel.id == 1284795372061069364):
                try:
                    response = setupbot.get_bot_response(message.content)
                except Exception as e:
                    response = f"An error occurred: {str(e)}"
                    print(response)
                await message.reply(response)
        
    @commands.command()
    async def chatterbothelp(self, ctx: commands.Context):
        with open(r'extensions\Chatterbot\data\help', 'r') as f:
            helpmessage = f.read()
        await ctx.send(helpmessage)


    @commands.command()
    async def clearbotdata(self, ctx: commands.Context):
        user_name = ctx.author.name
        if not PermissionCheck.check("chatterbot", "userclearbotdata", "Developer", user_name):
            await ctx.send("[Error] You don't have the permissions to do this.")
            return
        await ctx.send(setupbot.clearbotdata())

    @commands.command()
    async def trainbot(self, ctx: commands.Context, language: str):
        user_name = ctx.author.name
        if not PermissionCheck.check("chatterbot", "usertrainbot", "Developer", user_name):
            await ctx.send("[Error] You don't have the permissions to do this.")
            return
        message=setupbot.trainbot(language)
        await ctx.send(message)

async def setup(bot: commands.Bot):
    await bot.add_cog(Bot(bot))
