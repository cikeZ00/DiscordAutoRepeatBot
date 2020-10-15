import discord, json
from discord.ext import commands

with open("config.json") as f:
    config = json.load(f)

def write_config(change):
    with open("config.json", 'w') as f:
        json.dump(change, f, indent=4)

class repeat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.counter = 0

    @commands.has_permissions(administrator=True)
    @commands.command(name="setmessage", description="Repeat specified")
    async def setmessaget(self, ctx, message):
        config["Settings")]["repeat"] = str(message)
        write_config(config)

    @commands.has_permissions(administrator=True)
    @commands.command(name="settime", description="Set time in seconds (Default: 60)")
    async def settime(self, ctx, message):
        config["Settings")]["seconds"] = int(message)
        write_config(config)

    @commands.has_permissions(administrator=True)
    @commands.command(name="setchannel", description="Set channel (ID)")
    async def setchannel(self, ctx, message):
        config["Settings")]["channel"] = int(message)
        write_config(config)

def setup(bot):
    bot.add_cog(repeat(bot))
