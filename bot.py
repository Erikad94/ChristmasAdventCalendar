# bot.py
import os
import datetime
import random

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
        "Christmas with the kranks",
        "Its a wonderful life",
        "Garfield christmas movie",
        "The man who invented christmas",
        "Tokyo godfathers",
        "Joyeux noel",
        "Rudolph the Red-Nosed Reindeer",
        "Christmas chronicles 2",
        "Elf",
        "National Lampoons Christmas Vacation",
        "A Charlie Brown Christmas",
        "The Muppet Christmas Carol",
        "A Christmas Carol",
        "Miracle on 34th Street",
        "Scrooged",
        "Bad Santa",
        "Jack Frost",
        "Santa Claus Conquers the Martians"]

    links = [
        "https://www.justwatch.com/ca/movie/die-hard",
        "https://www.justwatch.com/ca/movie/lethal-weapon",
        "https://www.justwatch.com/ca/movie/gremlins",
        "https://www.justwatch.com/ca/movie/the-christmas-chronicles",
        "https://www.justwatch.com/ca/movie/how-the-grinch-stole-christmas",
        "https://www.justwatch.com/ca/movie/klaus",
        "https://www.justwatch.com/ca/movie/arthur-christmas",
        "https://www.justwatch.com/ca/movie/home-alone",
        "https://www.justwatch.com/ca/movie/rise-of-the-guardians",
        "https://www.justwatch.com/ca/movie/the-santa-clause",
        "https://www.justwatch.com/ca/movie/the-santa-clause-2",
        "https://www.justwatch.com/ca/movie/love-actually",
        "https://www.justwatch.com/ca/movie/beauty-and-the-beast-the-enchanted-christmas",
        "https://www.justwatch.com/ca/movie/the-nightmare-before-christmas",
        "https://www.justwatch.com/ca/movie/the-polar-express",
        "https://www.justwatch.com/ca/movie/jingle-all-the-way",
        "https://www.justwatch.com/ca/movie/a-christmas-story",
        "https://www.justwatch.com/ca/movie/christmas-with-the-kranks",
        "https://www.justwatch.com/ca/movie/its-a-wonderful-life",
        "https://www.youtube.com/watch?v=TbL-uxd4ZVw",
        "https://www.justwatch.com/ca/movie/the-man-who-invented-christmas",
        "https://www.justwatch.com/ca/movie/tokyo-godfathers",
        "https://www.justwatch.com/ca/movie/joyeux-noel",
        "https://www.justwatch.com/ca/movie/rudolph-the-red-nosed-reindeer",
        "https://www.justwatch.com/ca/movie/the-christmas-chronicles-2",
        "https://www.justwatch.com/ca/movie/elf",
        "https://www.justwatch.com/ca/movie/national-lampoons-christmas-vacation",
        "https://www.justwatch.com/ca/movie/a-charlie-brown-christmas",
        "https://www.justwatch.com/ca/movie/the-muppet-christmas-carol",
        "https://www.justwatch.com/ca/movie/a-christmas-carol",
        "https://www.justwatch.com/ca/movie/miracle-on-34th-street",
        "https://www.justwatch.com/ca/movie/scrooged",
        "https://www.justwatch.com/ca/movie/bad-santa",
        "https://www.justwatch.com/ca/movie/jack-frost",
        "https://www.justwatch.com/ca/movie/santa-claus-conquers-the-martians"]

    today = datetime.datetime.now().day
    month = datetime.datetime.now().month
    if message.content == 'ChristmasMovieBot Advent':
        if month ==12 and today < 26:
            message = message = "Today is a wonderful christmasy day, you should watch " + movies[today-1] + ". You can find out where to watch it here : " + links[today-1]
            await message.channel.send(message)
            break
        else:
            await message.channel.send("Sadly it is not christmas yet")

    if message.content == 'ChristmasMovieBot Random':
        rand = random.randint(0, len(movies)-2)
        message = "HoHoHo, you wanted a random Christmas movie here it is : " + movies[rand] + ". You can find out where to watch it here : " + links[rand]
        await message.channel.send(message)
        break

    if message.content == 'ChristmasMovieBot Weird':
        rand = random.randint(0, len(movies)-2)
        message = "Here is the weirdest christmas movie you can watch : " + movies[len(movies)-1] + ". You can find out where to watch it here : " + links[len(movies)-1]
        await message.channel.send(message)
        break

    if message.content == 'ChristmasMovieBot Help':
        message = "You have 3 options:\nChristmasMovieBot Advent : I Will give you the movie of the day.\nChristmasMovieBot Random : I will give you a random movie from my list.\nChristmasMovieBot Weird : I Will give you the weirdest Christmas movie I know."
        await message.channel.send(message)
        break

client.run(TOKEN)