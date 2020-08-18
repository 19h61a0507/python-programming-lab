count,count1=0,0
for i in range(1,101):
    result=i*i
    if result%10==2:
        count=count+1        
    elif result%10==9:
        count1=count1+1
    else:
        print("NOTHING")
print("Number of didgits that end with 2 are ",count)
print("Number of didgits that end with 9 are ",count1)        
    
