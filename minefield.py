n = int(input())

if n == 1:
    c1 = int(input())
    print(c1)

elif n == 2:
    c1 = int(input())
    c2 = int(input())
    print(c1 + c2)
    print(c1 + c2)

else:
    c1 = int(input())
    c2 = int(input())
    
    print(c1 + c2)
    
    contador = 3
    while contador <= n:
        c3 = int(input())
        print(c1 + c2 + c3)
        
        c1 = c2
        c2 = c3
        contador += 1
        
    print(c1 + c2)
