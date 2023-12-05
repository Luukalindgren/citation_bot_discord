
import discord
import os
from discord.ext import tasks
from dotenv import load_dotenv
from fetch_data import get_random_summary

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

token = os.getenv('BOT_TOKEN')


def format_quote(summary):
    formatted_message = (

        f"## *{summary['random_quote'].strip()}*\n"
        "```\n"
        f"Kirja: {summary['title']}\n"
        f"Kirjailija: {summary['author']}\n"
        f"Kirjan arvosana: ({summary['rating']}/5)\n"
        "```\n"
        "**[Kirjan tiivistelmä](https://blog-nextjs-three-nu.vercel.app/books)**"

    )

    return formatted_message


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    daily_quote.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Quote'):
        summary = get_random_summary()

        formatted_message = format_quote(summary)

        await message.channel.send(formatted_message)


@tasks.loop(hours=24)
async def daily_quote():
    await client.wait_until_ready()
    channel = client.get_channel(1181191090817216565)

    summary = get_random_summary()
    formatted_message = format_quote(summary)
    await channel.send(formatted_message)


client.run(token)
