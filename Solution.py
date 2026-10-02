arr = [1, 2, 4, 5]

n = 5

expected = n * (n + 1) // 2

actual = 0

for x in arr:
    actual += x

print(expected - actual)