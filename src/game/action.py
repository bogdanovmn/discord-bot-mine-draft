import enum

from game.actions.mine_research_game_action import MineResearchGameAction
from game.actions.balance_game_action import BalanceGameAction


class GameActionType(enum.Enum):
    mine_research = ('шахта', 0, MineResearchGameAction)
    balance = ('баланс', 0, BalanceGameAction)

    def __init__(self, command, args_required, handler_class):
        self.command = command
        self.args_required = args_required
        self.handler_class = handler_class


class GameAction:
    def __init__(self, action_type, args):
        self.args = args
        self.type = action_type


