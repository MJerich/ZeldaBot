# musicBotHelper.py
import youtube_dl
import os
import discord

# function to check if the bot is already connected to the voice channel
def is_connected(bot, ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients)
    return voice_client and voice_client.is_connected()

# play command, must be followed with a youtube url


async def play(ctx, url: str, bot):
    songPlaying = os.path.isfile('song.mp3')
    try:
        if songPlaying:
            os.remove('song.mp3')
    except PermissionError:
        await ctx.send('wait for the current song to finish please.')
        return

    voiceChannel = discord.utils.get(
        ctx.guild.voice_channels, name='Reign\'s music studio')

    if not is_connected(ctx, bot):
        await voiceChannel.connect()

    voice = discord.utils.get(bot.voice_clients)

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


async def leave(ctx, bot):
    voice = discord.utils.get(bot.voice_clients)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send('The bot is not in a voice channel.')

# pause the music


async def pause(ctx, bot):
    voice = discord.utils.get(bot.voice_clients)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('Nothing is playing.')

#resume the music after pausing


async def resume(ctx, bot):
    voice = discord.utils.get(bot.voice_clients)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('Audio is already playing.')

# stop the music


async def stop(ctx, bot):
    voice = discord.utils.get(bot.voice_clients)
    if voice.is_playing():
        voice.stop()
    else:
        await ctx.send('Nothing is playing.')
