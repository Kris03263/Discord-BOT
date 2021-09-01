import discord
import random
import json
import requests
import time
import datetime
import os
from pprint import pprint
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='#') # 機器人指令的觸發文字

for Filename in os.listdir('DiscordBot/Functions'):
    if Filename.endswith('.py'):
        bot.load_extension(F'Functions.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run('Token') # bot 的 token
  
