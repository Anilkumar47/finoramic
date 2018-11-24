def redundentBrace(A):
	stack = []
	operaters = {"+", "-", "*", "/", "("}
	for char in A:
		if char in operaters:
			stack.append(char)
		elif char == ")" :
			if stack[-1] == "(":
				return "yes"
			else:
				while stack and stack[-1] != "(":
					stack.pop()
				stack.pop()
	return "no"
A="((a + b)) "
print(redundentBrace(A))
