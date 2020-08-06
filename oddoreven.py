def oddoreven(num):
    if  num%2==0:
        return 1
    else:
        return 0


num=int(input("enter the number"))
if oddoreven(num)!=0:
    print("The number is prime")
else:
    print("The number is odd")


        
