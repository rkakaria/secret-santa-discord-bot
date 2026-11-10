# Secret Santa Discord Bot
This repository contains code for a simple Discord bot that assigns each member of the channel in which it is run another channel member as a Secret Santa giftee. 

## How it works
For a channel with _n_ non-bot members, this bot will assign each member a different member as their Secret Santa giftee such that there is a cycle of length _n_ between members. For example, for a channel with members A, B, C, D, and E, running the bot could result in the assignations B → E → A → D → C → B, where member B is assigned member E, member E is assigned member A, and so on. No cycles of length < _n_ are ever generated.  
For each assignment, the code randomly selects from the pool of non-assigned members, so running the bot multiple times will result in different assignments. Additionally, every non-bot member of the channel is assumed to be participating, so the bot should only be run in a channel in which all channel members wish to be included in Secret Santa.

## Dependencies ##
- [pycord](https://pycord.dev/)
- built-in Python libraries

## How to run
1. Run ``git clone https://github.com/rkakaria/secret-santa-discord-bot.git``
2. Create a ``.env`` file in the secret-santa-discord-bot directory
3. Create a [new Discord app](https://docs.discord.com/developers/quick-start/getting-started#step-1-creating-an-app). 
4. Replace the placeholder text, including the opening and closing brackets, in the ``.env`` file with the new Discord app's application ID and public key, and the bot's token.
5. Enable ``Server Members Intent`` in the bot settings. 
6. Install the bot to your desired Discord server and channel.
7. Run ``python main.py`` in your bot directory
8. Wait for the ``<bot_name> is ready!`` terminal output
9. In your desired channel, type and enter ``/assign-secret-santa``

The bot will return a confirmation message and every non-bot member of the channel will receive a direct message from the bot containing the name and unique username of their assigned giftee behind spoiler text.