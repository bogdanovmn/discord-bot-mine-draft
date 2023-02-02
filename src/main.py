import os
import logging

import discord
from dotenv import load_dotenv
from game.context import GameContext
from game.user import User
from game.user_input import UserInput

# System config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(name)s]  %(message)s')
load_dotenv()

# Discord config
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Init game context
gameContext = GameContext()


# Discord event handlers


@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    logging.debug(message)

    if message.author == client.user:
        return

    user = User(message.author)
    user_input = UserInput(message.content)
    if user_input.is_command():
        action = user_input.action()
        if action:
            action_outcome = gameContext.play(user, action)
            if action_outcome:
                await message.channel.send(action_outcome)
        else:
            logging.warning(f"User's command is not found: {user_input.command()}")


# Start bot
client.run(os.getenv('DISCORD_BOT_TOKEN'))
