
import discord
import os
from dotenv import load_dotenv
from fetch_data import get_random_summary

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

token = os.getenv('BOT_TOKEN')


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Quote'):
        summary = get_random_summary()
        await message.channel.send("## " + f"*{summary['random_quote'].strip()}*" + "\n```" + f"\nKirja: {summary['title']}" + f"\nKirjailija: {summary['author']}" + f"\nKirjan arvosana: ({summary['rating']}/5)" + "\n```" + "\n**[Kirjan tiivistelmä](https://blog-nextjs-three-nu.vercel.app/books)**")

client.run(token)
