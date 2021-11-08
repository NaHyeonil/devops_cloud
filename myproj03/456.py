for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


result = 0
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        result += i

print(result)
