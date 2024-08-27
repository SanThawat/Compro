def weird_divide(a,b,c) :
    result = a%b
    if result == 0:
        if c == 0:
            return int(a/b)
        elif c == 1:
            first = a/b
            second = a/first
            return second
        elif c == 2:
            first = a/b
            second = b/first
            return second

    elif result > 0 and result <= 5:
        if c == 0:
            return a/b
        elif c == 1:
            return a%b
        elif c == 2:
            return a//b
        
    elif result > 5:
        if c == 0:
            return a//b
        elif c == 1:
            return a/b
        elif c == 2:
            return a%b


print(weird_divide(4,2,0))
print(weird_divide(5,2,1))
print(weird_divide(20,14,1))