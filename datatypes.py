values = [1, 5, 10,"aruna", 20, 30, 40]

# list is a data type that allows multiple values and can be different data types
# lists are mutable
print(values[0])

print(values[5])

print(values[-1])

print(values[1:4])

values.insert(3, "Naga")  #insert is used to insert at particular position
print(values)

values.append("addanki") #append is used to insert at end
print(values)

values[4] = "ARUNA" #updating
print(values)

del values[0]
print(values)




# Tuple is same as List data type but immutable i,e updation or modification is not possible

val = (1, 2, 3, "aru", 5.6)
print(val)

#val[3]="Aru" #does not support item assignment
#print(val)

#Dictionaries are key and value pair

dic = {"a":1 , 5:"abc", "Hello world":"c"}
print(dic["a"])
print(dic[5])
print(dic["Hello world"])


# creating empty dicts and add values to it
dict = {}
dict['firstname']="Naga Aruna"
dict['lastname']="addanki"
dict['gender']="Female"
dict['age']=23
print(dict)