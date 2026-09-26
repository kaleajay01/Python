# Lists (mutable)
names=["sanika","sumit","rishika","prachi","sanika"]
marks=[95,98,96,99,98]
print(f"name list: {names}")
print(f"marks list: {marks}")

marks[0]=100
names[2]="naina"
print(f"\nupdated name list: {names}")
print(f"updated marks list: {marks}")

#Tuples (immutable) -means for each operation on tuple it create a copy of tuple then perform oprtaion on tuple

p=(54,66,69,23,75)
q=(99,95,36,12,4.56,23.17)
r=('a','e','i','o','u')
print(f"\n{p}")
print(f"{r}")

# p[0]=96
# print(f"\nupdated: {p}")     -----not acceptable because tuple is immutable
#set
myset={96,92,97,99,95}
print(f"\n{myset}")

# Dictionary
vowels= {'a':1,"e":2,"i":3,"o":4,"u":5}
print(f"\n{vowels}")

