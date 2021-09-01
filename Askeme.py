import discord
import random
import json
import sys
import requests
from discord.ext import commands
from discord.ext.commands import Bot, cog
from classes import Cog_Extension
from datetime import datetime, timezone, timedelta

with open('Chat.JSON',mode="r",encoding='utf8') as Gua:
        GuaPP = json.load(Gua)

class who(Cog_Extension):       
    @commands.command()
    async def 我是誰(self,ctx): 
        await ctx.send(random.choice(GuaPP["GuaRP5"]))
def setup(bot):
    bot.add_cog(who(bot))
