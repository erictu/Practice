def numWaysChange(n):
	if n <= 0:
		return 0
	# if 5< n < 10:
	# 	return numWaysChange(n-5) + numWaysChange(n-6)
	if n == 1:
		return 1
	if n == 5:
		return 2
	if n == 10:
		return 2
	return numWaysChange(n-1) + numWaysChange(n-5) + numWaysChange(n-10) + numWaysChange(n-25)