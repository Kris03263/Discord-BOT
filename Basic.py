import discord
import random
import json
import sys
import requests
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot, cog
from classes import Cog_Extension

class Basic(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        Now = 0
        print(">>bot online<<")
        await self.bot.change_presence(status=discord.Status.online, activity = discord.Game("氣象呱查員"))
        while True:
            await asyncio.sleep(10)
            channel =  self.bot.get_channel(875603565203316766)
            url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=CWB-5C60CAF7-5596-451E-B4DF-4B9CC51ABB59&downloadType=WEB&format=JSON'
            # 要求網站回傳
            res = requests.get(url)
            # 將回傳值的 json 檔丟入 data_we
            data_qu = res.json()
            if data_qu['records']['earthquake'][0]['earthquakeNo'] != Now:
                Now = data_qu['records']['earthquake'][0]['earthquakeNo']
                # 顯示數值
                embed=discord.Embed(title="*地震報告*", url="https://www.cwb.gov.tw/V8/C/", description="來自呱呱特派員", color=0xb806f9)
                embed.set_author(name="中央氣象局", url="https://www.cwb.gov.tw/V8/C/", icon_url="https://i.imgur.com/MOL5A8l.jpg")
                embed.add_field(name="報告編號", value=data_qu['records']['earthquake'][0]['earthquakeNo'], inline=True)
                embed.add_field(name="跌倒時間", value=data_qu['records']['earthquake'][0]['earthquakeInfo']['originTime'], inline=True)
                embed.add_field(name="在哪跌倒", value=data_qu['records']['earthquake'][0]['earthquakeInfo']['epiCenter']['location'], inline=False)
                embed.add_field(name="芮氏規模", value=data_qu['records']['earthquake'][0]['earthquakeInfo']['magnitude']['magnitudeValue'], inline=True)
                embed.add_field(name="深度(公里)", value=data_qu['records']['earthquake'][0]['earthquakeInfo']['depth']["value"], inline=True)
                await channel.send(embed=embed)
            
            

def setup(bot):
    bot.add_cog(Basic(bot))
