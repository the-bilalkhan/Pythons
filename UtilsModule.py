def Maxima(Values):
        Max = Values[0]
        for Value in Values:
            if Value > Max:
                Max = Value
        return Max


def Minima(Values):
    Min = Values[0]
    for Value in Values:
        if Value < Min:
            Min = Value
    return Min
