from .abstract_game_action import AbstractGameAction


class MineResearchGameAction(AbstractGameAction):
    def result(self):
        return f"Вы спустились в шахту"

