# text = input("Enter your code:")
# n = ""
# for i in range(len(text)):
#     if text[i] == "a":
#         print("X")
#     elif text[i] == "b":
#         print("Y")
text = input("Enter the code:")
result = ""
for i in range(len(text)):
    if text[i] == "a":
        result += "X"
    elif text[i] == "b":
        result += "Y"
    else:
        result = text[i]
print(result)