def Scorewowwow(x,y,z):

    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        pass
    else:
        return "Error"
    if x < 0 or y < 0 or z < 0:
        return "Error"

    score = 100

    if x > 5:
        score -= 1 * (x-5)
        x = 5
    if x <= 5:
        score -= 5 * (x-0)

    if y > 8:
        score -= 2 * (y-8)
        y = 8
    if y <= 8:
        score -= 3 * (y-0)

    if score < 0:
        score = 0
        
    if score == z:
        return "Excellent"
    if z - 8 == score:
        return f"A1,{score}"
    elif z - 5 == score:
        return f"A2,{score}"
    elif z - 10 == score:
        return f"B1,{score}"
    elif z - 1 == score:
        return f"B2,{score}"
    else:
        return "Wrong number"
    

# print(Scorewowwow(22,25,2))
# print(Scorewowwow(7,2,67))
# print(Scorewowwow(1,3,94))
