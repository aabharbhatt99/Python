# fibonaaci series code
n = int(input("Number of terms: "))
mylist = [1, 1]
for i in range(n-2):
  mylist.append(mylist[-1]+mylist[-2])
for j in range(len(mylist)-1):
  print(str(mylist[j]) + ", ", end="")
print(str(mylist[-1]))
