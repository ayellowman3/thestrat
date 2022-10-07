
def get_label(candle1,candle2):
    res = 1
    if candle2.get_high()>candle1.get_high():
        res+=1
    if candle2.get_low()<candle1.get_low():
        res+=1
    return res
