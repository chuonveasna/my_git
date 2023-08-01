text = str(input())
for i in range(len(text)):
    if text[i] == "a":
        print("Dont write with a")
        text = str(input("Try Again"))
print("You are Good!")