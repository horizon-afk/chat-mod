import discord
import json
import mod

#loads config file from config.json
configFile = open("config.json", "r")
configData = json.load(configFile)
token = configData['token']
configFile.close()

bot = discord.Client()
#prompts when the bot is ready to use
@bot.event
async def on_ready():
    print("The bot's ready!")

#triggers when a message is sent
@bot.event
async def on_message(message):
    mod.message = message.content
    mod.channel = message.channel
    purge = mod.deleteMsg()
    
    if (purge == True):
        await message.channel.purge(limit=1)


#the main function to run the bot
bot.run(token)