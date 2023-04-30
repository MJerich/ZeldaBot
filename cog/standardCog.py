# onMessage.py
from discord.ext import commands
import random


class standardCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # custom formatted !help command
    @commands.command(name='help')
    async def helpFunction(self, ctx):
        await ctx.send(
            '''```
Standard commands:
    !help: Will bring you here.
    !joke: Will tell you a funny joke!
    !ymh: Will give you a funny joke from "Your Mom's House Podcast"
    !flip: Flip a coin and get a "Heads" or "Tails" response.
    !ai {your message here}: Will send your message to ChatGPT-3 and then give you it's response.
RemindMe commands:
    !RemindMe: will make a reminder you and anyone/role you tag.
            format: !RemindMe (number) (seconds, minutes,
                    hours, or days) (your message)
            Example: !RemindMe 2 days DnD tonight at 8pm dont forget! @DnD role
            will respond: "@yourname: DnD tonight at 8pm dont forget! @DnD role"
                        in 2 days
```'''
        )

    # YMH quote
    @commands.command(name='ymh')
    async def ymhFunction(self, ctx):
        ymhQuotes = ['"What\'s up there chomo?"', '"You just lost your life."',
                     '"You\'re fired ok, you didn\'t follow proto."',
                     '"Imagine a pig with tits."', '"Come on Mark, don\'t be stingy."', '"Just let me eat ya."',
                     '"Who is Randy?"',
                     '"Your mom in the fuckin stands!"', '"Try it out."', '"You\'ll cum in 4 strokes."',
                     '"Bert is fat."',
                     '"I asked him, would you ever date your mom?"', '"Just Glassin\'"',
                     '"Good morning Julia."', '"Let\'s go full trottle."', '"cool stuff, neat stuff, slick stuff"',
                     '"I\'m a hot white trash cum dump, let\'s fuck."']
        YHMResponse = random.choice(ymhQuotes)
        await ctx.send(YHMResponse)

    # joke
    @commands.command(name='joke')
    async def jokesFunction(self, ctx):
        jokes = ['Why did the scarecrow win an award? Because he was outstanding in his field.',
                 'What\'s brown and sticky? A stick.', 'What do you call a fake noodle? An Impasta.',
                 'I would avoid the sushi if I was you. It\'s a little fishy.',
                 'Want to hear a joke about paper? Nevermind it\'s tearable.',
                 'I used to work in a shoe recycling shop. It was sole destroying.',
                 'What do you call a belt with a watch on it? A waist of time.',
                 'How do you organize an outer space party? You planet.',
                 'Do you know where you can get chicken broth in bulk? The stock market.',
                 'Why did the octopus beat the shark in a fight? Because it was well armed.',
                 'How much does a hipster weigh? An instagram.',
                 'What did daddy spider say to baby spider? You spend too much time on the web.',
                 'Atheism is a non-prophet organisation.',
                 'There\'s a new type of broom out, it\'s sweeping the nation.',
                 'What cheese can never be yours? Nacho cheese.',
                 'What did the Buffalo say to his little boy when he dropped him off at school? Bison.',
                 'Have you ever heard of a music group called Cellophane? They mostly wrap.',
                 'The shovel was a ground breaking invention.',
                 'A scarecrow says, "This job isn\'t for everyone, but hay, it\'s in my jeans."',
                 'A Buddhist walks up to a hot dog stand and says, "Make me one with everything."',
                 'Did you hear about the guy who lost the left side of his body? He\'s alright now.']
        JOKEResponse = random.choice(jokes)
        await ctx.send(JOKEResponse)

    # coin flip
    @commands.command(name='flip')
    async def coinFlip(self, ctx):
        headOrTail = ['Heads', 'Tails']
        flipResponse = random.choice(headOrTail)
        await ctx.send(flipResponse)


async def setup(bot):
    await bot.add_cog(standardCommands(bot))
