data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd']

freq = {}

for element in data:
    if element in freq:
        freq[element] = freq[element] + 1
        
    else:
        freq[element] = 1
    
    
print(freq)

from collections import Counter

data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd']

freq = Counter(data)
print(freq)

