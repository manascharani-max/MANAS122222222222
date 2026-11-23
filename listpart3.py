L = [4, 5, 10, 11, 12, 15, 22]
print("original list  :", L)

sum = 0

for i in L:
    sum =sum+1


avg = sum/len(L)

print("sum =", sum)
print("average =", avg)

L.sort()


print("smalllest element is:", L[0])


print("largest element is:", L[-1])