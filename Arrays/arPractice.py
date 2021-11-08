from array import *

#1. create an array and traverse
print("Step_1:")
my_array=array('i',[1,2,3,4,5])
for i in my_array:
    print(i)

#2. access individiual elements through indexes
print("Step_2:")
print(my_array[3])

#3. append any value using append() method
print("Step_3:")
my_array.append(6)
print(my_array)

#4. Insert value in an array using insert method
print("Step_4:")
my_array.insert(2,69)
print(my_array)

#5. extend python array using extend method
print("Step_5:")
new_array=array('i',[11,12,13,14,15])
my_array.extend(new_array)
print(my_array)

#6. add items from list to array using fromlist() method
print("Step_6")
tempList=[20,21,22,23,24,25]
my_array.fromlist(tempList)
print(my_array)

#7. remove an array element using remove() method
print("Step_7:")
my_array.remove(69)
print(my_array)

#8. remove last array element using pop() method
print("Step_8:")
my_array.pop()
print(my_array)

#9. fetch any element index in array, using index(element) method
print("Step_9:")
print(my_array.index(22))

#10. reverse a python array using reverse() method
print("Step_10:")
my_array.reverse()
print(my_array)

#11. get array buffer information using buffer_info() method
print("Step_11:")
print(my_array.buffer_info())

#12. check for number of occurrences of an element using count() method
print("Step_12:")
my_array.append(23)
print(my_array)
print(my_array.count(23))

#13. convert array to string using toString() method
print("Step_13:")
str1=""
for i in my_array:
    str1+=str(i)
print(str1)

#14. slice elements from an array
print("Step_14:")
print(my_array[1:4])


