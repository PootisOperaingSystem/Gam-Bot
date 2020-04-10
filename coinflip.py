import discord
from discord.ext import commands
import random

class CoinFlip(commands.Cog):

	def __init__(self, client):
		self.client = client

	#Commands
	@commands.command(aliases=["cf", "50/50", "50-50", "fifty-fifty"])
	async def coinflip(self, ctx, side):
		outcome = (random.randint(0, 1)) #Only outputs 0 or 1
		if outcome == 0:
			outcome = 'heads'
		elif outcome == 1:
			outcome = 'tails'
		if outcome == side.lower():
			await ctx.send("You Win!")
		elif outcome != side.lower():
			await ctx.send("You Lose!")
	#Need to add currencies & Loss/Gain of money

		

def setup(client):
	client.add_cog(CoinFlip(client))