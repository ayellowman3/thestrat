class Candle:
    def __init__(self, symbol, open, high, low, close):
        self.symbol = symbol
        self.open = open
        self.high = high
        self.low = low
        self.close = close

    def get_open(self):
        return self.open

    def get_high(self):
        return self.high

    def get_low(self):
        return self.low

    def get_close(self):
        return self.close
