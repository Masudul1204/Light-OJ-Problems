num1 = int(input())
for i in range(num1):
    num2 = int(input())
    print("Case",i+1,end=": ")
    for x in range(1, num2+1):
        if(num2 % x == 0):
            print(x, end=" ")
    print(end="\n")
    