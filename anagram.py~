def anagram(ls): 
	length = len(ls)
	lss = []
	b_list = []
	for i in range(0,length):
		a_list = []
		for j in range(i+1,length):
			if sorted(ls[i]) == sorted(ls[j]):
				if i+1  not in a_list and i+1 not in b_list:
					a_list.append(i+1)
					b_list.append(i+1)
				if j+1 not in b_list:
					a_list.append(j+1)
					b_list.append(j+1)
		if i+1 not in b_list:
			a_list.append(i+1)
		if a_list:
			lss.append(a_list)
	print(lss)
ls=[ "cat", "dog", "god", "tca" ]
anagram(ls)
