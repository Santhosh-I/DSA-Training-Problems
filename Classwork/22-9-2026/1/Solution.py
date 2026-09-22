s = "!S``PW"

arr = []
length = []
current_len = max_len = 0

for i in s:
    if i not in arr:
        arr.append(i)
        current_len = len(set(arr))
    else:
        arr.append(i)
        arr.remove(arr[0])
        current_len = len(set(arr))
    length.append(current_len)
    print(arr)

print(max(length))
    