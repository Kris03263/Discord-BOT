import discord
import random
import json
from discord.ext import commands
from discord.ext.commands import Bot, cog
from classes import Cog_Extension


with open('Chat.JSON',mode="r",encoding='utf8') as Gua:
        GuaPP = json.load(Gua)
class Command(Cog_Extension):

    @commands.command()
    async def duck(self,ctx): # 指令 re 重新讀取和寫入 json
        await ctx.send("呱呱")

    @commands.command()
    async def Bang(self,ctx): 
        await ctx.send("https://i.imgur.com/7BWNSmk.png")

    @commands.command()
    async def Bur(self,ctx): 
        await ctx.send("https://i.imgur.com/YjrfnSD.png") 

    @commands.command()
    async def ping(self, ctx): 
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

def setup(bot):
    bot.add_cog(Command(bot))
