def ackerman(m,n):
    global x,y
    x.append((m,n))
    y.append(n)
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ackerman(m-1, 1)
    return ackerman(m-1, ackerman(m, n-1))
