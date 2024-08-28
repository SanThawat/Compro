def WeirdDivide(a,b,c) :
    result = a%b
    if b == 0:
        return "Error"
    if result == 0:
        if c == 0:
            return int(a/b)
        elif c == 1:
            first = a/b
            second = first/a
            return second
        elif c == 2:
            first = a/b
            second = first/b
            return second

    if result > 0 and result <= 5:
        if c == 0:
            return a/b
        elif c == 1:
            return a%b
        elif c == 2:
            return int(a/b)
        
    if result > 5:
        if c == 0:
            return int(a/b)
        elif c == 1:
            return a/b
        elif c == 2:
            return a%b


# print(WeirdDivide(4,2,0))
# print(WeirdDivide(5,2,1))
# print(WeirdDivide(20,14,1))