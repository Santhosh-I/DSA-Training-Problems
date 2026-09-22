nums = [4,4,4]
k = 3
sums = []

for i in range(len(nums) - k + 1):
    if len(nums[i:k+i]) == len(set(nums[i:k+i])):
        sums.append(sum(nums[i:k+i]))
    else:
        sums.clear()
        sums.append(0)


print(max(sums))