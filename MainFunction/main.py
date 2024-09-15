import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import discord
from discord.ext import commands
from MainFunction import PermissionCheck, SetUp

class main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        print()
        print(f'<Sever:{message.guild},Channel:{message.channel},User:{message.author},Time:{message.created_at},Time(last edited):{message.edited_at},ID:{message.id}>')
        if message.reference:
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            print(f'Reply to {replied_message.author}\nMessage Link_URL:{replied_message.jump_url}')
        print(f'{message.content}')
        print()
        for embed in message.embeds:
            print(embed.title)
            print(embed.description)
            for field in embed.fields:
                print(field.name, field.value)
        for attachment in message.attachments:
            print(attachment.filename)
            print(attachment.url)
            print(attachment.size)
        print(f'Message Link_URL:{message.jump_url}')
        print()

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Unknown command. Please use `>help` for a list of commands.")

    @commands.command()
    async def help(self, ctx: commands.Context):
        with open(r'K:\Megumin\data\help.txt', 'r') as f:
            helpmessage = f.read()
        await ctx.send(helpmessage)

    @commands.command()
    async def changelog(self, ctx: commands.Context, Version: str):
        try:
            with open(fr'K:\Megumin\changelog\changelog {Version}.txt', 'r', encoding='utf-8') as f:
                changelog = f.read()
            await ctx.send(changelog)
        except Exception:
            await ctx.send(f'Version {Version} not found, or your syntax is incorrect!')

    @commands.command()
    async def changeloglist(self,ctx):
        print('Load Changelog List...')
        l='# Changelog List(Use `>changelog <Version>` to see details.):\n'
        files = [f for f in os.listdir(r'K:\Megumin\changelog') if os.path.isfile(os.path.join(r'K:\Megumin\changelog', f))]
        print(l,files)
        for i in files:
            l=l+'- '+i[10:16]+'\n'
        await ctx.send(l)

    @commands.command()
    async def set(self, ctx: commands.Context, category: str, options: str, value: str):
        print(f'{ctx.author.name} change {category} {options} to {value}')
        user_name = ctx.author.name
        if PermissionCheck.checkrole("Developer", user_name):
            result = SetUp.ChangeValue(category, options, value)
            await ctx.send(result)
            return
        await ctx.send("[Error] You don't have the permissions to do this.")

    @commands.command()
    async def checksetup(self, ctx: commands.Context, Category: str, Options: str):
        value = SetUp.CheckValue(Category, Options)
        if value is None:
            await ctx.send(f"[Error] No value in {Options} in {Category}! Use `>setuplist` to view all setups.")
        else:
            await ctx.send(f'The value in {Options} in {Category} is {value}.')

    @commands.command()
    async def setuplist(self, ctx: commands.Context):
        await ctx.send(SetUp.list())

async def setup(bot: commands.Bot):
    await bot.add_cog(main(bot))
