sum = 0
for i in range(1,6):
    sum = sum+ i
print(sum)


it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1