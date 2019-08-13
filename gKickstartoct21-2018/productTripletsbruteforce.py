testcases = int(input())
for i in range(0,testcases):
	n = int(input())
	#n in n numbers that are goin to entered
	arr = [int(x) for x in input().split()]
	#print arr
	finalans=0
	for i in range(0,n):
		for j in range(0,n):
			for k in range(0,n):
				if i!=j and j!=k and i!=k:
					if arr[i]*arr[j]==arr[k] or arr[k]*arr[j]==arr[i] or arr[i]*arr[k]==arr[j]:
						finalans=finalans+1	
	print (finalans/6)