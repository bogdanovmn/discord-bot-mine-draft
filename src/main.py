import os
import logging

import discord
from dotenv import load_dotenv
from game.context import GameContext
from game.model.player import PlayerRepository
from game.player_input import PlayerInput

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

    player_input = PlayerInput(message.content)
    if player_input.is_command():
        action = player_input.action()
        if action:
            player = PlayerRepository.find_or_create(message.author.id, message.author.display_name)
            action_outcome = gameContext.play(player, action)
            if action_outcome:
                await message.channel.send(action_outcome)
        else:
            logging.warning(f"Player's command is not found: {player_input.command()}")


# Start bot
client.run(os.getenv('DISCORD_BOT_TOKEN'))
