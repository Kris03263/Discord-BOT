import discord
import random
import json
from discord.ext import commands
from discord.ext.commands import Bot, cog
class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
