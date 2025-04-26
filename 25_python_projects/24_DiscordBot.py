# Requires 'discord.py': pip install discord.py
# Get bot token from https://discord.com/developers/applications
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello from the bot!")

if __name__ == "__main__":
    print("Get a bot token from https://discord.com/developers/applications")
    bot.run("YOUR_BOT_TOKEN")  # Replace with your Discord bot token