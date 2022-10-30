from itertools import permutations
import numpy as np

dizi1 = []
dizi2 = []

uzunluk = int(input("1.grafın düğüm sayısını giriniz: "))

uzunluk2 = int(input("\n2.grafın düğüm sayısını giriniz: "))

if(uzunluk != uzunluk2):
    print("İki graf izomorfik değildir.")
    quit()

print("\n1.grafın komşuluk matrisini giriniz:")
for i in range(uzunluk):
    dizi1.append([])
    for j in range(uzunluk):
        dizi1[i].append(int(input()))
        
print("\n2.grafın komşuluk matrisini giriniz:")
for i in range(uzunluk):
    dizi2.append([])
    for j in range(uzunluk):
        dizi2[i].append(int(input()))
        
if(np.sum(np.sum(dizi1)) != np.sum(np.sum(dizi2))):
    print("İki graf izomorfik değildir.")
    quit()

temp = []

for i in range(uzunluk):
    temp.append(i)
    
perm = list(permutations(temp))

for item in perm:
    flag = True
    for i in range(uzunluk):
        if(flag):
            for j in range(uzunluk):
                if(flag):
                    if(dizi1[i][j] != dizi2[item[i]][item[j]]):
                        flag = False
                else:
                    break
        else:
            break
        
    if(flag):
        break
    
if(flag):
    print("\nBu iki graph izomorfiktir.")
else:
    print("\nBu iki graph izomorfik değildir.")
