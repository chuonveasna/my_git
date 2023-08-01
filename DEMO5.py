text = str(input())
length = len(text)
count = 0
result = " "
for i in range(length):
    if text[i] == "a":
        count += 1
        if  count %2 == 0:
            result = "Morning"
        else:
            result = "Good night"
print(result)