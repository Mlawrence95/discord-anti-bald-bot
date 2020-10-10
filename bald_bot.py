import discord
import json
import numpy as np
from discord.ext import commands

# credentials
cred_path = r"C:\Users\Mike\Documents\credentials\discord_creds.json"
with open(cred_path, 'r') as cred_handle:
	creds = json.load(cred_handle)

# balds
balds = ['Aang', 'Little Bill', 'Stewie', 'Jeff Bezos', 
         'Caillou', 'Mr. Clean', 'Arthur', 'Numba 1',
         'David', 'Charlie Brown']

bot = commands.Bot(command_prefix='$', case_insensitive=True)

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')
	
@bot.event
async def on_message(message):
	#if str(message.channel) == "anti-bald-child-chat":
	if message.author != bot.user:
		if "bald" in str(message.content).lower():
			bald_kid = np.random.choice(balds)
			await message.channel.send(f'Bald? FUCK them bald kids! FUCK {bald_kid}!')

bot.run(creds['bot_secret'])
