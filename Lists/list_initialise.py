
print("------User input in lists---------")
n=input("Enter total numbers\n")
print()
user_list=n.split( ) 
#split will convert string to list upon given space, eg: 10 12 13 14 15 = ['10','12','13','14','15'] space separates the string to list
print("list: ", user_list) #prints the list in string format
# convert the string in the list to integers
for i in range(0,len(user_list)):
    # convert each item to int type
    user_list[i]=int(user_list[i])
print("list final: ",user_list) #prints the list in integers, as stored.