import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx, s1=5, s2=0):
    await ctx.send(s1+s2)   

@bot.command()
async def carpma(ctx,s3=4, s4=0):
    await ctx.send(s3*s4)    

@bot.command()
async def yazitura(ctx,tahmin):
    a=["yazı","tura"]
    b=random.choice(a)
    if tahmin==b:
        await ctx.send("doğru tahmin ettin")
    else:
        await ctx.send(f"yanlış tahmin ettin, cevap {b}")




bot.run("TOKEN")
