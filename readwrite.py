file = open('test.txt')
#read all the contents of the file
#print(file.read())
#print(file.read(2))
#print(file.read(10))

#print single line at a time
#print(file.readline())
#print(file.readline())
#file.close()

#print line by line using while loop
#line = file.readline()
#while line!="":
#    print(line)
#    line=file.readline()

#for getting output in the form of list
#values=[apple,ball,cat,dog,elephant,fox]
for line in file.readlines():
    print(line)
