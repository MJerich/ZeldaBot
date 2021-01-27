# bot.py
import os
import discord
import random
import youtube_dl
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
myGuild = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='*', case_insensitive=True)

# connect the bot to discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# function for find user messages
@bot.event
async def on_message(message):

    # wont reply to self
    if message.author == bot.user:
        return

    # cloud to butt translator
    if 'cloud' in message.content.lower():
        await message.channel.send('Did you mean butt(s)?')


    # !ymh command to make a YMH quote
    ymhQuotes = ['"What\'s up there chomo?"', '"You just lost your life."', '"You\'re fired ok, you didn\'t follow proto."',
                '"Imagine a pig with tits."', '"Come on Mark, don\'t be stingy."', '"Just let me eat ya."', '"Who is Randy?"',
                '"Your mom in the fuckin stands!"', '"Try it out."', '"You\'ll cum in 4 strokes."', '"Bert is fat."',
                '"Okay, but would you marry your mom?"', '"Just Glassin\'"', '"10-12 Benadryl"', '"Good morning Julia."']

    if message.content.lower() == '!ymh':
        YHMresponce = random.choice(ymhQuotes)
        await message.channel.send(YHMresponce)

    # !joke command to make a joke
    jokes = ['Why did the scarecrow win an award? Because he was outstanding in his field.',
             'What\'s brown and sticky? A stick.', 'What do you call a fake noodle? An Impasta.', 'I would avoid the sushi if I was you. It\'s a little fishy.',
             'Want to hear a joke about paper? Nevermind it\'s tearable.', 'I used to work in a shoe recycling shop. It was sole destroying.',
             'What do you call a belt with a watch on it? A waist of time.', 'How do you organize an outer space party? You planet.',
             'Do you know where you can get chicken broth in bulk? The stock market.', 'Why did the octopus beat the shark in a fight? Because it was well armed.',
             'How much does a hipster weigh? An instagram.', 'What did daddy spider say to baby spider? You spend too much time on the web.',
             'Atheism is a non-prophet organisation.', 'There\'s a new type of broom out, it\'s sweeping the nation.', 'What cheese can never be yours? Nacho cheese.',
             'What did the Buffalo say to his little boy when he dropped him off at school? Bison.', 'Have you ever heard of a music group called Cellophane? They mostly wrap.',
             'The shovel was a ground breaking invention.', 'A scarecrow says, "This job isn\'t for everyone, but hay, it\'s in my jeans."',
             'A Buddhist walks up to a hot dog stand and says, "Make me one with everything."', 'Did you hear about the guy who lost the left side of his body? He\'s alright now.']
    if message.content.lower() == '!joke':
        JOKEresponce = random.choice(jokes)
        await message.channel.send(JOKEresponce)

    # !help or !commands to show all commands
    if message.content.lower() == '!help' or message.content.lower() == '!commands':
        await message.channel.send(
'''```
Standard commands:
    !help: Will bring you here.
    !joke: Will tell you a funy joke!
    !ymh: Will give you a funny joke from "Your Mom's House Podcast"
Music Bot commands:
    *play: Play a song in the music channel, must be followed by a youtube url.
    *pause: Pause music in the music channel.
    *resume: Resume playing music after pausing in the music channel.
    *stop: Stop the current song playing in the music channel.
    *leave: Make the bot leave the music channel.
```'''
        )


    # will allow bot.commands if i add them later
    await bot.process_commands(message)

# *MUSIC BOT STARTS HERE*

# function to check if the bot is already connected to the voice channel
def is_connected(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()

# play command, must be followed with a youtube url
@bot.command(hidden=True)
async def play(ctx, url: str):
    songPlaying = os.path.isfile('song.mp3')
    try:
        if songPlaying:
            os.remove('song.mp3')
    except PermissionError:
        await ctx.send('wait for the current song to finish please.')
        return

    voiceChannel = discord.utils.get(
        ctx.guild.voice_channels, name='Reign\'s music studio')

    if not is_connected(ctx):
        await voiceChannel.connect()

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'))


# make bot leabve the voice channel
@bot.command(hidden=True)
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send('The bot is not in a voice channel.')

# pause the music
@bot.command(hidden=True)
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('Nothing is playing.')

#resume the music after pausing
@bot.command(hidden=True)
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('Audio is already playing.')

# stop the music
@bot.command(hidden=True)
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.stop()
    else:
        await ctx.send('Nothing is playing.')

# *MUSIC BOT ENDS HERE*

#client.run(token)
bot.run(token)
