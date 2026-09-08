Test_case = int(input())

for i in range(Test_case):
    count = 0
    array = list(map(int,input().split()))
    for i in array:
        if i == 0:
            count += 1
    if count == 0:
        print("No absentees")
    else:
        print(count,"Student absent")
        
        


