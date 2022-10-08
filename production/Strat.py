
def get_label(candle1,candle2):
    res = 1
    if candle2.get_high()>candle1.get_high():
        res+=1
    if candle2.get_low()<candle1.get_low():
        res+=1
    return res

def populate_number(candles_list):
    candles = candles_list.copy()
    c1,c2 = None, None
    while candles:
        c1,c2=c2,candles.pop(0)
        if c1 is not None:
            c2.set_number(get_label(c1,c2))
            print(c2.number,c2.direction)
