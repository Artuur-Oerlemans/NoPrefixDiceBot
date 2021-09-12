import discord
import os
from keep_alive import keep_alive
from service.message_handler import detect_commands

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await detect_commands(message)

keep_alive()
client.run(os.environ['TOKEN'])
