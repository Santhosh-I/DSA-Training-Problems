from collections import Counter

strs = ["eat","tea","tan","ate","nat","bat"]

freq = []

for i in strs:
    freq.append(Counter(i))

print(freq)