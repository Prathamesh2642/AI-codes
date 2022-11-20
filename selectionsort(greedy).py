def selectionsort(li):
    size=len(li)
    for i in range(0,size):
        minindex=i
        for j in range(i+1,size):
            if li[j]<li[minindex]:
                minindex=j
                
        (li[i],li[minindex])=(li[minindex],li[i])
    return li

li=[]       
num=int(input("Enter the number of elements in the list "))
for i in range(0,num):
    li.append(int(input(f"Enter the number ")))
# li=[100,1,2,3,78,55,34]
li1=selectionsort(li)
for i in range(0,len(li1)):
    print(li1[i])
