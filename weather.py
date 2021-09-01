import discord
import random
import json
import sys
import requests
from discord.ext import commands
from discord.ext.commands import Bot, cog
from classes import Cog_Extension
from datetime import datetime, timezone, timedelta
class wea(Cog_Extension):
    @commands.command()  
    async def 天氣(self,ctx,area):
        key = {
        '連江': 0, '金門': 1, '宜蘭': 2, '新竹': 3, 
        '苗栗': 4, '彰化': 5, '南投': 6, '雲林': 7, 
        '嘉義': 8, '屏東': 9, '臺東': 10,'台東':10,'花蓮': 11, 
        '澎湖': 12, '基隆': 13, '新竹': 14, '嘉義': 15, 
        '臺北': 16,'台北':16, '高雄': 17, '新北': 18, '臺中': 19, '台中': 19,
        '臺南': 20,'台南':20, '桃園': 21 }
        url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-D0047-091?Authorization=CWB-97AF1200-D64F-4BD7-BFBA-C8E9892538FC&downloadType=WEB&format=JSON'
        # 要求網站回傳
        res = requests.get(url)
        # 將回傳值的 json 檔丟入 data_we
        data_we = res.json()
        description = data_we['cwbopendata']['dataset']['locations']['location'][key[area]]['weatherElement'][14]['time'][0]['elementValue']['value'] # 氣象描述
        # 地理位置
        location = data_we['cwbopendata']['dataset']['locations']['location'][key[area]]['locationName']
        await ctx.send((location+"天氣:\n"+"```\n"+description+"```\n"))
def setup(bot):
    bot.add_cog(wea(bot))
