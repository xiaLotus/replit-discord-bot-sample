from discord.ext import commands
import discord

# class can change
class hello(commands.Cog):
    # stereotype
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Your commands
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hi! <@{ctx.author.id}>")

# stereotype
async def setup(bot: commands.Bot):
    # change the class name
    await bot.add_cog(hello(bot))