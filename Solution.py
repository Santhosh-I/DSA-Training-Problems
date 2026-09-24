arr = [100,200,150,300,250]
sum = 0
sum_arr = []

for i in range(len(arr)):
    sum += arr[i]
    sum_arr.append(sum)

print(sum_arr)