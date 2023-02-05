import logging

from game.action import GameAction
from game.model.player import Player


class GameContext:
    def __init__(self):
        pass

    def play(self, player: Player, action: GameAction):
        logging.info(f"{player.name} is playing {action.type}")
        return action.type.handler_class(player, action.args).result()

