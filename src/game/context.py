import logging


class GameContext:
    def __init__(self):
        pass

    def play(self, user, action):
        return action.type.handler_class(user, action.args).result()

