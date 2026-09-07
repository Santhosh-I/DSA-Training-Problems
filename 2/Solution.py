array = list(map(int,input("Enter array:").split()))

print("First Largest :",max(array))
array.remove(max(array))
print("Second Largest :",max(array))