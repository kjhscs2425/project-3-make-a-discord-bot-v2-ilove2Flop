"""
Do NOT modify this file
(At least at first)

Instead, modify the functions in `my_bot.py`
"""

import os
import discord
import my_bot
from secret import *

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    try:
        print(f"Received message: {message.content}")
        
        if message.author.display_name == "sir.duck.alot":
            print("Message from sir.duck.alot")
            await message.channel.send("Hello, sir.duck.alot! How can I assist you today?")
        
        if message.channel.name == "james_bot":  
            if message.author != client.user: 
                user_name = message.author.display_name
                if my_bot.should_i_respond(message.content, user_name):
                    response = my_bot.respond(message.content, user_name)
                    await message.channel.send(response)
    except Exception as e:
        print(f"Error: {e}")

if my_secret:
    client.run(my_secret)
else:
    print("Error: DISCORD_BOT_TOKEN environment variable not set.")
