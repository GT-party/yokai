a,b=int(input()),float(input())
if a/(b*b)>=18.5 and a/(b*b)<25:
    print("Оптимальная масса")
elif a/(b*b)<18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")