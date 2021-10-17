import discord
import os
from dotenv import load_dotenv
import requests
import constant

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
FUN_API_KEY = os.getenv('FUN_API_KEY')

postHeader = {"X-Funtranslations-Api-Secret": FUN_API_KEY}

intents = discord.Intents.default()
client = discord.Client(intents=intents)

print("Client loaded: " + client)

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):

    msgParts = str(message.content).split()

    cmd = msgParts[0]
    msgParts.pop(0)
    args = msgParts
    if cmd[0] != constant.PREFIX:
        return
    cmd = cmd[1:]
    print(msgParts)
    if message.author == client.user or message.author.bot:
        return
    elif cmd == "test":
        await message.reply("Never Should've Come Here!")
    elif cmd == "dova":
        textToTranslate = " ".join(args)
        postParams = {"text": textToTranslate, "translation": "thuum"}
        result = requests.post(constant.TRANSLATOR_URL,data=postParams, headers=postHeader)
        jsonResponse = result.json()
        translation = jsonResponse["contents"]["translated"]
        print(jsonResponse)
        await message.reply(translation)
    else:
        await message.reply("Command '" + cmd + "' unknown")

client.run(DISCORD_BOT_TOKEN)