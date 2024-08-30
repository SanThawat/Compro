def IceCream(member,age,taste,scoop):

    price = 0.0
    discount = 0.0

    if scoop <= 0 or age <= 0:
        return "Error"
    if member != "Normal" and member != "Gold" and member != "Silver":
        return "Error"
    if taste != "Chocolate" and taste != "Vanilla" and taste != "Special" and taste != "Bubble Gum":
        return "Error"
    
    if taste == "Chocolate" or taste == "Vanilla":
        price = 70 * scoop
    if taste == "Special" or taste == "Bubble Gum":
        price = 79 * scoop

    if member == "Silver":
        if age < 10 and taste == "Bubble Gum" and scoop > 3:
            discount += 0.07 * price
        if age >= 66 and taste == "Special" and scoop > 3:
            discount += 36
        if age >= 66 and taste == "Bubble Gum" and scoop > 3:
            discount += 36

    if member == "Gold":
        if scoop > 5:
            discount += 0.05 * price
        if age <= 28:
            if taste == "Special" and age%4 == 2:
                discount += age//4
            if taste == "Vanilla":
                discount += 22

    if member == "Normal":
        pass

    total = price - discount

    if total < 0:
        total = 0

    pay = 0
    multi = 1

    if total % 2 == 0:
        if total//50 < total/50:
            multi = total//50 + 1
        else:
            multi = total//50
        pay = 50 * multi
    else:
        pay = 100 * (total//100) + 100

    return int(pay - total)



