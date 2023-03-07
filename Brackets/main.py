class BracketSentinel:
    def __init__(self, *args, **kwargs):
        super(BracketSentinel, self).__init__(*args, **kwargs)
        self.brackets = {
            "open": ("(", "{", "["),
            "close": {
                "(": ")",
                "[": "]",
                "{": "}"
            }
        }

    def isOpen(self, bracket):
        return bracket in self.brackets["open"]

    def closeCorrectly(self, lastOpenBracket, bracketClose):
        return bracketClose == self.brackets["close"][lastOpenBracket]


    def run(self, brackets):
        stack = []
        for bracket in brackets:
            if self.isOpen(bracket):
                stack.append(bracket)
            elif stack.__len__() > 0 and self.closeCorrectly(stack[-1], bracket):
                del stack[-1]
            else:
                return False
        else:
            return stack.__len__() == 0

    def sentinel(self, brackets, showError = False):
        sintaxSuccessfull = True
        errors = []
        stack = []
        for index, bracket in enumerate(brackets):
            if self.isOpen(bracket):
                stack.append(bracket)
            elif stack.__len__() > 0 and self.closeCorrectly(stack[-1], bracket):
                del stack[-1]
            else:
                sintaxSuccessfull = sintaxSuccessfull and False
                errors.append(index)
        else:
            sintaxSuccessfull = sintaxSuccessfull and stack.__len__() == 0
        

        y = list(" " * brackets.__len__())
        for i in errors:
            y[i] = "^"
        print("\n", *list(brackets), "\n", *y)
        return sintaxSuccessfull