import discord
from discord.ext import commands

class Ping(commands.Cog):

	def __init__(self, client):
		self.client = client

	#Commands
	@commands.command()
	async def ping(self, ctx):
		await ctx.send("Pong!")

def setup(client):
	client.add_cog(Ping(client))