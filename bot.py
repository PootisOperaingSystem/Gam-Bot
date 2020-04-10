"""
IMPORTING PACKAGES
"""

import discord
from discord.ext import commands, tasks
from itertools import cycle
import os

token = ""

"""
SETTING PREFIX
"""

client = commands.Bot(command_prefix = "$") #sets the prefix to "$"
client.remove_command("help")

statuses = cycle(["Hunter is Gay.", "No furries.", "Fuck hackers."])

"""
CREATING EVENTS
"""

#On Ready / Presence
@client.event
async def on_ready(): #Goes into ready state when ready
	change_status.start()
	print("Bot is ready.") #When bot is ready, it outputs the string into the command prompt
#Member Messages
@client.event
async def on_member_join(member):
	print(f'{member} has joined the server.') #when member joins, it outputs the string to the console.
@client.event
async def on_member_remove(member):
	print(f'{member} has left the server.') #when memeber leaves, it outputs the string to the console.

"""
CREATING COMMANDS
"""

def is_owner(ctx):
	return ctx.author.id == 171718014801149952


#Cog loading / unloading
@client.command()
@commands.check(is_owner)
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
@client.command()
@commands.check(is_owner)
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")

"""
ERROR HANDLING
"""

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("ERROR: CommandNotFound, Please enter a valid command.")


"""
LOADING COGS
"""

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

"""
TASKS
"""

#Changing the status every 30 seconds to the next one in the list
@tasks.loop(seconds=30)
async def change_status():
	await client.change_presence(activity=discord.Game(next(statuses)))

"""
RUNNING THE BOT
"""

client.run(token)
