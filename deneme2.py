numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
        
print(evens)

even = [number for number in numbers if number % 2 == 0]
print(even)

m = [[0] * 3 for x in range(3)]

for row in range(3):
    for col in range(3):
        if row == col:
            m[row][col] = 1
            
print(m)
        