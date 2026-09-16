arr = [2,5,1,8,3,5,1]
# method-1
res = [arr[0]]
for i in range(len(arr)-1):
    max_num = max(arr[i],arr[i+1])
    arr[i+1] = max_num
    res.append(arr[i+1])

print(res)

# method-2
max = arr[0]
for i in arr:
    if i > max:
        max = i
    print(max,end = " ")
