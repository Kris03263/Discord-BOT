import discord
import random
import json
from discord.ext import commands
from discord.ext.commands import Bot, cog
from classes import Cog_Extension

class Delete(Cog_Extension):
    @commands.Cog.listener()
    async def on_message_delete(self,msg):
        if msg.author != self.bot.user:
            channel = self.bot.get_channel(873941760647245835)
            embed=discord.Embed(title="抓到囉", color=0xdb08f7)
            embed.set_author(name="呱呱", url="https://i.imgur.com/GXqnoax.mp4")
            embed.add_field(name="作者", value=msg.author, inline=True)
            embed.add_field(name="所在頻道", value=msg.channel, inline=True)
            embed.add_field(name="刪除的訊息內容", value=msg.content, inline=True)
            await channel.send(embed=embed)
        else:
            await self.bot.process_commands(msg)

def setup(bot):
    bot.add_cog(Delete(bot))
