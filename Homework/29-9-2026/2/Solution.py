s = "bacd"
s = list(s)
k = 2

for i in range(len(s)):
    s[2*k], s[2*k + 1] = s[2*k + 1], s[2*k]

print(s)