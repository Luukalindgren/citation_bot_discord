
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

        formatted_message = (

            f"## *{summary['random_quote'].strip()}*\n"
            "```\n"
            f"Kirja: {summary['title']}\n"
            f"Kirjailija: {summary['author']}\n"
            f"Kirjan arvosana: ({summary['rating']}/5)\n"
            "```\n"
            "**[Kirjan tiivistelmä](https://blog-nextjs-three-nu.vercel.app/books)**"
        )

        await message.channel.send(formatted_message)

client.run(token)
