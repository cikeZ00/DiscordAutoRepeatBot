import json, os
from discord.ext import commands
from os import path

# CONFIG
if not path.exists("config.json"):
    with open('config.json', 'w') as configout:
        json.dump({
            "Discord":{
                "other": {
                    "token": "",
                    "prefix": "!",
                }
            },
            "Settings":{
                "repeat_message": "",
                "channel": None,
                "seconds": 60
            }
        }, configout, indent=4)
    print("[INFO] config.json generated!")
    quit()

else:
    with open("config.json") as f:
        config = json.load(f)

# Bot setup
bot = commands.Bot(command_prefix=config["Discord"].get("other").get("prefix"), case_insensitive=True, self_bot=False)

#Loading cogs
if __name__ == '__main__':
    for extension in os.listdir("modules"):
        if extension == "__pycache__":
            pass
        
        else:
            bot.load_extension("modules." + extension[:-3])


# Init bot with auth token
bot.run(config["Discord"].get("other").get("token"), bot=True)
