def main():
	sum = sum_three(1,2,3)
	q = div_three(sum)

def sum_three(a1,a2,a3):
	sum = a1+a2+a3
	print sum
	return sum

def div_three(n):
	q = n/3
	print q
	return q

if __name__=="__main__":
	main()

