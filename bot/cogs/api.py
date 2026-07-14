import discord
from discord.ext import commands
import aiohttp
import random
from aiohttp import ClientSession

class api(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #DOG FACTS
    @commands.command()
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()
        embed = discord.Embed(title="Doggo! <a:DoggoPet:839210173386326037>", color=discord.Color.random()) # Create embed
        embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed) # Send the embed

    #CAT FACTS
    @commands.command()
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            catjson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/cat')
            factjson = await request2.json()
        embed = discord.Embed(title="Meow meow! <a:Kitty:847338388452671569>", color=discord.Color.random()) # Create embed
        embed.set_image(url=catjson['link']) # Set the embed image to the value of the 'link' key
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed) # Send the embed

    #JOKE
    @commands.command()
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def joke(self, ctx):
        url="https://dad-jokes.p.rapidapi.com/random/joke"

        headers={
            'x-rapidapi-host' : "dad-jokes.p.rapidapi.com",
            'x-rapidapi-key' : self.bot.joke_api_key
        }

        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r=await response.json()
                await ctx.send(f"**{r['setup']}**\n\n||{r['punchline']}||")

    @commands.command(name='mom')
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def mom_fat(self, ctx, arg=None):

        if arg==None:
            responses=[
                "Yo mama's so poor, the ducks throw bread at her.",
                "Yo mama's so old, when she goes to the museum, she finds her exes.",
                "Yo mama's so poor, she chases the garbage truck with a grocery list.",
                "Yo mama's cooking so nasty, she flys got together and fixed the hole in the window screen.",
                "Yo mama's so depressing, blues singers come to visit her when they've got writer's block.",
                "Yo mama's so short, you can see her feet on her driver's license.",
                "Yo mama's so old, her social security number is one.",
                "Yo mama's so poor, she can't even afford to pay attention.",
                "Yo momma is so poor she went running after the garbage truck with a grocery list.",
                "Yo mama's so old, she walked out of a museum and the alarm went off.",
                "Yo mama's so old, her classmate was moses."
                "Yo mama's so big, her belt size is **equator**.",
                "Yo mama's so classless, she's a Marxist utopia.",
                "Yo mama's so short, she went to see Santa and he told her to get back to work.",
                "Yo mama's so scary, the government moved Halloween to her birthday.",
                "Yo mama's so nasty, they used to call them jumpolines 'til yo mama bounced on one.",
                "Yo mama's teeth so yellow, I can't believe it's not butter.",
                "Yo mama's so poor, Nigerian princes wire her money.",
                "Yo mama's so lazy, she stuck her nose out the window and let the wind blow it."
                ]
            responses=random.choice(responses)
            await ctx.send(responses)

        elif arg.lower()=="fat":
            responses=[
                "Yo mama's so fat, when she fell I didn't laugh, but the sidewalk cracked up",
                "Yo mama's so fat, when she skips a meal, the stock market drops.",
                "Yo mama's so fat, her vibrator suffocated.",
                "Yo mama's so fat, it took me two buses and a train to get to her good side.",
                "Yo mama's so fat, when she goes camping, the bears hide their food.",
                "Yo mama's so fat, if she buys a fur coat, a whole species will become extinct.",
                "Yo mama's so fat, she stepped on a scale and it said: 'To be continued.'",
                "Yo mama's so fat, her bellybutton gets home 15 minutes before she does.",
                "Yo mama's so fat, I swerved to miss her in my car and ran out of gas.",
                "Yo mama's so fat, I took a picture of her last Christmas, and it's still printing.",
                "Yo mama's so fat, when she wears high heels, she strikes oil.",
                "Yo mama's so fat, she was overthrown by a small militia group, and now she's known as the Republic of Yo Mama.",
                "Yo mama's so fat, when she sits around the house, she SITS AROUND the house.",
                "Yo mama's so fat, her car has stretch marks.",
                "Yo mama's so fat, she can't even jump to a conclusion.",
                "Yo mama's so fat, her blood type is Ragu.",
                "Yo mama's so fat, if she was a Star Wars character, her name would be Admiral Snackbar.",
                "Yo mama's so fat, she brought a spoon to the Super Bowl."
                ]
            responses=random.choice(responses)
            await ctx.send(responses)

        elif arg.lower()=="dumb":
            responses=[
                "Yo mama's so dumb, she stared at a cup of orange juice for 12 hours because it said **concentrate**.",
                "Yo mama's so dumb when they said it was chilly outside, she grabbed a bowl.",
                "Yo mama's so dumb, she put lipstick on her forehead to make up her mind.",
                "Yo mama's so dumb, when they said, **Order in the court,** she asked for fries and a shake.",
                "Yo mama's so dumb, she thought a quarterback was a refund.",
                "Yo mama's so dumb, she thought a quarterback was a refund.",
                "Yo mama's so dumb, she went to the eye doctor to get an iPhone.",
                "Yo mama's so dumb, she got hit by a parked car.",
                "Yo mama's so dumb, when I told her that she lost her mind, she went looking for it.",
                "Yo mama's so dumb when thieves broke into her house and stole the TV, she chased after them shouting **Wait, you forgot the remote!**",
                "Yo mama's so dumb, she went to the dentist to get a Bluetooth.",
                "Yo mama's so dumb, she took a ruler to bed to see how long she slept.",
                "Yo mama's so dumb, she got locked in the grocery store and starved to death.",
                "Yo mama's so dumb, when I said, **Drinks on the house**, she got a ladder.",
                "Yo mama's so dumb, it takes her two hours to watch 60 Minutes.",
                "Yo mama's so dumb, she put airbags on her computer in case it crashed."
                ] 
            responses=random.choice(responses)
            await ctx.send(responses)

        elif arg.lower()=="ugly":
            responses=[
                "Yo mama's so ugly, she threw a boomerang and it refused to come back.",
                "Yo mama's so ugly that Dominic Toretto said, **family can't fix that**.",
                "Yo mama's so ugly, she made a blind kid cry.",
                "Yo mama's so ugly, her birth certificate is an apology letter from the condom factory.",
                "Yo mama's so ugly, her portraits hang themselves.",
                "Your momma so ugly she has to sneak up on the mirror.",
                "Yo mama's teeth are so yellow when she smiles at traffic, it slows down.",
                "Yo mama's armpits are so hairy, it looks like she's got Buckwheat in a headlock.",
                "Yo mama's so ugly, when she was little, she had to trick-or-treat by phone.",
                "Yo mama is so ugly when the devil saw her, he started praying.",
                "Yo mama's so ugly, her birth certificate is an apology letter.",
                "Yo mama's so ugly, she looked out the window and was arrested for mooning."
            ]
            responses=random.choice(responses)
            await ctx.send(responses)

        else:
            em = discord.Embed(description=f"<:RedTick:868863832934727780> Command not found.", color= 0xFF0000)
            await ctx.send(embed=em)

    @commands.command(name='quote', aliases=['q'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def quote(self, ctx):
        responses=[
                "Friendship is like peeing on yourself: everyone can see it but only you get the warm feeling it brings.",
                "When all else fails, there's always delusion.",
                "A good friend will help you move. But a best friend will help you move a dead body."
            ]
        responses=random.choice(responses)
        await ctx.send(responses)
            



def setup(bot):
    bot.add_cog(api(bot))