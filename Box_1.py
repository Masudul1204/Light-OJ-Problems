num1 = int(input())
for i in range(num1):
    num2 = int(input())
    for x in range(num2):
        print('*',end="")
        for j in range(num2-1):
            print('*',end="")
        print(end="\n")
    print(end="\n")