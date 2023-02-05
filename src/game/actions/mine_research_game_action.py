from game.actions.abstract_game_action import AbstractGameAction
from game.model.player import Attribute


class MineResearchGameAction(AbstractGameAction):
    def result(self):
        gold = self.player.attr(Attribute.GOLD)
        increment = 1
        self.player.set_attr(Attribute.GOLD, gold + increment)
        return f"Вы спустились в шахту и нашли там золото: {increment} "

