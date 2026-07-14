import discord
from discord.ext import commands

class snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.sniped_messages={}

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        if message.attachments:
            nab=message.attachments[0]
            self.bot.sniped_messages[message.channel.id] = (
            nab.proxy_url, message.content, message.author, message.channel.name, message.created_at)
        else:
            self.bot.sniped_messages[message.channel.id] = (
            message.content, message.author, message.channel.name, message.created_at)
            
    @commands.command(aliases=['s'])
    @commands.has_permissions(manage_messages=True)
    async def snipe(self, ctx,):

        try:
            nab_proxy_url, contents, author, channel_name, time = self.bot.sniped_messages[ctx.channel.id]
        except:
            contents, author, channel_name, time = self.bot.sniped_messages[ctx.channel.id]

        try:
            embed = discord.Embed(description = contents, color = 0x326BF7, timestamp = time)
            embed.set_image(url = nab_proxy_url)
            embed.set_author(name = {author}, icon_url = author.avatar_url)
            embed.set_footer(text = f"Deleted in : #{channel_name}")
            await ctx.channel.send(embed = embed)
            
        except:
            embed = discord.Embed(description = contents, color = 0x326BF7, timestamp = time)
            embed.set_author(name = f"{author.name}#{author.discriminator}", icon_url = author.avatar_url)
            embed.set_footer(text = f"Deleted in : #{channel_name}")
            await ctx.channel.send(embed = embed)

    @snipe.error
    async def snipe_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are missing `MANAGE_MESSAGES` permission(s) to run this command!") 

        
        
def setup(bot):
    bot.add_cog(snipe(bot))

