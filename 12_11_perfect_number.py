start=int(input(f'Number From: : '))
end=int(input(f'Number To: '))

for num in range(start,end):
	sum=0
	for j in range (1,num):
		if num%j==0:
			sum=sum+j

	if sum==num:
		print(f'The number {num} is a perfect number')
