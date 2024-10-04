matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

yeni_matris = []


for i in range(len(matris)):
    for j in matris[i]:
        print(j, end= " ")
    print("")
    
print("-" * 20)

yeni_matris = []

for i in range(len(matris)):
    ic_matris = []
    for j in matris:
        ic_matris.append(j[i])
        
    yeni_matris.append(ic_matris)


for i in range(len(yeni_matris)):
    for j in yeni_matris[i]:
        print(j, end= " ")
    print("")
    

print("-"*20)

yeni_matris = [[j[i] for j in matris] for i in range(len(matris))]
print(yeni_matris)
