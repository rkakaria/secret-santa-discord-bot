import os
import discord
from dotenv import load_dotenv
from datetime import datetime
import random

# load bot token
load_dotenv()
TOKEN = str(os.getenv("DISCORD_TOKEN"))

# set up bot
intents = discord.Intents.default()
intents.members = True # allow access to member list of a channel
bot = discord.Bot(intents = intents)

# terminal message when bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")

# main assignation function
@bot.slash_command(name = "assign-secret-santa", description = "DM participants with Secret Santa assignments")
async def assign(ctx: discord.ApplicationContext):
    await ctx.defer(ephemeral = False) # prevent timeout error message if task takes > 3 seconds

    year = str(datetime.now().year)

    channel_id = ctx.channel.id # get current channel id
    channel = bot.get_channel(channel_id) # get current channel 

    users = [] # create list of members
    users_dict = {} # create dict of assignments

    try:
        for member in channel.members:
            if member.bot: # skip bots in the channel
                continue

            users.append(member)
            users_dict[member] = None
        
        if len(users) == 1:
            await ctx.respond("You need at least two channel members!")
            return
        
        # assign first secret santa
        member1 = random.choice(users)
        users.remove(member1)

        member2 = random.choice(users)
        users.remove(member2)

        users_dict[member1] = member2

        curr_member = member1

        # assign the rest
        while(len(users)) > 0:
            new_member = random.choice(users)
            users.remove(new_member)
            users_dict[new_member] = curr_member
            curr_member = new_member

        users_dict[member2] = curr_member

        for santa in users_dict:
            assigned = users_dict[santa]

            # get most recognizable name for each user
            if assigned.nick:
                assigned_name = assigned.nick
            elif assigned.global_name:
                assigned_name = assigned.global_name
            else:
                assigned_name = assigned.name
            
            message = ":sparkles:Secret Santa " + year + ":sparkles: \n You have been assigned: ||" + assigned_name + " (@" + assigned.name + ")||"

            await santa.send(message)

        # response to command user
        await ctx.respond("Secret Santas have been assigned!")

    except AttributeError as e:
        if str(e) == "'NoneType' object has no attribute 'members'": # cannot be run in a DM
            await ctx.respond("**You must run the /assign-secret-santa command in a server channel - no action taken!**")

bot.run(TOKEN) # run the bot with the token