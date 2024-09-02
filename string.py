string = "I love India"

l = len(string)
i = 0

while i < l:
    print(string[i], end=" ")
    i += 1
print()
# unary minus

i = 1
l = len(string)
while i <= l:
    print(string[-i], end=" ")
    i += 1
