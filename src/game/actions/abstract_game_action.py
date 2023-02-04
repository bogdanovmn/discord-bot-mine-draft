import logging


class AbstractGameAction:
    def __init__(self, user, args):
        self.args = args
        self.user = user

    def result(self):
        logging.error("Action is not implemented")
        return

