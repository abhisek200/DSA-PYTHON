
import numpy as np
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)
print("--------insert----------")
newtwoDarray=np.insert(twoDArray,1,[[1,2,3,4]],axis=0) #axis=0 ~ rows ; axis=1 ~ column
# insert(array,index position in 2Darray, axis 0/1 dependancy in rows and columns)
print(newtwoDarray)

print("--------append----------")
newtwoDarray2=np.append(twoDArray,[[1,2,3,4]],axis=0)
print(newtwoDarray2)

# access element
print("------------ACCESSING ELEMENT-----------")
def accessElement(array,rowIndex,colIndex):
    if rowIndex>=len(array) and colIndex>=len(array[0]):    #len(array~column and len(array[0])~rows
        print("Incorrect index")
    else:
        print("your respective value is: ",array[rowIndex][colIndex])
accessElement(twoDArray,3,3)


# traversal
print("------------TRAVERSAL-----------")
def traversal(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=" ")
        print(end="  ")
traversal(twoDArray)

# searching
print("\n------------SEARCHING-----------")
def search(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if(array[i][j]==value):
                return "value is located at "+str(i)+" "+str(j)
    return "element is not found"
print(search(twoDArray,17))

# deleteion
print("------------DELETION-----------")
newTDarray=np.delete(twoDArray,1,axis=1) #array, index position, axis-0/1 ~ rows/columns
print(newTDarray)

