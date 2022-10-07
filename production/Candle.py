class Candle:
    def __init__(self, symbol, open, high, low, close):
        self.symbol = symbol
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.number = 1
        self.direction = None

    def get_open(self):
        return self.open

    def get_high(self):
        return self.high

    def get_low(self):
        return self.low

    def get_close(self):
        return self.close

    def set_number(self, number):
        self.number=number
        if self.number == 2:
            self.set_direction()

    def set_direction(self):
        if self.close>self.open:
            self.direction = "U"
        else:
            self.direction = "D"
