# onMessage.py
import discord
from discord.ext import commands
import random

async def userMessage(message, bot):
    # wont reply to self
    if message.author == bot.user:
        return

    # cloud to butt translator
    if 'cloud' in message.content.lower():
        await message.channel.send('Did you mean butt(s)?')

    # !ymh command to make a YMH quote
    if message.content.lower() == '!ymh':
        await ymhFunction(message, bot)

    # !joke command to make a joke
    if message.content.lower() == '!joke':
        await jokesFunction(message, bot)

    # will allow bot.commands if i add them later
    await bot.process_commands(message)

async def ymhFunction(message, bot):
    ymhQuotes = ['"What\'s up there chomo?"', '"You just lost your life."', '"You\'re fired ok, you didn\'t follow proto."',
                 '"Imagine a pig with tits."', '"Come on Mark, don\'t be stingy."', '"Just let me eat ya."', '"Who is Randy?"',
                 '"Your mom in the fuckin stands!"', '"Try it out."', '"You\'ll cum in 4 strokes."', '"Bert is fat."',
                 '"Okay, but would you marry your mom?"', '"Just Glassin\'"', '"10-12 Benadryl"', '"Good morning Julia."']
    YHMresponce = random.choice(ymhQuotes)
    await message.channel.send(YHMresponce)


async def jokesFunction(message, bot):
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
    JOKEresponce = random.choice(jokes)
    await message.channel.send(JOKEresponce)


async def helpFunction(message, bot):
    await message.channel.send(
        '''```
Standard commands:
    !help: Will bring you here.
    !joke: Will tell you a funy joke!
    !ymh: Will give you a funny joke from "Your Mom's House Podcast"
Music Bot commands:
    !play: Play a song in the music channel, must be followed by a youtube url.
    !pause: Pause music in the music channel.
    !resume: Resume playing music after pausing in the music channel.
    !stop: Stop the current song playing in the music channel.
    !leave: Make the bot leave the music channel.
```'''
    )
