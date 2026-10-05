def cheack_bill(unit):
    if unit>0 and unit<=100:
        return unit*5
    elif unit>100 and unit<=200:
        return (unit-100)*7+500
    elif unit>200 and unit<=300:
        return (unit-200)*10+1200
    elif unit>300:
        return (unit-300)*15+2200
    else:
        return "invalid input"
    
unit=int(input("enter unit"))
print(cheack_bill(unit))    