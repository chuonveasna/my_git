text = str(input())
count = len(text)
result = 0 
for i in range(count):
    if text[i] == "a":
        result = result + 1 
        if result == 3:
            result = 0
print(result)