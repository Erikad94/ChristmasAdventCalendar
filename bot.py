# bot.py
import os
import datetime

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    movies = ["Die hard",
        "Lethal weapon",
        "Gremlins",
        "The christmas chronicles",
        "The grinch",
        "Klaus",
        "Arthur christmas",
        "Home alone",
        "Rise of the guardians",
        "Santa clause",
        "Santa clause 2",
        "Love actually",
        "Beauty and the beast enchanted christmas",
        "Nightmare before christmas",
        "The polar express",
        "Jingle all the way",
        "A christmas story",
        "Chrostmas with the kranks",
        "Its a wonderful life",
        "Garfield christmas movie",
        "The man who invented christmas",
        "Tokyo godfathers",
        "Joyeux noel",
        "Rudolph the Red-Nosed Reindeer",
        "Christmas chronicles 2"]

    today = datetime.datetime.now().day
    month = datetime.datetime.now().month
    count = 1
    if message.content == 'ChristmasMovieForToday':
        if month ==12:
            for movie in movies:
                if count == today:
                    message = "Today is a wonderful christmasy day, you should watch " + movie
                    await message.channel.send(message)
                    break
                else:
                    count+=1
                if count > 25:
                    await message.channel.send("Sadly it is not christmas yet")
                    break
        else:
            await message.channel.send("Sadly it is not christmas yet")

client.run(TOKEN)