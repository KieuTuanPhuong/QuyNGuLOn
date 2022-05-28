# n = 5

# n! = 120
# 1+2+...+n = 15
# S3 = 70
# S4 = 225


def giaithua(n):
	if n==1:
		return n
	else:
		return n*giaithua(n-1)

def tong(n):
	s2=0
	for num in range(1, n+1, 1):
		s2+=num
	return(s2)

def sigma1(n):
	s3=0
	for k in range(1, n+1, 1):
		s3+=(k*(k+1))
	return(s3)

def sigma2(n):
	s4=0
	for k in range(1, n+1, 1):
		s4+=(k*k*k)
	return(s4)

def main():
	n = int(input("Nhap so can tim: "))

	print("S1 = ", giaithua(n))
	print("S2 = ", tong(n))
	print("S3 = ", sigma1(n))
	print("S4 = ", sigma2(n))

main()