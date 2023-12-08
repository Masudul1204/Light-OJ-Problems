
rows = int(input("Enter a number:: "))

for i in range(1,rows):
    for j in range(rows-i):
        print(i, end=' ')
    print('')
