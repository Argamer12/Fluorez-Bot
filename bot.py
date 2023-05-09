from multiprocessing import log_to_stderr
from multiprocessing.spawn import get_preparation_data
from sys import builtin_module_names
from turtle import title
import discord
from discord.ext import commands
from discord.ext.commands import bot
import urllib
import random
import json
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix=',', intents=intents)
client.remove_command("help")
case_insensitive=True
bot.author_id = 709247944309735505

  
#Prefix Defining
@client.event
async def on_ready():
  print("Bot is working.")


#Just a testing command
@client.command()
async def hi(ctx):
  await ctx.send("Hello!")


#1- once ",hello" is sent, the bot tell that it is online.
@client.command(name="online", aliases=["working", "up", "on"])
async def online(ctx):
  await ctx.send("Hi, the bot is functioning correctly.")


#2- rules command
@client.command(name="rules",
                aliases=["rule", "RULES", "Rules", "RULE", "Rule"])
async def rules(ctx):
  embed = discord.Embed(
    title="Rules", description="These are the basic rules u need to follow.")
  embed.set_author(name="Retro Palm Studios")
  embed.add_field(name="__1 – Spamming, Raiding or Unwanted Messages___",
                  value="""1.1 | Excessive use of emojis, or capitalization
                                                                               1.2 | Excessive & unnecessary use of spoilers
                                                                               1.3 | Posting NSFW or abusive content
                                                                               1.4 | Mass pinging members or moderators
                                                                               1.5 | Raiding, Spamming or sending unnecessary messages in the server or DM's
                                                                               1.6 | Advertising in server except 'self promotion' channel
                                                                               1.7 | Discord Server invite links are strictly not allowed
                                                                               -------------------------------------------------------------------------------------------""",
                  inline=False)
  embed.add_field(
    name="__2 – Harassing, Trolling or Swearing__",
    value="""2.1 | Jokes on Religion, Caste, Politics, or cultural groups
                                                                        2.2 | Abusing, Swearing or harassing members in server or DM's
                                                                        2.3 | Harassment or Trolling via fake account or alternative account
                                                                        2.4 | Sharing anyone's personal or professional details without their permission
                                                                        2.5 | Sharing anyone's DM screenshots without their concern and permission
                                                                        -------------------------------------------------------------------------------------------""",
    inline=False)
  embed.add_field(
    name="__3 – Other Violations__",
    value="""3.1 | Money Fraud on the name of giveaways or in other form
                                                         3.2 | Misbehaving with moderators or administrators
                                                         3.3 | Death threats or suicidal encouragement in any way
                                                         3.4 | Inappropriate usernames which is hard to mention or inappropriate profile pic
                                                         3.5 | Abusive or NSFW account name, nickname, profile picture or/and custom status
                                                         3.6 | Begging for roles in the server or in Moderator's DM
                                                         -------------------------------------------------------------------------------------------""",
    inline=False)
  embed.add_field(
    name="__4 – Discord Privacy Policy & terms of Service__",
    value=
    """4.1 | Violating Discord Terms of Service : https://discordapp.com/terms
                                                                                  4.2 | Violating Discord Privacy Policy : https://discordapp.com/privacy
                                                                                 -------------------------------------------------------------------------------------------
                                                                                 -------------------------------------------------------------------------------------------""",
    inline=False)
  embed.set_footer(
    text="Please follow these rules or you will get some serious punishments.")
  await ctx.send(embed=embed)


#3- purge command
@client.command(name="clear", aliases=["delete", "remove", "purge", "del"])
@commands.has_permissions(manage_messages=True)
async def Clear(ctx, amount=2):
  await ctx.channel.purge(limit=amount)


#4- kick commands
@client.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  if reason == None:
    reason = " NO REASON PROVIDED"
  await ctx.guild.kick(member)
  kick_log = client.get_channel(887292002499182612)
  await kick_log.send(
    f'Moderator {ctx.author.mention} has kicked {member.mention}. The reason provided is {reason}'
  )


#5- ban command
@client.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  if reason == None:
    reason = " NO REASON PROVIDED"
  await member.ban(reason=reason)
  ban_log = client.get_channel(887292002499182612)
  await ban_log.send(
    f'Moderator {ctx.author.mention} has banned {member.mention}. The reason provided is {reason}'
  )


#6- meme command
@client.command(name="meme", aliases=["MEME", "memer", "emem", "meem", "emme"])
async def meme(ctx):
  memeApi = urllib.request.urlopen('https://meme-api.com/gimme')
  memeData = json.load(memeApi)
  memeUrl = memeData['url']
  memeName = memeData['title']
  memePoster = memeData['author']
  memeSub = memeData['subreddit']
  memeLink = memeData['postLink']

  embed = discord.Embed(title=memeName)
  embed.set_image(url=memeUrl)
  embed.set_footer(
    text=f"Meme by: {memePoster} | Subreddit: {memeSub} | Post: {memeLink}")
  await ctx.send(embed=embed)


#7- games command
@client.command(name="games",
                aliases=["Games", "GAMES", "Game", "game", "GAME", "gamelist"])
async def games(ctx):
  embed = discord.Embed(
    title="Games",
    description="These are all the games we have released/plan to release.",
  )
  embed.set_author(name="Retro Palm Studios")
  embed.add_field(name="__1. Steam: The Game__",
                  value="""Genre: Adventure, Open World 
                                                            Status: Released
                                                            Release Date: 30-7-2020
                                                            Condition: Unstable(Updated Regularly)
                                                            Description:
                                                            
                                                            
                                                            [Click here for the game link](https://www.roblox.com/games/5463177142/Steam-The-Game)
                                                            -------------------------------------------------------------------------------------------""",
                  inline=False)
  embed.add_field(name="__2. Blackout__",
                  value=""""Genre: Showcase
                                                      Status: Released
                                                      Release Date: 21-2-2022
                                                      Condition: Stable
                                                      Description:
                                                      
                                                      
                                                      [Click here for the game link](https://www.roblox.com/games/8892052055/Blackout)
                                                      -------------------------------------------------------------------------------------------""",
                  inline=False)
  embed.add_field(name="__3. Fazbear's Fright: Reopening__",
                  value=""""Genre: Horror
                                                                         Status: UnReleased
                                                                         Release Date: TBA (Delayed- no new timings announced)
                                                                         Condition: Development Paused
                                                                         Description:
                                                      
                                                      
                                                                         -------------------------------------------------------------------------------------------""",
                  inline=False)
  embed.add_field(name="__4. Dead Dreams__",
                  value=""""Genre: Horror
                                                         Status: UnReleased
                                                         Release Date: TBA (Early/Mid 2023)
                                                         Condition: Under Development
                                                         Description:
                                                      
                                                      
                                                         -------------------------------------------------------------------------------------------""",
                  inline=False)
  embed.set_footer(
    text=
    "Thanks for reading! Please support us by playing our games and giving us feedbacks."
  )
  await ctx.send(embed=embed)


@client.command(name="help",
                aliases=["HELP", "Help", "commands", "Commands", "COMMANDS"])
async def help(ctx):
  embed = discord.Embed(title="Commands List")
  embed.set_author(name="Retro Palm Studios")
  embed.add_field(name="Syntax",
                  value="""The prefix used is `,`
                                            Syntax is `,<Command name>`""",
                  inline=False)
  embed.add_field(name="1. Rules",
                  value="""Shows the list of rules in our server.
                                              Aliases: "rules", "rule", "RULES", "Rules", "RULE", "Rule"
                                              
                                              Permissions required: none
                                              ____
                                              """,
                  inline=False)
  embed.add_field(name="2. Memes",
                  value="""Picks a random meme from reddit and shows it to you.
                                              Aliases: "meme", "MEME", "memer", "emem", "meem", "emme"
                                              
                                              Permissions required: none
                                              ____
                                              """,
                  inline=False)
  embed.add_field(name="3. Games",
                  value="""Shows the list of games we have worked/working on.
                                              Aliases: "games", "Games", "GAMES", "Game", "game", "GAME", "gamelist"
                                              
                                              Permissions required: none
                                              ____
                                              """,
                  inline=False)
  embed.add_field(name="4. Purge",
                  value="""Deletes the number of messages entered.
                                              Aliases: "clear", "delete", "remove", "purge", "del"
                                              Syntax: `:purge <number of messages>`

                                              Permissions required: Manage_Messages
                                              ____
                                              """,
                  inline=False)
  embed.add_field(name="5. Kick",
                  value="""Kicks the member.
                                              Aliases: "kick"
                                              Syntax: `:kick <member> <reason>`

                                              Permissions required: kick_members
                                              ____
                                              """,
                  inline=False)
  embed.add_field(name="6. Ban",
                  value="""Bans the member.
                                              Aliases: "ban"
                                              Syntax: `:ban <member> <reason>`

                                              Permissions required: ban_members
                                              ____
                                              """,
                  inline=False)
  embed.set_footer(
    text=
    "Please contact the moderators if you feel something is wrong or if you are confused."
  )
  await ctx.send(embed=embed)

keep_alive()
bot.run('OTg1MjI4MDM1Mjk5MDgyMjkw.GI847J.LNzszcijvHkPWeUvaI_QYsatFfYZd7p1lyL4Ug')
