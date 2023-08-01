number= int(input())
for i in range(number,0,-1):
    for z in range (1, i+1):
        print(z, end=" ")
    print("\r")