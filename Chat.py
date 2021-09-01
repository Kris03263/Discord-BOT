import discord
import random
import json
from discord.ext import commands
from discord.ext.commands import Bot, cog
from classes import Cog_Extension
with open('Chat.JSON',mode="r",encoding='utf8') as Gua:
        GuaPP = json.load(Gua)

class Mes(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.author != self.bot.user:
            if "呱" == msg.content or "呱呱" == msg.content:
                await msg.channel.send("呱你媽")

            elif "鴨" in msg.content or "你是張啟鋒嗎" in msg.content:
                z = random
                await msg.channel.send("我是"+random.choice(GuaPP["GuaRP3"])+"好嗎")

            elif "隨機呱呱" in msg.content:
                await msg.channel.send(random.choice(GuaPP["Guajpg"]))

            elif "呱呱食物" == msg.content:
                num =random.randrange(len(GuaPP["GuaRP1"]))
                await msg.channel.send(GuaPP["GuaRP1"][num])
                await msg.channel.send(GuaPP["GuaRP2"][num])

            elif "叫" in msg.content:
                arr = ["不要阿","呱"]
                await msg.channel.send(random.choice(arr))

            elif "笑死" in msg.content:
                num = random.randrange(len(GuaPP["GuaRP6"]))
                await msg.channel.send(GuaPP["GuaRP6"][num])

            elif "xd" in msg.content or "xD" in msg.content or "XD" in msg.content:
                await msg.channel.send("笑屁喔")
            
            elif "幹" in msg.content:
                await msg.channel.send("笑死")

            elif "quack" == msg.content:
                await msg.channel.send("https://i.imgur.com/yqBSN19.mp4")

            elif "張啟鋒" in msg.content:
                num1 = random.randrange(len(GuaPP["GuaRP4"]))
                await msg.channel.send(GuaPP["GuaRP4"][num1])

            elif "你是不是螃蟹" == msg.content:
                await msg.channel.send("Bingo,答對囉")

            elif "呱呱跳舞" == msg.content:
                await msg.channel.send('https://i.imgur.com/GXqnoax.mp4')

            elif "烤" in msg.content:
                await msg.channel.send('來烤阿機掰人 屌你祖宗十八代')

            elif "Fuck" in msg.content:
                await msg.channel.send('又舔嘴唇!')
            
            elif "qq" in msg.content or "QQ" in msg.content:
                await msg.channel.send('很難過欸')

            elif "ok" in msg.content or "OK" in msg.content:
                await msg.channel.send('好欸')

            elif "?" == msg.content:
                num3 = random.randrange(len(GuaPP["GuaRP7"]))
                await msg.channel.send(GuaPP["GuaRP7"][num3])
        else:
            await self.bot.process_commands(msg)

def setup(bot):
    bot.add_cog(Mes(bot))
