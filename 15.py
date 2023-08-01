n = int(input("Enter number "));

count = 0
result = ""
for i in range (n):
    if i != count:
        result += str(i)
    else:
        result = " "
    print(result)

