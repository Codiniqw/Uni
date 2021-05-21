def suma(num):
    sumT=0
    if(num != 0):
         sumT=num+suma(num-1)
    return sumT

print(suma(3))