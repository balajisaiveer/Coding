testcases = int(input())
ans1=[]
ans=[]
for testcasenumber in range(0,testcases):

	n = int(input())
	#n in n numbers that are goin to entered
	arr = [int(x) for x in input().split()]
	#print arr
	#################################################################################################3
	###################BRUTE FROCE N^3
	finalans=0
	for i in range(0,n):
		for j in range(0,n):
			for k in range(0,n):
				if i!=j and j!=k and i!=k:
					if arr[i]*arr[j]==arr[k] or arr[k]*arr[j]==arr[i] or arr[i]*arr[k]==arr[j]:
						finalans=finalans+1	
	
	# print "answer from methoed 1"
	ans.append(finalans/6)
	
	# print finalans/6

	##################################################################################################3
	######################BETTER METHOD N^2 but N space
	finalans1=0
	
	maxvalue = max(arr)
	initialzeroslist = [0]*maxvalue
	for i in arr:
		initialzeroslist[i-1]=initialzeroslist[i-1]+1
	# print initialzeroslist
	for i in range(0,n):
		secondzeroslist=[]
		
		################################3
		#CREATING ANOTHER LIST FOR justifying the exsistance of 1 while multiplication
		for m in initialzeroslist:
			secondzeroslist.append(m)
		# print secondzeroslist
		#Now changing the secondzeroslist does not effect intialzeros list
		for j in range(i,n):
			if i!=j:
				if arr[i]*arr[j]<=maxvalue:
					# print "-------------------------"
					# print arr[i],arr[j]
					# print "#########################"
					if secondzeroslist[(arr[i]*arr[j])-1]!=0:
						if arr[i]!=1 and arr[j]!=1 :
							# print arr[i],arr[j]
							finalans1 =finalans1+initialzeroslist[(arr[i]*arr[j])-1]
							#print finalans1
						if arr[i]==1 and arr[j]!=1:
							# print arr[i],arr[j]
							finalans1 = finalans1+secondzeroslist[(arr[i]*arr[j])-1]-1
							# print finalans1
							if secondzeroslist[(arr[i]*arr[j])-1] >1:
								secondzeroslist[(arr[i]*arr[j])-1]=secondzeroslist[(arr[i]*arr[j])-1]-1
						if arr[j]==1 and arr[i]!=1:
							# print arr[i],arr[j]
							finalans1 = finalans1+secondzeroslist[(arr[i]*arr[j])-1]-1
							# print finalans1
							if secondzeroslist[(arr[i]*arr[j])-1] >1:
								secondzeroslist[(arr[i]*arr[j])-1]=secondzeroslist[(arr[i]*arr[j])-1]-1

						###### IN ABOVE CASE WE DID NOT INCLUE ALL ONES SCENARIO						
	increaseduetoones=0
	if initialzeroslist[0]>=3:
		increaseduetoones = (initialzeroslist[0]*(initialzeroslist[0]-1)*(initialzeroslist[0]-2))/6
	finalans1 = finalans1+increaseduetoones
	# print "answer from methoed 2"
	# print finalans1
	ans1.append(finalans1)
##################################
#PRINTING ALL THE ANSWERS AT THE LAST
for t in range(0,testcases):
	# print t
	print ('Case #%d: %d'%(t+1,ans1[t]))
	