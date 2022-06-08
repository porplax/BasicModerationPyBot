import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

client = commands.Bot(command_prefix="== ")

@client.event
async def on_ready():
    return print("it is the time to moderate 👀")
    
"""
Moderator commands.

KICK : BAN : MUTE
"""
# Kicks a discord member from the current guild. 
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member):
    await member.kick()
    return await ctx.send(f"Successfully kicked {member} from the guild.")

# Error if user does not meet permissions for ban.
@kick.error 
async def kick_err(ctx, error):
    if isinstance(error, MissingPermissions):
        return await ctx.send("You don't have the required permissions for kick!")

# Bans a discord member from the current guild.
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    return await ctx.send(f"Sucessfully banned {member} from the guild.")

# Error if user does not meet permissions for ban.
@ban.error 
async def ban_err(ctx, error):
    if isinstance(error, MissingPermissions):
        return await ctx.send("You don't have the required permissions for ban!")

# Temporary mutes a discord member in the current guild. (With the appropriate role ofc.)
@client.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, member : discord.Member, role : discord.Role):
    if role in member.roles:
        await member.remove_roles(role)
        return await ctx.send(f"Unmuted {member} from the guild!")
    else:
        await member.add_roles(role)
        return await ctx.send(f"Muted {member} from the guild!") 

# Error if user does not meet permissions for ban.
@mute.error 
async def mute_err(ctx, error):
    if isinstance(error, MissingPermissions):
        return await ctx.send("You don't have the required permissions for mute!")

@client.command()
async def devtool(ctx):
    return await ctx.send(ctx.message.author.guild_permissions)

client.run("")
