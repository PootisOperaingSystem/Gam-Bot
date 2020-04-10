import discord
from discord.ext import commands
import random
class magicball(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command(aliases=["8ball", "magic_conch"]) #The aliases still invoke the command when called
	async def eightball(self, ctx, *, question): #this is spelled out because we cant start definitions with numbers
		responses = ["It is certain.", #Yes
	 				 "It is decidedly so.",
					 "Without a doubt.",
					 "Yes - definitely.",
	 				 "You may rely on it.",
					 "As I see it, yes.",
	 				 "Most likely.",
	 				 "Outlook good.",
					 "Yes.",
					 "Signs point to yes.",
					 "Reply hazy, try again.", #Maybe
					 "Ask again later.",
					 "Better not tell you now.",
				 	 "Cannot predict now.",
	 				 "Concentrate and ask again.",
					 "Don't count on it.", #Nos
					 "My reply is no.",
					 "My sources say no.",
					 "Outlook not so good.",
					 "Very doubtful."]
		await ctx.send(f"{random.choice(responses)}")

def setup(client):
	client.add_cog(magicball(client))