class MineResearchGameAction:
    def __init__(self, user, args):
        self.args = args
        self.user = user

    def result(self):
        return f"Вы спустились в шахту"

