def Flowers(type,number,grade,season,bouquet) :
        
    price = 0
    Summer = ["Marigolds","Zinnias"]
    Rainy = ["Roses","Hydrangeas"]
    Winter = ["Lisianthus","Sunflowers"]

    flower = Summer + Rainy + Winter

    if type in flower:
        if season != "Summer" and season != "Rainy" and season != "Winter":
            return "Error"
        
        if isinstance(number,int) == False:
            return "Error"
        else:
            if number < 0:
                return "Error"
        
        if type == "Marigolds":
            price = 20.0
            if season != "Summer":
                price *= 2
        elif type == "Zinnias":
            price = 35.0
            if season != "Summer":
                price *= 2
        elif type == "Roses":
            price = 70.0
            if season != "Rainy":
                price *= 2
        elif type == "Hydrangeas":
            price = 90.0
            if season != "Rainy":
                price *= 2
        elif type == "Lisianthus":
            price = 80.0
            if season != "Winter":
                price *= 2
        elif type == "Sunflowers":
            price = 75.0
            if season != "Winter":
                price *= 2

        if grade == "A":
            price *= 1.3
        elif grade == "B":
            price *= 1.0
        elif grade == "C":
            price *= 0.7
        else:
            return "Error"

        price *= number

        if bouquet == "Full":
            price += 200.0
        elif bouquet == "Base":
            price += 100.0
        elif bouquet == "Null":
            price += 0.0
        else:
            return "Error"
    
        return price
    else:
        return "Error"



        
    
print(Flowers("Marigolds",10,"A","Summer","Full"))
print(Flowers("Zinnias",5,"B","Winter","Base"))
print(Flowers("Roses",8,"C","Rainy","Null"))
print(Flowers("Lisianthus",4,"B","Winter","Null"))
print(Flowers("Marigolds",10,"A","Authum","Full"))
print(Flowers("Daisies",5,"B","Winter","Base"))
print(Flowers("Roses",3,"D","Rainy","Null"))
print(Flowers("Zinnias",7,"A","Summer","Advance"))
print(Flowers("Sunflowers","five","B","Winter","Base"))
print(Flowers("Hydrangeas",-3,"A","Rainy","Full"))

# print(Flowers("Lisianthus",5,"A","Summer","Full"))
