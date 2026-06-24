import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def Mateo(ctx, count_heh = 5):
    await ctx.send("Mateo" * count_heh)
    
@bot.command()
async def Bienvenido(ctx, pais):
    if pais  == "Japon":
        await ctx.send("Bienvenido al Server en Japon")
    elif pais  == "Argentina":
        await ctx.send("Bienvenido al Server en Argentina")
        
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

bot.run("token")
