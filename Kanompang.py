def Kanompang(a,b,c,d,e):
    torn = 0
    torns = 0

    if a == 1:
        torn += 1
    else:
        return False
    
    if b == 2:
        torn -= 1
        torns += 2
    elif b == 1:
        torn += 1
    else:
        return False
    
    if c == 2:
        if torn > 0:
            torn -= 1
            torns += 2
        else:
            return False
    elif c == 1:
        torn += 1
    else:
        return False
    
    if d == 2:
        if torn > 0:
            torn -= 1
            torns += 2
        else:
            return False
    elif d == 1:
        torn += 1
    else:
        return False
    
    if e == 2:
        if torn > 0:
            torn -= 1
            torns += 2
            return True
        else:
            return False
    elif e == 1:
        torn += 1
        return True
    else:
        if torn + torns >= 4:
            return True
        else:
            return False
    
    
    
