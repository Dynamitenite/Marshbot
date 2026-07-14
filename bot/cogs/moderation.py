import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['b', 'mute'])
    @commands.has_permissions(manage_messages=True)
    async def banish(self, ctx, member: discord.Member, reason=None):
        banished=discord.utils.get(ctx.guild.roles, name="Banished")

        if member == self.bot.user: 
            em = discord.Embed(description= f"<:RedTick:868863832934727780> You can't banish me, fool.", color= 0xFF0000)
            await ctx.channel.send(embed=em)
            return

        elif member ==ctx.author:
            em = discord.Embed(description= f"<:RedTick:868863832934727780> Why tf do you wanna banish yourself?", color= 0xFF0000)
            await ctx.channel.send(embed=em)
            return
            
        elif member.guild_permissions.manage_messages:
            embed = discord.Embed(description="<:RedTick:868863832934727780> That user is a mod/admin, I can't do that.", color= 0xFF0000)
            await ctx.send(embed=embed)
            return

        if not banished:
            banished = await ctx.guild.create_role(name="Banished")
            for channel in ctx.guild.channels:
                await channel.set_permissions(banished, speak=False, send_messages=False, add_reactions=False)
        if banished in member.roles:
            em = discord.Embed(description= f"<:RedTick:868863832934727780> {member} is already banished.", color= 0xFF0000)
            await ctx.channel.send(embed=em)
        else:
            await member.add_roles(banished)
            em = discord.Embed(title= 'Banished', description= f"<:green_tick:868863780585631784> {member} was banished.", color= 0x326BF7)
            await ctx.send(embed=em)
            

    @banish.error
    async def banish_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(description= "<:RedTick:868863832934727780> You are missing `KICK_MEMBERS` permission(s) to run this command.", color= 0xFF0000)
            await ctx.send(embed=em) 

    @commands.command(aliases=['ub', 'unmute'])
    @commands.has_permissions(manage_messages=True)
    async def unbanish(self, ctx, member: discord.Member):
        banished=discord.utils.get(ctx.guild.roles, name="Banished")
        if banished not in member.roles:
            em = discord.Embed(description= f"<:RedTick:868863832934727780> {member} is not banished.", color= 0xFF0000)
            await ctx.channel.send()
            await ctx.channel.send(f'{member} is not banished.')
        else:
            await member.remove_roles(banished)
            em = discord.Embed(title= 'Unbanished', description= f'<:green_tick:868863780585631784> {member} was unbanished.', color= 0x326BF7)
            await ctx.send(embed=em)
    
    @unbanish.error
    async def unbanish_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(description= "<:RedTick:868863832934727780> You are missing `KICK_MEMBERS` permission(s) to run this command.", color= 0xFF0000)
            await ctx.send(embed=em) 

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):

        if member.guild_permissions.manage_messages:
            embed = discord.Embed(description="<:RedTick:868863832934727780> That user is a mod/admin, I can't do that.", color= 0x326BF7)
            await ctx.send(embed=embed)

        #if member.top_role >= ctx.author.top_role:
            #embed = discord.Embed(description="Your role is not high enough in the role hierarcy.", color= 0x326BF7)
            #await ctx.send(embed=embed)
        else:
            await member.kick(reason=reason)
            #await ctx.message.delete()
            embed = discord.Embed(title= 'Kicked', description=f'<:green_tick:868863780585631784> {member} was kicked', color= 0x326BF7)
            await ctx.channel.send(embed=embed)
            await member.send(f"You have been kicked from **{ctx.guild.name}** for `{reason}`")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are missing `KICK_MEMBERS` permission(s) to run this command!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason="No reason given"):


        if member.guild_permissions.manage_messages:
            embed = discord.Embed(description="<:RedTick:868863832934727780> That user is a mod/admin, I can't do that.", color= 0xFF0000)
            await ctx.send(embed=embed)

        #if member.top_role >= ctx.author.top_role:
            #await ctx.send("That user is a mod/admin, I can't do that.")
        else:
            await member.ban(reason=reason)
            #await ctx.message.delete()
            em = discord.Embed(title= 'Banned', description= f'<:green_tick:868863780585631784> {member} was banned', color= 0x326BF7)
            await ctx.channel.send(embed=em)
            await member.send(f"You have been banned from **{ctx.guild.name}** for `{reason}`")
    
    
    @ban.error
    async def ban_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(description= "You are missing `BAN_MEMBERS` permission(s) to run this command.", color= 0xFF0000)
            await ctx.channel.send(embed=em)
            await ctx.send("<:RedTick:868863832934727780> You are missing `BAN_MEMBERS` permission(s) to run this command.") 



def setup(bot):
    bot.add_cog(moderation(bot))
