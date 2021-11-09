
def main():
    mylist=list()
    n=int(input("Enter how many day's temperature: "))
    for i in range(0,n):
        Value=float(input("Enter day {}'s tempetrature: ".format(i+1)))
        mylist.append(Value)
    avg=average(mylist,n)
    print("Average temperature: %.3f"%avg)
    print(maxFromAvg(mylist,avg))

def average(mylist,total):
    add=0
    for i in mylist:
        add=add+i
    avg=add/total
    return avg

def maxFromAvg(list,avg):
    count=0
    for i in list:
        if(i>avg):
            count+=1
    return "{} value is greater than average.".format(count)

main()
        