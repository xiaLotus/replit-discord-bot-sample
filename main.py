from discord.ext import commands
import discord
import os
import asyncio
import keep_alive

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(
    command_prefix = "!",
    intents = intents
)


@bot.event
async def on_ready():
  print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def load(ctx, extensions):
  bot.load_extension(f"cmds.{extensions}")
  await ctx.send(f"Load {extensions}")

@bot.command()
async def unload(ctx, extensions):
  bot.unload_extension(f"cmds.{extensions}")
  await ctx.send(f"Unload {extensions}")

async def load_extensions():
  for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
      await bot.load_extension(f"cmds.{filename[:-3]}") 

async def main():
    async with bot:
      await load_extensions()
      # can use json to change the text
      await bot.start('Your Discord Bot Token')

if __name__ == '__main__':
  keep_alive.keep_alive()
  asyncio.run(main())
  # can use json to change the text
  bot.run('Your Discord Bot Token')
      


