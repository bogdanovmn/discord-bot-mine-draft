from .action import GameActionType, GameAction


class UserInput:
    def __init__(self, text):
        self.text_tokens = text.split()

    def is_command(self):
        return len(self.text_tokens) > 0 and self.text_tokens[0].startswith("!")

    def action(self):
        for actionType in GameActionType:
            if actionType.command == self.command():
                if len(self.text_tokens) != (actionType.args_required + 1):
                    raise Exception(f"У этой команды должно быть {actionType.args_required} аргументов")

                return GameAction(actionType, self.text_tokens[1:])

    def command(self):
        return self.text_tokens[0][1:]





