import enum

from .mine_research_game_action import MineResearchGameAction


class GameActionType(enum.Enum):
    mine_research = ('шахта', 0, MineResearchGameAction)

    def __init__(self, command, args_required, handler_class):
        self.command = command
        self.args_required = args_required
        self.handler_class = handler_class


class GameAction:
    def __init__(self, type, args):
        self.args = args
        self.type = type


