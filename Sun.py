import requests
import discord
from discord.ext import commands
from discord.ext.commands import Bot, cog
from classes import Cog_Extension
from discord.ext import commands
from discord.ext.commands import Bot, cog
from classes import Cog_Extension
from datetime import datetime, timezone, timedelta
class sun(Cog_Extension):
    @commands.command()  
    async def Sunrise(self,ctx):
        tz = timezone(timedelta(hours=+8))
        tttime = datetime.now(tz)
        #tttime = datetime.datetime.now()
        url = str('https://opendata.cwb.gov.tw/api/v1/rest/datastore/A-B0062-001?Authorization=CWB-5C60CAF7-5596-451E-B4DF-4B9CC51ABB59&downloadType=web&format=JSON&locationName=&dataTime='+str(tttime.year)+'-'+str(tttime.month)+'-'+str(tttime.day)+'&sort=locationName')
        res = requests.get(url)
        # 將回傳值的 json 檔丟入 data_we
        Sundata = res.json()

        Sunrise =  Sundata["records"]["locations"]["location"]

        embed=discord.Embed(title=str(Sunrise[13]["time"][0]["dataTime"])+" 日出資料 :sunrise_over_mountains:", color=0xfff700)
        embed.set_author(name="中央氣象局", url="https://scweb.cwb.gov.tw/", icon_url="https://media.discordapp.net/attachments/345147297539162115/732527875839885312/ROC_CWB.png")
        embed.add_field(name="資料編號", value=str(Sundata["result"]["resource_id"]), inline=True)
        embed.add_field(name="資料日期", value=str(Sunrise[13]["time"][0]["dataTime"]), inline=True)
        embed.add_field(name=Sunrise[13]["locationName"], value=Sunrise[13]["time"][0]["parameter"][1]["parameterName"]+"-->"+Sunrise[13]["time"][0]["parameter"][1]["parameterValue"], inline=False)
        embed.add_field(name=Sunrise[12]["locationName"], value=Sunrise[12]["time"][0]["parameter"][1]["parameterName"]+"-->"+Sunrise[12]["time"][0]["parameter"][1]["parameterValue"], inline=False)
        embed.add_field(name=Sunrise[14]["locationName"], value=Sunrise[14]["time"][0]["parameter"][1]["parameterName"]+"-->"+Sunrise[14]["time"][0]["parameter"][1]["parameterValue"], inline=False)
        embed.add_field(name=Sunrise[15]["locationName"], value=Sunrise[15]["time"][0]["parameter"][1]["parameterName"]+"-->"+Sunrise[15]["time"][0]["parameter"][1]["parameterValue"], inline=False)
        embed.set_footer(text="報告提供：中央氣象局")
        await ctx.send(embed=embed)
    @commands.command()  
    async def Sunset(self,ctx):
        tz = timezone(timedelta(hours=+8))
        tttime = datetime.now(tz)
        #tttime = datetime.datetime.utcnow()
        url = str('https://opendata.cwb.gov.tw/api/v1/rest/datastore/A-B0062-001?Authorization=CWB-5C60CAF7-5596-451E-B4DF-4B9CC51ABB59&downloadType=web&format=JSON&locationName=&dataTime='+str(tttime.year)+'-'+str(tttime.month)+'-'+str(tttime.day)+'&sort=locationName')
        res = requests.get(url)
        # 將回傳值的 json 檔丟入 data_we
        Sundata = res.json()

        Sunset =  Sundata["records"]["locations"]["location"]

        embed=discord.Embed(title=str(Sunset[13]["time"][0]["dataTime"])+" 日落資料 :city_sunset:", description="來自呱呱特派員", color=0xb806f9)
        embed.set_author(name="中央氣象局", url="https://scweb.cwb.gov.tw/", icon_url="https://i.imgur.com/MOL5A8l.jpg")
        embed.add_field(name="資料編號", value=str(Sundata["result"]["resource_id"]), inline=True)
        embed.add_field(name="資料日期", value=str(Sunset[13]["time"][0]["dataTime"]), inline=True)
        embed.add_field(name=Sunset[13]["locationName"], value=Sunset[13]["time"][0]["parameter"][5]["parameterName"]+"-->"+Sunset[13]["time"][0]["parameter"][5]["parameterValue"], inline=False)
        embed.add_field(name=Sunset[12]["locationName"], value=Sunset[12]["time"][0]["parameter"][5]["parameterName"]+"-->"+Sunset[12]["time"][0]["parameter"][5]["parameterValue"], inline=False)
        embed.add_field(name=Sunset[14]["locationName"], value=Sunset[14]["time"][0]["parameter"][5]["parameterName"]+"-->"+Sunset[14]["time"][0]["parameter"][5]["parameterValue"], inline=False)
        embed.add_field(name=Sunset[15]["locationName"], value=Sunset[15]["time"][0]["parameter"][5]["parameterName"]+"-->"+Sunset[15]["time"][0]["parameter"][5]["parameterValue"], inline=False)
        embed.set_footer(text="報告提供：中央氣象局")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(sun(bot))
