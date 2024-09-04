def prime(i):
    if i <= 1:
        return False
    for n in range (2,int(i**(0.5))+1):
        if i%n == 0:
            return False
    else:
        return True



def SushiImjang(red,white,gold,black,member):

    if not isinstance(red,int):
        return "Error"
    if not isinstance(white,int):
        return "Error"
    if not isinstance(gold,int):
        return "Error"
    if not isinstance(black,int):
        return "Error"
    if not isinstance(member,bool):
        return "Error"
    if red < 0 or white < 0 or gold < 0 or black < 0:
        return "Error"
    
    r = 40
    w = 60
    g = 80
    b = 120
    dish = red + white + gold + black 
    price = (r*red)+(w*white)+(g*gold)+(b*black)
    fined = 0
    discount = 0
    sc = 0

    if not member:
        if gold == 0 and black == 0 and red + white < 10 :
            if prime(dish):
                white += 1
                dish += 1
                price += w
            else: 
                fined += 60
        if gold == 0 and black == 0:
            if red + white > 10 and red + white <= 15 and red > 0 and white > 0:
                gold += 1
                dish += 1
                price += 0
            elif red + white > 15 and red > 0 and white > 0:
                discount += 100
        if dish > 25:
            discount += 200
        sc += 0.1*price

    if member:
        price = 0.9 * price

        if dish >= 20 and black > 2:
            sc = 0
        elif dish >= 10 and black > 5:
            sc = 0
        elif dish >= 20 and black > 2:
            sc = 0
        elif dish >= 10 and black > 5:
            sc = 0
        else:
            sc = 0.05 * price

        

        
        if gold >= 5:
            red_free = gold//5
            red += red_free
            dish += red_free
            price += 0
        if black >= 3:
            white_free = black//3
            white += white_free
            dish += white_free
            price += 0

    total = price - discount + sc + fined

    return (int(total),dish)

# print(SushiImjang(5,2,0,0,False))
# print(SushiImjang(11,0,0,0,False))
# print(SushiImjang(0,20,0,0,False))
# print(SushiImjang(2,4,10,3,True))
# print(SushiImjang(18,2,5,0,True))


