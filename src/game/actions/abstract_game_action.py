import logging


class AbstractGameAction:
    def __init__(self, player, args):
        self.args = args
        self.player = player

    def result(self):
        logging.error("Action is not implemented")
        return

