def bonus(salary):
    if salary<=20000:
        bonus=s*10/100
        totalsalary=salary+bonus
        return totalsalary
    elif salary>20000 and salary<=40000:
        bonus=salary*15/100
        totalsalary=salary+bonus
        return totalsalary
    elif salary>40000 and salary<=60000:
        bonus=salary*20/100
        totalsalary=salary+bonus
        return totalsalary
    else:
        bonus=salary*25/100
        totalsalary=salary+bonus
        return totalsalary
    
salary=int(input("enter salary"))
print(bonus(salary))
