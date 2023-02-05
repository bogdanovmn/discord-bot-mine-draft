from game.actions.abstract_game_action import AbstractGameAction
from game.model.player import Attribute


class BalanceGameAction(AbstractGameAction):
    def result(self):
        self.player.attrs()
        return f"Ваш баланс: {self.player.attr(Attribute.GOLD)} gold"

