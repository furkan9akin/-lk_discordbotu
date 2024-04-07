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
async def topla(ctx, a=0,b=0):
    await ctx.send(a+b)

@bot.command()
async def çıkar(ctx, a=0,b=0):
    await ctx.send(a-b)

@bot.command()
async def çarp(ctx, a=0,b=0):
    await ctx.send(a*b)

@bot.command()
async def böl(ctx, a=0,b=0):
    await ctx.send(a/b)

@bot.command()
async def üs_alma(ctx, a=0,b=0):
    await ctx.send(a**b)

@bot.command()
async def bölme_kalan(ctx, a=0,b=0):
    await ctx.send(a%b)

@bot.command()
async def zar_oyunu(ctx, a=0):
    x=random.randint(1,6)
    if x==a:
        await ctx.send("Doğru cevap")
    if x!=a:
        await ctx.send(f"Yanlış cevap. Doğru cevap {x} olmalıydı.")

@bot.command()
async def yazı_tura(ctx, a):
    a=a.lower()
    y=["yazı","tura","dik"]
    x=random.choice(y)
    if a==x:
        await ctx.send("Tutturdun.")
    else:
        await ctx.send(f"Tutturamadın, {x} olmalıydı.")

bot.run("")
