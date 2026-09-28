# class Solution:
#     def areAnagrams(self, s1, s2):
#        # code here
       
#         freq1 = {}
#         freq2 = {}
#         for i in s1:
#            freq1[i] = freq1.get(i,0) + 1
           
#         for i in s2:
#             freq2[i] = freq2.get(i,0) + 1
            
#         return freq1 == freq2


arr = [0]*26
for i in arr:
    arr[5] = 1
    
print(arr)