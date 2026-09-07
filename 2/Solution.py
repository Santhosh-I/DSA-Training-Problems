array = list(map(int,input("Enter array:").split()))

print("First Largest :",max(array),"Index :",array.index(max(array))+1)
array.remove(max(array))
print("Second Largest :",max(array),"Index :",array.index(max(array))+1)