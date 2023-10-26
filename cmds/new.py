from discord.ext import commands
import discord

# class can change
class new(commands.Cog):
    # stereotype
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Your commands
    # you can write here for @commands.command()


# stereotype
async def setup(bot: commands.Bot):
    # change the class name
    await bot.add_cog(new(bot))