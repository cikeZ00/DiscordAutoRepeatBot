import asyncio
import time

from discord.ext import commands, tasks
import json
import discord

with open("config.json") as f:
    config = json.load(f)

class repeat_servie(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.counter = 0

    #Event
    @tasks.loop(seconds=int(config["Settings"].get("seconds")))
    async def repeat_event(self):
        print("Called")
        with open("config.json") as f:
            config = json.load(f)
        channel = self.bot.get_channel(config["Settings"].get("channel"))
        await channel.send(config["Settings"].get("repeat_message"))

    #Start on boot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot starting")
        if config["Settings"].get("repeat_message") != "":
            self.repeat_event.start()
            print("[INFO] Repeat service started!")
        
        await self.bot.change_presence(
            activity=discord.Game(name="Type: " + config["Discord"].get("other").get("prefix") + "help", type=1))

    #Start/Stop Commands
    @commands.has_permissions(administrator=True)
    @commands.command(name="service", description="Start/Stop service \n``Usage: service <start/stop>``")
    async def manage_service(self, ctx, option=None):
        if option == "start":
            self.repeat_event.start()
            await ctx.send("Service started.")
        elif option == "stop":
            self.repeat_event.cancel()
            await ctx.send("Service stopped.")

def setup(bot):
    bot.add_cog(repeat_servie(bot))
