def GrabSusu(a,b,x,y):
    distance = ((((y-b)**2)+((x-a)**2))**(0.5))
    price = distance + 10
    add_price = 0
    if distance > 20:
        add_price += (price * 0.7) * (distance - 20)
        distance = 20

    if distance > 15:
        add_price += (price * 0.5) * (distance - 15)
        distance = 10
        
    if distance > 10:
        add_price += (price * 0.3) * (distance - 10)
        distance = 10
        
    if distance > 5:
        add_price += (price * 0.1) * (distance - 5)
        distance = 5
        
    if distance > 0 and distance < 5:
        add_price += 0
        
    if distance == 0:
        return "Error"
    
    result = price + add_price
    return int(result)
    
print(GrabSusu(1,2,3,4))
print(GrabSusu(0,0,10,10))
print(GrabSusu(2,3,8,11))