def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return  fact



n1=int(input("Number    "))
s=fact(n1)
print(s)
