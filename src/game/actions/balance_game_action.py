from .abstract_game_action import AbstractGameAction


class BalanceGameAction(AbstractGameAction):
    def result(self):
        return f"Ваш баланс: ..."

