import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)
# client = commands.Bot(command_prefix='!', intents=intents)

TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print(f'logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(f"received message:{message.content}")

    if message.content.strip() == '!ping':
        print("Pong command received") 
        await message.channel.send('Pong!')

    if message.content.strip() == '!roast':
        print("roast command received")
        await message.channel.send('Time to lubricant you!')

    if message.content.startswith('!meme'):
        print("meme command received")
        # heres where the api comes in 
        response = requests.get('http://127.0.0.1:5000/meme')

        if response.status_code == 200:
            meme_data = response.json()
            meme_url = meme_data['url']
            # embed for image
            meme_filename = os.path.basename(meme_url)
            await message.channel.send(file=discord.File(f'static/memes/{meme_filename}'))
            # embed = discord.Embed()
            # embed.set_image(url=meme_url)
            # await message.channel.send(meme_url)
        else:
            print(f"Error fetching meme: {response.status_code}")
            await message.channel.send("Sorry cant fetch a meme rn")

client.run(TOKEN)


