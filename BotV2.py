import discord
import random
import os
import requests
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
async def Reciclar(ctx,*, tipo):
    if tipo  == "Carton Sucio" or tipo == "Pan Mojado":
        await ctx.send("No se puede Reciclar, tiralo en el tacho de basura mas cercano")
    elif tipo  == "Cascaras" or tipo == "Papel":
        await ctx.send("Si se puede reciclar, usa las cascaras de abono para las plantas y el Papel Mojalo para volverlo una masa eso lo pegas en una pared bien aplastado para que se seque y lo puedas volver a usar ")
    elif tipo == "Potes de Plastico" or tipo == "Botellas de Plastico":
        await ctx.send("Los podes usar para guardar cosas, y podes usar una botella de plastico q usaste para tomar agua denuevo mientras no este rota  ")
        
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
    
@bot.command()
async def meme(ctx):
    Lista_imagenes = os.listdir('Images')
    with open(f'Images/{random.choice(Lista_imagenes)}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("Tu Token Aquí")
