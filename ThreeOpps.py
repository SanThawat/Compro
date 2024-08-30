def ThreeOpps(a,b,c,ans,op):

    if not isinstance(a,int):
        return "Error"
    if not isinstance(b,int):
        return "Error"
    if not isinstance(c,int):
        return "Error"
    if not isinstance(ans,int):
        return "Error"
    if not isinstance(op,str):
        return "Error"
    if op != "+" and op != "-":
        return "Error"
    
    if op == "+":
        if a + b == ans:
            return str(a) + op + str(b)
        elif a + c == ans:
            return str(a) + op + str(c)
        elif b + c == ans:
            return str(b) + op + str(c)
        elif a + b + c == ans:
            return str(a) + op + str(b) + op + str(c)
        else:
            return "No match"

        

    if op == "-":
        if a - b == ans:
            return str(a) + op + str(b)
        elif a - c == ans:
            return str(a) + op + str(c)
        elif b - c == ans:
            return str(b) + op + str(c)
        elif a - b - c == ans:
            return str(a) + op + str(b) + op + str(c)
        else:
            return "No match"
    
