def wowzaa_calculator(x,y,o,m):
    if isinstance(x,int) and isinstance(y,int):
        pass
    else:
        return "Error"
    
    checkM = [0,1,2,3,4]
    if m not in checkM:
        return "Error"
    
    if o == "+":
        if m == 0:
            return x+y
        elif m == 1:
            return y+x
        elif m == 2:
            return x-y
        elif m == 3:
            return (x+y) + (x-y)
        elif m == 4:
            if (x*y) < (x+y):
                return "wow"
            elif (x*y) > (x+y):
                return "zaa"
            elif (x*y) == (x+y):
                return "wowzaa"

    elif o == "-":
        if m == 0:
            return x-y
        elif m == 1:
            return y-x
        elif m == 2:
            return x+y
        elif m == 3:
            return (x+y) - (x-y)
        elif m == 4:
            if (x*y) < (x+y):
                return "wow"
            elif (x*y) > (x+y):
                return "zaa"
            elif (x*y) == (x+y):
                return "wowzaa"

    elif o == "*":
        if m == 0:
            return x*y
        elif m == 1:
            return y*x
        elif m == 2:
            if y == 0:
                return "Error"
            return x//y
        elif m == 3:
            return (x+y) * (x-y)
        elif m == 4:
            if (x*y) < (x+y):
                return "wow"
            elif (x*y) > (x+y):
                return "zaa"
            elif (x*y) == (x+y):
                return "wowzaa"

    elif o == "/":
        if m == 0:
            if y == 0:
                return "Error"
            return x//y
        elif m == 1:
            if x == 0:
                return "Error"
            return y//x
        elif m == 2:
            return x*y
        elif m == 3:
            if (x-y) == 0:
                return "Error"
            return (x+y) // (x-y)
        elif m == 4:
            if (x*y) < (x+y):
                return "wow"
            elif (x*y) > (x+y):
                return "zaa"
            elif (x*y) == (x+y):
                return "wowzaa"
    
