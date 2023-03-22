class BrowserHistory:

    def __init__(self, homepage: str):
        self.br = [homepage]
        self.ans = []
        self.curr = 0

    def visit(self, url: str) -> None:
        self.br = self.br[:self.curr + 1] + [url]
        self.curr = len(self.br) - 1

    def back(self, steps: int) -> str:
        if self.curr - steps < 0:
            self.curr = 0
            return self.br[self.curr]
        else:
            self.curr -= steps
            return self.br[self.curr]

    def forward(self, steps: int) -> str:
        if self.curr + steps >= len(self.br):
            self.curr = len(self.br) - 1
            return self.br[self.curr]
        else:
            self.curr += steps
            return self.br[self.curr]

