# proving binary search has lesser time complexity compared to naive search by importing the time module

import random
import time

def naive(arr,ele):
	for i in range(len(arr)):
		if(arr[i]==ele):
			return i

	return -1
	
def binsearch(l,target,low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1
    midpoint = (low + high) // 2  # 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binsearch(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binsearch(l, target, midpoint+1, high)

#arr=[3,5,7,10,4,9]
#ele=10
#print(naive(arr,ele))
#print(binsearch(arr,0,len(arr)-1,ele))

length = 10000
sorted_list = set()
while len(sorted_list)<length:
	sorted_list.add(random.randint(-3*length, 3*length))
sorted_list = sorted(list(sorted_list))

start=time.time()
for target in sorted_list:
	naive(sorted_list,target)
end=time.time()
print("Naive search time: ", (end - start), "seconds")

start=time.time()
for target in sorted_list:
	binsearch(sorted_list,target,0,10000)
end=time.time()
print("Binary search time: ", (end - start), "seconds")


