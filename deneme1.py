numbers = (1, 2, 3, 4, 5)

sq = [number ** 2 for number in numbers]
print(sq)

numbers2 = (6, 7, 8, 9, 10)
sq2 = []

for nm in numbers2:
   sq2.append(nm**2)
    
print(sq2)

kareler = [x **2 for x in range(1,11)]
print(kareler)