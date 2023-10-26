from discord.ext import commands
import discord
import os

# of Cog_Extension
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
