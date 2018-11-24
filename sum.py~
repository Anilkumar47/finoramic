def find3Numbers(A, arr_size, B): 
	length = len(A)
	A.sort()
	ls = []
	for i in range (0,length):
			j = i+1
			k = length-1
			while(j<k):
				if(A[i] + A[j] + A[k] <= B):
					ls.append(A[i] + A[j] + A[k])
					j += 1
				else:
					k -= 1
	if ls:
		maximum = max(ls)
	return maximum
A=[ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ]
B = -1
arr_size = len(A) 
print(find3Numbers(A, arr_size, B))

