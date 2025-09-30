import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents, help_command=None)
loadextensions=[]

@bot.event
async def on_ready():
    channel = bot.get_channel(1284795372061069364)
    if channel:
        await channel.send("Explosion!")
    print(f'Login Successfully!\nLogged in as {bot.user}')

async def load_main_cogs():
    global loadextensions
    loadextensions.append('MainFunction')
    await bot.load_extension('MainFunction.main')
    # await bot.load_extension('extensions.Chatterbot.main')


@bot.command()
async def load(ctx,name):
    global loadextensions
    if name in loadextensions:
        await ctx.send(f'{name} Extension has already been loaded!\nUse `>loaded` to see the loaded Function and Extensions.')
        return
    extension='extensions.'+name+'.main'
    try:
        await bot.load_extension(extension)
    except Exception as e:
        print(e)
        await ctx.send(f'Fail to load {name} Extensions!\n{name} Extensions is not found.\nUse `>extensionslist` to see the available extensions.')
        return
    loadextensions.append(name)
    await ctx.send(f'Load {name} Extensions successful!')

@bot.command()
async def unload(ctx,name):
    if name=='MainFunction':
        await ctx.send('[ERROR]MainFunction is not unloadable! (MainFunction is an important function in maintaining operations, unloading it may cause Megumin to lose normal operation.)')
    elif name in loadextensions:
        loadextensions.remove(name)
        name='extensions.'+name+'.main'
        await bot.unload_extension(name)
        await ctx.send(f'Unload {name} Extension successful!')
        return
    else:
        await ctx.send(f'{name} isn\'t loaded yet, or {name} is not found.\nUse `>loaded` to see the loaded Function and Extensions.')
    
@bot.command()
async def reload(ctx,name):
    if name not in loadextensions:
        await ctx.send(f'{name} Extension has not been loaded yet!\nUse `>loaded` to see the loaded Functions and Extensions.')
        return
    if name!='MainFunction' and name!='MF':
        name='extensions.'+name+'.main'
    else:
        name='MainFunction.main'
    try:
        await bot.unload_extension(name)
        await bot.load_extension(name)
    except Exception as e:
        print(e)
        await ctx.send(f'Fail to load {name} Extensions!\n{name} Extensions is not found.\nUse `>extensionslist` to see the available extensions.')
        return
    await ctx.send(f'Reload {name} Extensions successful!')

@bot.command()
async def loaded(ctx):
    ld='# Loaded Function and Extensions List:\n'
    for i in loadextensions:
        ld=ld+'- '+i+'\n'
    await ctx.send(ld)

@bot.command()
async def functionslist(ctx):
    l='# Available Extensions:\n'
    with open(r'.\data\extensionslist','r') as f:
        while True:
            n=f.readline()
            if n=='':
                break
            l=l+'- '+n+'\n'
            d=f.readline()
            l=l+'> '+d+'\n'
    await ctx.send(l)
        


async def start_bot():
    await load_main_cogs()
    await bot.start("")

asyncio.run(start_bot())


