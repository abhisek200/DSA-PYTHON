
print("------------ACCESSING ELEMENTS-----------")
shoppingList=['MILK','CHEESE','BUTTER']
print(shoppingList[1]) #returns index value
print('CHEESE' in shoppingList) #boolean return
print(shoppingList[-1])   

print("------------TRAVERSING ELEMENTS-----------")
for i in shoppingList:
    print(i,end=" ")
print("\n")
# also
for i in range(len(shoppingList)):
    print(shoppingList[i]+"+",end="")

print("------------UPDATE/INSERT ELEMENTS-----------")
myList=[1,2,3,4,5,6,7]
print(myList)
myList[2]=33
print(myList)
# insertion
myList.insert(0,69)
print(myList)
newList=[11,12,13,14,15]
myList.extend(newList)
print(myList)

print("------------DELETE ELEMENTS-----------")
m2list=['a','b','c','d']
print(m2list)
print(m2list.pop(2))
print(m2list.pop()) #default:-1

m2list.extend(newList)
print(m2list)
del m2list[3] #element in length
print(m2list)
del m2list[0:2] #0 to n-1
print(m2list)

# remove()
m2list.remove(15)
print(m2list)


print("------------SEARCH ELEMENTS-----------")
val=20
m2list.append(20)
print(m2list)
# 'in' operator
if 14 in m2list:
    print('value {} found at index: '.format(14),m2list.index(20))
else:
    print('value not exists in list')

# other method is looping
def searchList(list,value):
    for i in list:
        if i==value:
            return 'value {} found at index -> '.format(value)+str(list.index(value))
    return 'value does not exists'
print(searchList(m2list,14))

# take input from user store in list and add
mylist=list()
while(True):
    inp=input("Enter Number: ")
    if inp == 'done':break
    value=float(inp)
    mylist.append(value)
    avg=sum(mylist)/len(mylist)
print(avg)
