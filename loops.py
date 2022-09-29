# if condition

a = 1000
if a>999:
    print("True")
    print("second line")
else:
    print("False")
print("if-else condition is completed")

#for loop
#having fixed iteration number
obj = [1,2,3,4,5]
for i in obj:
    print(i)


obj1 = [2,3,4,5,6]
for i in obj1:
   print(i*5)

#sum of first five natural numbers 1+2+3+4+5=15
#range(i,j) -> i to j-1

summation = 0
for i in range(1,6):
    summation=summation+i
print(summation)

print("****************************************")


for k in range(1,20,3):
    print(k)

print("**********************************")

for m in range(10):
    print(m)


#while loop
#keep on executing until condition is false
#a=5
#while a>3:
#    print(a)


print("**************")

#a=5
#while a>3:
#    print(a)
#    a=a-1
#print("while loop execution is done")



it = 10
while it>1:
    if a==9:
        it = it-1
        continue
    if a==3:
        break
    print(it)

    it = it-1