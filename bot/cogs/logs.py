import discord
import json
from discord.ext import commands

class logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    async def gay(self, ctx, channel :discord.TextChannel):
        with open('channel.json', 'r') as f:
            channels = json.load(f)

        channels[str(ctx.guild.id)] = channel

        with open('channel.json', 'w') as f: 
            json.dump(channels, f, indent=4)

        await ctx.send(f"Logging has been set to {channel.mention}")


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author == self.bot.user: return
        if message.author.bot: return


        if message.attachments:
            embed = discord.Embed(description = message.content, color = 0x326BF7)
            embed.set_image(url=message.attachments[0].proxy_url)
            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            embed.set_footer(text=f"ID: {message.id}")
            embed.timestamp = message.created_at
            channels = discord.utils.get(self.bot.get_all_channels(), guild__name='ideas')
            await channels.send(embed=embed)
        else:
            deleted = discord.Embed(title=f"Message deleted in #{message.channel.name}", description=message.content, color=0x4040EC)
            ##deleted.set_author(name=message.author,  icon_url=message.author.avatar_url)
            deleted.add_field(name="Content",value=message.content)
            deleted.set_footer(text=f"ID: {message.id}")
            deleted.timestamp = message.created_at
            channels = discord.utils.get(self.bot.get_all_channels(), guild__name='ideas')
            await channels.send(embed=deleted)




def setup(bot):
    bot.add_cog(logs(bot))