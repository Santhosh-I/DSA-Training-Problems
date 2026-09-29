# arr = "abbaca"
# final = [arr[0]]

# for i in range(len(arr)-1):
#     if arr[i] != arr[i+1]:
#         final.append(arr[i+1])
#     else:
#         final.pop()

# print(final)


# arr = [int(x) for x in input().split()]
# print(arr)

n = int(input())
arr = []

for i in range(n):
    arr.append(input())
print(arr)