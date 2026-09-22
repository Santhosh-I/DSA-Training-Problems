arr = [100, 200, 300, 400]
k = 2
current_sum  = max_sum = sum(arr[:k])

for i in range(k,len(arr)):
    current_sum += arr[i] - arr[i-k]
    max_sum = max(current_sum,max_sum)

print(max_sum)
    
