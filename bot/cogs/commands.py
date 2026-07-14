import discord
import random
from discord.ext import commands

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='8ball')
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def _8ball(self, ctx, *, message=None ): 
        if message == None:
            em=discord.Embed(description="You need to ask a question, dipshit!", color=0x326BF7)
            await ctx.channel.send(embed=em)
        else:
            responses = [
            discord.Embed(title='It is certain.', color=0x326BF7),
            discord.Embed(title='Go away or before I eat your cat.', color= 0x326BF7),
            discord.Embed(title='Without a doubt.', color= 0x326BF7),
            discord.Embed(title='Yes definitely.', color= 0x326BF7),
            discord.Embed(title='You may rely on it.', color=0x326BF7),
            discord.Embed(title='Most likely.', color=0x326BF7),
            discord.Embed(title='Outlook good.', color=0x326BF7),
            discord.Embed(title='Yes.', color=0x326BF7),
            discord.Embed(title='Signs point to yes.', color=0x326BF7),
            discord.Embed(title='Reply hazy, try again.', color=0x326BF7),
            discord.Embed(title='Ask again now.', color=0x326BF7),
            discord.Embed(title='Better not tell you now.', color=0x326BF7),
            discord.Embed(title='Cannot predict now.', color=0x326BF7),
            discord.Embed(title='Concentrate and ask again.', color=0x326BF7),
            discord.Embed(title="Don't count on it.", color=0x326BF7),
            discord.Embed(title='No way, Jose.', color=0x326BF7),
            discord.Embed(title='My sources say no.', color=0x326BF7),
            discord.Embed(title='Outlook not very good.', color=0x326BF7),
            discord.Embed(title='Very doubtful.', color=0x326BF7)
                ]
            responses = random.choice(responses)
            await ctx.send(embed=responses)

    @commands.command(aliases=['e','an','announce'])
    @commands.has_permissions(administrator=True)
    async def echo(self, ctx, channel: discord.TextChannel=None, *, message): 


        #if channel==None:
            #await ctx.channel.send(embed=em)
            #await ctx.message.add_reaction("<:green_tick:868863780585631784>")
            
        await channel.send(message)
        await ctx.message.add_reaction("<:green_tick:868863780585631784>")

    @echo.error
    async def echo_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are missing `ADMINISTRATOR` permission(s) to run this command!")

    @commands.command()
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def dm(self, ctx, user: discord.User, *, message=None):
        if message == None:
            await ctx.send('You need to put a message', delete_after=5)
    
        else:
            await user.send(message)
            #await ctx.message.delete()
            await ctx.channel.send('"' + message + '"' + ' sent to ' + str(user))
            print(str(ctx.author) +':' + '"' + message + '"' + ' sent to ' + str(user))
            

    @commands.command()
    async def on_message(self, message):
        if message.content.startswith('+dm ' + '<@!815950259921354772>'):
                await message.channel.send("I can't DM myself")

    @dm.error
    async def dm_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are missing `MANAGE_MESSAGES` permission(s) to run this command!")  

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member: discord.Member=None):

        if member is None:
            embed = discord.Embed(title="Avatar", color = discord.Color.random())
            embed.set_image(url=ctx.author.avatar_url)
            embed.set_author(name = f"{ctx.author}", icon_url = ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
            return

        else:
            embed = discord.Embed(title="Avatar", color=discord.Color.random())
            embed.set_image(url=member.avatar_url)
            embed.set_author(name = f"{member}", icon_url = member.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def poll(self, ctx, *, message):
        em=discord.Embed(title="<:CH_BlobPoll:868863936362065940> **POLL**", description=f"{message}", color=0x326BF7)
        em.set_footer(text=f"Requested by {ctx.author}")
        msg=await ctx.channel.send(embed=em)
        await msg.add_reaction('<:green_tick:868863780585631784>')
        await msg.add_reaction('<:RedTick:868863832934727780>')

    @commands.command(aliases=['r'])
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, role: discord.guild.Role): 

        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f"{role.name} removed from {member}")

        else:
            await member.add_roles(role)
            await ctx.send(f"{role.name} added to {member}")

    @role.error
    async def role_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are missing `MANAGE_ROLES` permission(s) to run this command.")

        if isinstance(error, commands.RoleNotFound):
            await ctx.send("That role doesn't exist in the server.")

    @commands.command(name="purge", aliases=['c', 'clear'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send('Purged by {}'.format(ctx.author.name), delete_after=1)
        await ctx.message.delete()
      
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are missing `MANAGE_MESSAGES` permission(s) to run this command.")     
            
def setup(bot):
    bot.add_cog(commands(bot))