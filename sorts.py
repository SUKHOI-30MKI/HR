import random
import time
import matplotlib.pyplot as plt

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)/2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
	return alist

def quickSort(alist):
	quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
	if first<last:
		splitpoint = partition(alist,first,last)
		quickSortHelper(alist,first,splitpoint-1)
		quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
	pivotvalue = alist[first]
	leftmark = first+1
	rightmark = last
	done = False
	while not done:
		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark = leftmark + 1
		while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark -1
		if rightmark < leftmark:
			done = True
		else:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp
	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp
	return rightmark

def heapify(alist, n, i):
	largest=i  
	l = 2 * i + 1  
	r = 2 * i + 2
	if l<n and alist[i]<alist[l]:
		largest = l
	if r<n and alist[largest]<alist[r]:
		largest = r
	if largest != i:
		alist[i],alist[largest] = alist[largest],alist[i]  
		heapify(alist, n, largest)
def heapSort(alist):
	n = len(alist)
	for i in range(n,-1,-1):
		heapify(alist, n, i)
	for i in range(n-1,0,-1):
		alist[i], alist[0] = alist[0], alist[i]  
		heapify(alist,i,0)

def random1(l):
	alist1=[]
	for i in range(0,l):
		alist.append(random.randint(0,l))
	return alist

list4=[]
list5=[]
list6=[]
list7=[]
alist=[]
				
x=100
while x<=1000:
	alist=random1(x)
	listms=alist[:]
	listqs=alist[:]
	lisths=alist[:]
	g=time.time()
	mergeSort(listms)
	h=time.time()
	mst=h-g
	list4.append(mst)
	i=time.time()
	quickSort(listqs)
	j=time.time()
	qst=h-g
	list5.append(qst)
	k=time.time()
	heapSort(lisths)
	l=time.time()
	hst=l-k
	list6.append(hst)
	list7.append(x)
	x=x+100

plt.plot(list7,list4,'y')
plt.plot(list7,list5,'k')
plt.plot(list7,list6,'g')
plt.xlabel('Number of entries')
plt.ylabel('Time')
plt.show()
