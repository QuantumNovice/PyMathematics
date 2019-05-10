from copy import deepcopy
def toArchitectScale(value):
    whole = 0
    sig = len(str(value))
    
    while value > 1:
        print(value)
        value -= 1
        whole += 1
    value = value*10
    value8 = value*0.8
    value16 = value*1.6
    return (whole, round(value8, sig), round(value, sig), round(value16, sig))


x,y,z,t = toArchitectScale(1.33)
print( '{0} {1}/8 {0} {2}/10  {0} {3}/16'.format(x,y,z,t))
