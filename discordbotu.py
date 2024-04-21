import discord
from discord.ext import commands
import random
import os
import requests

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

@bot.command()
async def sayi_tahmin_et(ctx,a=0):
    x=random.randint(1,100)
    if x==a:
        await ctx.send("Doğru bildin.")
    elif abs(a-x)<=50:
        await ctx.send(f"Tahminin doğru sayıya {abs(a-x)} uzaklığında.")
    else:
        await ctx.send("Doğru sayıya uzaksın.")

@bot.command()
async def meme(ctx):
    x=random.choice(os.listdir('discord_meme'))
    with open(f'discord_meme/{x}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command()
async def fox(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

#

def get_duck_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#    

def get_pikachu_image_url():    
    url = ' https://pokeapi.co'
    res = requests.get(url)
    data = res.json()
    return data['sprites']

@bot.command()
async def pikachu(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_pikachu_image_url()
    await ctx.send(image_url)

bot.run("")
