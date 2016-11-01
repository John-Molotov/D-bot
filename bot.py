#imports
import time
import string
import logging
import discord
import asyncio

#read dictionary
words = []
dictin = open("dictionary", "a+")
dictin.seek(0)
dictionary = dictin.readlines()
for i in range(0, len(dictionary)):
    words.append(dictionary[i].rstrip())

#logging
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
format = logging.Formatter("%(asctime)s: %(name)s_%(levelname)s: %(message)s")
date = time.strftime("%d.%m.%Y(%I.%M.%S)")

#text logs
txtlog = logging.FileHandler(filename="logs\\"+date+".log", encoding="utf-8", mode="w")
txtlog.setLevel(logging.INFO)
txtlog.setFormatter(format)
logger.addHandler(txtlog)

#console logs
conlog = logging.StreamHandler()
conlog.setLevel(logging.WARNING)
conlog.setFormatter(format)
logger.addHandler(conlog)

#debug logs
buglog = logging.FileHandler(filename="logs\\debug\\"+date+".log", encoding="utf-8", mode="w")
buglog.setLevel(logging.DEBUG)
buglog.setFormatter(format)
logger.addHandler(buglog)

#login
client = discord.Client()
@client.event
async def on_ready():
    print("Logged in as " + str(client.user.name) + "(" + str(client.user.id) + ")")
    print("------")
    
#message recieved
@client.event
async def on_message(message):
    #simple words code
    if(str(message.channel)=="simple_word_room"):
        text = str(message.content).translate(dict.fromkeys(map(ord, string.punctuation))).split()
        for i in range(0, len(text)):
            if not text[i] in words:
                await client.send_message(message.channel, "please speak simple words")
                await client.delete_message(message)
    
client.run("MjQyNjI3NjY5MjExMDg2ODQ4.CvmRgQ.Xcf7Ycyc1mjFv2oXJHqEDx8VWFU")
