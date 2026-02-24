import discord # Imports the discord.py library ( Python API wrapper for Discord  )
from discord.ext import commands # Imports the commands extension from discord.ext
import os # Imports Python's built-in os module, which provides functions for interacting with the os
from dotenv import load_dotenv # Imports the load_dotenv function from python-dotenv package. It allows to load environment variables from a .env file into project.

load_dotenv() # Loads the environment variables from .env file into this script. ( Bot token are stocked in .env file )
intents = discord.Intents.default() # Creates an intents object with the default permissions. Intents are Discord's way of allowing bots to suscribe to specific events.
intents.message_content = True # Enables the message_content intent. Without this, your bot won't be able to read what users type in messages.
bot = commands.Bot(command_prefix='!', intents=intents) # Creates an instance of the bot using the commands.Bot class. intents=intents : Passed the intents object configured earlier, so the bot has the necessary permissions.

@bot.event
async def on_ready(): 
	print(f'{bot.user} connected.')
	try:
		synced = await bot.tree.sync()
		print(f"Synced {len(synced)} command(s)")
	except Exception as e:
		print(e)

auto_responses = {
	"12": "Hello, malheureusement le serveur est réservé aux personnes ayant **18 ans** ou plus, désolé :pray:",
	"13": "Hello, malheureusement le serveur est réservé aux personnes ayant **18 ans** ou plus, désolé :pray:",
	"14": "Hello, malheureusement le serveur est réservé aux personnes ayant **18 ans** ou plus, désolé :pray:",
	"15": "Hello, malheureusement le serveur est réservé aux personnes ayant **18 ans** ou plus, désolé :pray:",
	"16": "Hello, malheureusement le serveur est réservé aux personnes ayant **18 ans** ou plus, désolé :pray:",
	"17": "Hello, peux-tu nous préciser ton année de naissance ? Merci :pray:"
}

CHANNEL_ID = None;
CATEGORY_ID = 1475759911114768415
ROLE_IDS = [1475760523231494245, 1475762318468976723]

@bot.event
async def on_message(message):
	# Ignore messages from the bot itself
	if message.author == bot.user:
		return
	if CHANNEL_ID is not None and message.channel.id != CHANNEL_ID:
		await bot.process_commands(message)
		return
	if CATEGORY_ID is not None and message.channel.category_id != CATEGORY_ID:
		await bot.process_commands(message)
		return
	has_role = any(role.id in ROLE_IDS for role in message.author.roles)
	if not has_role:
		await bot.process_commands(message)
		return
	msg_lower = message.content.lower()
	for word, response in auto_responses.items():
		if word in msg_lower:
			await message.reply(response)
			break # Only one reply per message to avoid spam
	await bot.process_commands(message)

bot.run(os.getenv('DISCORD_TOKEN'))
