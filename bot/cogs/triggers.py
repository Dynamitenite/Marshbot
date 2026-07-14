import discord
from discord.ext import commands
import random
class triggers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def admin(self,ctx):
        em = discord.Embed(color= 0x326BF7)
        lol=["https://media1.tenor.com/images/f1973f495061be904f76c8c4635463fc/tenor.gif?itemid=4318961", 
        "https://media1.tenor.com/images/e65fffed2a52c699a94341219bc02e44/tenor.gif?itemid=22259000"
        ]
        em.set_image(url=random.choice(lol))
        await ctx.send(embed=em)
    
    @commands.command()
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def nsfw(self,ctx):
        em = discord.Embed(title="Caught you lacking in 4k", color= 0x326BF7)
        lol=['https://media1.tenor.com/images/54ab1ba720a71fd3f34f0064e38cb853/tenor.gif?itemid=20146264', 
        'https://media1.tenor.com/images/6493bee2be7ae168a5ef7a68cf751868/tenor.gif?itemid=17298755',
        'https://media1.tenor.com/images/cc67ae29083a961796bb53d5f4c53a10/tenor.gif?itemid=19585782'
        ]
        em.set_image(url=random.choice(lol))
        await ctx.send(embed=em)

            

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user: return
        if message.author.bot: return

        #if self.bot.mention in message.content():

            #with open('prefixes.json', 'r') as f:
                #prefixes = json.load(f)

            #pre = prefixes[str(message.guild.id)]

            #em = discord.Embed(description=f"<:helpinfo:868531903823769600> The prefix for this server is `{pre}`", color= 0x326BF7)
            #await message.channel.send(embed=em)
            #await self.bot.process_commands(message)


           
        #if message.content=='meme':
            #await message.channel.send('''Check out this new meme!!!
            
#https://www.instagram.com/p/CQkclT-LzIo''')

        #if '<@!283120067443687424' in message.content:
            #await message.channel.send("<a:ping:826930142256562247>")

        
        #if message.content.lower() == 'hello there':
            #await message.channel.send(f'General Kenobi <a:GeneralKenobi:820658491017527337>')

        #if message.content.lower().startswith('cope'):
            #await message.channel.send(f'Cope harder next time nab <a:PepeLaughers:846417893704990771>')

        #if 'ann cute' in message.content.lower():
            #await message.channel.send(f'{message.author.mention} Devon is on his way to assrape you <a:aPES_NarutoRun:841281953805893682>')


        #if message.content.upper() == 'F':
            #await message.channel.send(f'{message.author.name} has paid their respects')

        #if 'your mom gay' in message.content.lower() or 'your mom is gay' in message.content.lower():
            #await message.channel.send('8 year old fortnite kid insult moment <:pepecringe:818505853073621002>')
        
        #if message.content.lower() in ['vsco', 'vsco girl']:
            #await message.channel.send('sksksk anna oop-')

        #if message.content.lower() == "k":
            #await message.channel.send("Woah there buddy, I'll need to stop you right there; too cold")

        #if  message.content.lower() == 'pog' or message.content.lower() == 'pogu':
            #await message.channel.send("Are ya winning son?')
        
        #if 'gae' in message.content.lower():
            #await message.channel.send('No you <a:AnimeUnoReverse:818510160888463431>')

       # if 'fml' in message.content.lower():
            #await message.channel.send('<:HideThePain:818507993376489532>')

        #if 'yamete kudasai' in message.content.lower():
            #await message.channel.send('<:pepestop:818504516013785108> Stop right there buddy, consent is important')
        
        #if 'snowflake' in message.content.lower():
            #await message.channel.send('Time to run <a:run:820656250027114587>')
            #await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(triggers(bot))
