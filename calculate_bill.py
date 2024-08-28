def calculate_bill(elec,water,payment):

    elec_result = elec * 8

    if elec > 100:
        elec_result *= 1.06
        elec_result += 200

    elif elec > 50:
        elec_result += 100

    elif elec < 20:
        elec_result -= 50
        if elec_result < 0:
            elec_result = 0
    
    water_result = water * 15

    if water > 20:
        water_result *= 1.02

    elif water < 10:
        water_result -= 50
        if water_result < 0:
            water_result = 0

    elif water < 2:
        water_result = 0

    central_result = 200
    if (water_result + elec_result) >= 1505:
        central_result = 150

    result = elec_result + water_result + central_result

    if (result % 2) == 0 and (result % 5) == 0:
        result *= 0.93

    if water == 0 or elec == 0:
        return "Free"

    if payment == "cash":
        result = result
    elif payment == "online":
        result *= 0.95
    elif payment == "late":
        result *= 1.015

    return f"{result:.2f}"

print(calculate_bill(52,15,"cash"))
print(calculate_bill(141,31,"late"))
print(calculate_bill(22,0,"online"))




