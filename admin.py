import discord
from discord.ext import commands

class AdminCommands(commands.Cog):

	def __init__(self, client):
		self.client = client
#CLEAR
	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount : int):
		await ctx.channel.purge(limit=amount + 1) #purges or clears amount amount of messages, with a default value of 5
#KICK
	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member : discord.Member, *,reason=None):
		await member.kick(reason=reason)
		await ctx.send(f"Kicked {member.name}#{member.discriminator}")
#BAN
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member :discord.Member, *,reason=None):
		await member.ban(reason=reason)
		await ctx.send(f"Banned {member.name}#{member.discriminator}")
#UNBAN
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, *,member):
		banned_users = await ctx.guild.bans() #generates a banned entry of all banned users
		member_name, member_discriminator = member.split("#") #splits

		for ban_entry in banned_users: #for each member in the ban entry, checks if its the same person you want to unban
			user = ban_entry.user

			if (user.name, user.discriminator) == (member.name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f"Unbanned {user.name}#{user.discriminator}")

#ERROR HANDLING
	#Handling Clear Error
	@clear.error
	async def clear_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("ERROR: MissingRequiredArgument, Please specify how many messages you want to delete.")
	#Handling Kick Error
	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("ERROR: MissingRequiredArgument, Please mention who you want to kick.")
	#Handling Ban Error
	@ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("ERROR: MissingRequiredArgument, Please mention who you want to ban.")
	#Handling Unban Error
	@unban.error
	async def unban_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("ERROR: MissingRequiredArgument, Please mention who you want to unban.")

def setup(client):
	client.add_cog(AdminCommands(client))