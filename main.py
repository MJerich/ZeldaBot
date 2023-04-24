# main.py
import asyncio
import os
import discord
from helpers import onMessageHelper
from dotenv import load_dotenv
from discord.ext import commands

# import token from env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
command_prefix = os.getenv('COMMAND_PREFIX')

# set variables
cogsList = ['cog.standardCog', 'cog.remindCog', 'cog.openaiCog']
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
zeldaBot = commands.Bot(command_prefix=command_prefix, case_insensitive=True, help_command=None, intents=intents)


# set up cogs then start the bot
async def start():
    async with zeldaBot:
        for extension in cogsList:
            await zeldaBot.load_extension(extension)
        await zeldaBot.start(token)


# setup when the bot starts
@zeldaBot.event
async def on_ready():
    await zeldaBot.change_presence(activity=discord.Streaming(name='type "!help"', url='https://www.twitch.tv'
                                                                                       '/MattyReign'))
    print(f'{zeldaBot.user.name} has connected to Discord!')


# function to load adn watch for non-standard commands
@zeldaBot.event
async def on_message(message):
    await onMessageHelper.userMessage(message, zeldaBot)
    await zeldaBot.process_commands(message)


# run the bot
asyncio.run(start())
