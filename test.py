def my_sum(a, b):
	if a == None or b == None:
		raise ValueError("Input values can't be null")
	return 2*a + 3*b

def my_mult(a, b):
	if a == None or b == None:
		raise ValueError("Input values can't be null")
	return a*b*2

print(my_sum(5,6))
print(my_sum(4,2))
