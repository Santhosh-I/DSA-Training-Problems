string = input()
chars = list(string)
start = 0
end = len(string) - 1

while start < end:
    chars[start] , chars[end] = chars[end], chars[start]
    start += 1
    end -= 1

print("".join(chars) == string)