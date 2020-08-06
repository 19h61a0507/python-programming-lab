num=int(input("enter the number"))
flag=0
for i in range(1,num+1):
    if num%i==0:
        flag=flag+1
if flag==2:
    print(num ,"is a prime number")
else:
    print(num,"isn't a prime number")
