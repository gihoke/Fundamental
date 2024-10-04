liste = [1,2,3,4]
yeni_liste = []

for i in liste:
    yeni_liste.append(i**i)
    
print(yeni_liste)

print("-"*20)

yeni_liste = [i**i for i in liste]
print(yeni_liste)