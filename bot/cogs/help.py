import discord
import json
from discord.ext import commands

class helpcmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        with open('prefixes.json', 'w') as f: 
            json.dump(prefixes, f, indent=4)
    

        em = discord.Embed(title='Commands', description=f'Use {pre}help <command> for extended information on a command', color= 0x326BF7)

        em.add_field(name='General - 3', value="`ping` `invite` `admin`", inline=False)
        em.add_field(name='Fun - 3', value="`8ball` `dog` `cat` `mom` `quote`", inline=False)
        em.add_field(name='Moderation - 6', value="`role` `banish` `unbanish` `kick` `ban` `unban`", inline=False)
        em.add_field(name='Admin - 3', value="`prefix` `dm` `echo`", inline=False)
        em.add_field(name='Nsfw - 1', value="`nsfw`", inline=False)
        await ctx.send(embed=em)

    @help.command(aliases=['q'])
    async def quote(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 
    
        with open('prefixes.json', 'w') as f: 
            json.dump(prefixes, f, indent=4)

        em = discord.Embed(title = '**Role**', description = "Sends a quote", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}quote`")
        em.add_field(name = "**Aliases**", value = "`r`")
        await ctx.send(embed=em)

    @help.command()
    async def mom(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 
    
        with open('prefixes.json', 'w') as f: 
            json.dump(prefixes, f, indent=4)

        em = discord.Embed(title = '**Mom**', description = "Tells a yo mama joke", color= 0x326BF7)
        em.add_field(name=f'{pre}mom fat', value="Yo Mama **fat** joke", inline=False)
        em.add_field(name=f'{pre}mom dumb', value="Yo Mama **dumb** joke", inline=False)
        em.add_field(name=f'{pre}mom ugly', value="Yo Mama **ugly** joke", inline=False)
        await ctx.send(embed=em)

    @help.command(aliases=['r'])
    async def role(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 
    
        with open('prefixes.json', 'w') as f: 
            json.dump(prefixes, f, indent=4)

        em = discord.Embed(title = '**Role**', description = "Adds/removes a role from the specified member", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}role <member> <role>` ")
        em.add_field(name = "**Aliases**", value = "`r`")
        await ctx.send(embed=em)

    @help.command(aliases=['e','an','announce'])
    async def echo(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 
    
        with open('prefixes.json', 'w') as f: 
            json.dump(prefixes, f, indent=4)

        em = discord.Embed(title = f'**Echo**', description = "Makes the bot say something in the specified channel", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}echo [destination] <msg>` ")
        em.add_field(name = "**Aliases**", value = "``e` `an` `announce`")
        await ctx.send(embed=em)

    @help.command(aliases=['av'])
    async def avatar(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 
    
        with open('prefixes.json', 'w') as f: 
            json.dump(prefixes, f, indent=4)

        em = discord.Embed(title = f'**Avatar**', description = "Displays the specified user's avatar", color= 0x326BF7)
        em.add_field(name= '**Syntax**', value=f"`{pre}avatar <member>` ")
        em.add_field(name = "**Aliases**", value = "`av`")
        await ctx.send(embed=em)

    @help.command()
    async def admin(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 
    
        with open('prefixes.json', 'w') as f: 
            json.dump(prefixes, f, indent=4)

        em = discord.Embed(title = f'**Admin**', description = "Gives you complete control of the bot including all admin permissions", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}admin`")
        await ctx.send(embed=em)

    @help.command()
    async def ping(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 
    
        with open('prefixes.json', 'w') as f: 
            json.dump(prefixes, f, indent=4)


        em = discord.Embed(title = "**Ping**" , description = "Checks the bot's latency", color= 0x326BF7)
        em.add_field(name = "**Syntax**", value = f"`{pre}ping`")
        await ctx.send(embed=em)

    @help.command()
    async def prefix(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        em = discord.Embed(title = '**Prefix**', description = "Changes the bot's prefix")
        em.add_field(name= '**Syntax**', value=f"`{pre}prefix <prefix>`")
        await ctx.send(embed=em)

    @help.command(name='8ball')
    async def _8ball(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 
        
        em = discord.Embed(title = "**8ball**" , description = "Runs 8ball commands", color= 0x326BF7)
        em.add_field(name = "**Syntax**", value = f"`{pre}8ball <question>`")
        await ctx.send(embed=em)

    @help.command()
    async def invite(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        em = discord.Embed(title = '**Invite**', description = "Gives the invite link for the bot", color= 0x326BF7)
        em.add_field(name= '**Syntax**', value=f"`{pre}invite`")
        await ctx.send(embed=em)

    @help.command()
    async def dm(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 
    
        em = discord.Embed(title = '**DM**', description = "Sends a DM to a user")
        em.add_field(name='**Syntax**', value=f"`{pre}dm <member> <message>`")
        await ctx.send(embed=em)

    @help.command()
    async def kick(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 
    
        em = discord.Embed(title = '**Kick**', description = "Kicks the specified user from the guild", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}kick <member> <reason>`")
        await ctx.send(embed=em)

    
    @help.command()
    async def ban(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        em = discord.Embed(title = '**Ban**', description = "Bans the specified user from the guild", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}ban <member> <reason>`")
        await ctx.send(embed=em)

    @help.command(aliases=['s'])
    async def snipe(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)]

        em = discord.Embed(title = "**Snipe**" , description = "Shows the last deleted message from a channel", color= 0x326BF7)
        em.add_field(name = "**Syntax**", value = f"`{pre}snipe`")
        em.add_field(name = "**Aliases**", value = "`s`")
        await ctx.send(embed=em)

    
    @help.command(aliases=['b', 'mute'])
    async def banish(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        em = discord.Embed(title = '**Banish**', description = "Mutes a member indefinitely", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}banish <member>`")
        em.add_field(name = "**Aliases**", value = "`b` `mute`")
        await ctx.send(embed=em)

    @help.command(aliases=['ub'])
    async def unbanish(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        em = discord.Embed(title = '**Unbanish**', description = "Unmutes a member", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}unbanish <member>`")
        em.add_field(name = "**Aliases**", value = "`ub`")
        await ctx.send(embed=em)
    
    @help.command(name="purge", aliases=['clear', 'c'])
    async def clear(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        em = discord.Embed(title = '**Purge**', description = "Deletes the specified number of the most recent messages from a channel", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}purge [num]`")
        em.add_field(name = "**Aliases**", value = "`c` `clear`")
        await ctx.send(embed=em)

    
    @help.command()
    async def dog(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        em = discord.Embed(title = '**Dog**', description = "Sends random dog facts", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}dog`")
        await ctx.send(embed=em)

    @help.command()
    async def cat(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        em = discord.Embed(title = '**Cat**', description = "Sends random cat facts", color= 0x326BF7)
        em.add_field(name= '**Syntax**', value=f"`{pre}cat`")
        await ctx.send(embed=em)
        
    @help.command()
    async def nsfw(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        pre = prefixes[str(ctx.guild.id)] 

        em = discord.Embed(title = '`Nsfw`', description = "Runs nsfw commands", color= 0x326BF7)
        em.add_field(name='**Syntax**', value=f"`{pre}nsfw`")
        await ctx.send(embed=em)

    @help.error
    async def help_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Command **{ctx}** not found")
        




def setup(bot):
    bot.add_cog(helpcmd(bot))