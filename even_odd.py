def cheack_pnoddeven(n):
    if n>0 and n%2==0:
        return "POSSTIVE EVEN"
    elif n>0 and n%2!=0:
        return "POSITIVE ODD"
    elif n<0 and n%2==0:
        return "NEGATIVE EVEN"
    elif n<0 and n%2!=0:
        return "NEGATIVE ODD"
    else:
        return "zero"
    
n=int(input("enter number"))
print(cheack_pnoddeven(n))