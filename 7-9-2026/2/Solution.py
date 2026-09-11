array = list(map(int,input("Enter array:").split()))

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i] < array[j]:
            max = j
            print(array[j])

print(array[j])