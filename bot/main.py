#Import Discord Package
import discord
import asyncio
import os
import json
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

def get_prefix(client, message): 
    with open('prefixes.json', 'r') as f: 
        prefixes = json.load(f) 

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix= get_prefix)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you sleep 0_0'))
    print(f'{client.user} is ready.')
    print(f"Playing in {len(client.guilds)} servers")

async def ch_pr():
    await client.wait_until_ready()

    statuses = ["Studying 25 hours a day", "Friendzoned", "in 69420 servers", "Having an existential crisis", "with myself"]


    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=status))

        await asyncio.sleep(10)

client.loop.create_task(ch_pr())

@client.event
async def on_guild_join(guild): 
    with open('prefixes.json', 'r') as f: 
        prefixes = json.load(f) 

    prefixes[str(guild.id)] = '+'

    with open('prefixes.json', 'w') as f: 
        json.dump(prefixes, f, indent=4) 

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) 

    with open('prefixes.json', 'w') as f: 
        json.dump(prefixes, f, indent=4) 

@client.command()
@commands.has_permissions(administrator=True) 
async def prefix(ctx, prefix): 

    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f: 
        json.dump(prefixes, f, indent=4)

    em = discord.Embed(description=f"<:green_tick:868863780585631784> Prefix changed to: {prefix}", color= 0x326BF7)
    await ctx.send(embed=em)

@prefix.error
async def prefix_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing the `ADMINISTRATOR` permission(s)'.")

@client.remove_command('help')


@client.command(aliases=['p'])
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def ping(ctx):
    em = discord.Embed(description=f"Pong! {round(client.latency*1000)}ms", color= 0x326BF7)
    await ctx.send(embed=em)

@client.command(aliases=['i'])
async def invite(ctx):
    await ctx.author.send('https://discord.com/oauth2/authorize?client_id=815950259921354772&scope=bot&permissions=2147483647')
    await ctx.send(f"{ctx.author.mention} I DM'ed you the invite link", delete_after=3)

@client.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.errors.MemberNotFound):
        em = discord.Embed(description=f"That user is not in the server.", color= 0xFF0000) 
        await ctx.send(embed=em)  

    elif isinstance(error, commands.DisabledCommand):
        em = discord.Embed(description=f"{ctx.command} has been disabled.", color= 0xFF0000) 
        await ctx.send(embed=em)  

    elif isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"You're on a cooldown.",description=f"Try again in {round(error.retry_after, 2)}s.", color= 0xFFFF00)
        await ctx.message.delete(delay=5)
        await ctx.send(embed=em, delete_after=5)

    elif isinstance(error, commands.CommandNotFound):
        em = discord.Embed(description=f"<:RedTick:868863832934727780> Command not found.", color= 0xFF0000)
        await ctx.send(embed=em)

    elif isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(description=f"<:RedTick:868863832934727780> You forgot to input an argument for this command.", color= 0xFF0000)
        await ctx.send(embed=em)

    #else:
        #em = discord.Embed(description=f"<:RedTick:868863832934727780> Oh no! Something went wrong while running the command!", color= 0xFF0000)
        #await ctx.send(embed=em)
       

extensions = ['cogs.commands', 'cogs.help', 'cogs.snipe', 'cogs.triggers', 'cogs.moderation', 'cogs.api']

if __name__== '__main__':
    for ext in extensions:
        client.load_extension(ext)
        
#RUN THE CLIENT ON THE SERVER


client.run(os.getenv('TOKEN'))


 



