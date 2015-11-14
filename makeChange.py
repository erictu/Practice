def makeChangeHelper(n, denoms, index):
	if index >= len(denoms) -1:
		return 1
	denomAmount = denoms[index]
	ways = 0 
	i = 0
	while i*denomAmount <= n:
		amountRemaining = n -i*denomAmount
		ways += makeChangeHelper(amountRemaining, denoms, index +1)
		i += 1
	return ways

def makeChange(n):
	denoms = [25, 10, 5, 1]
	return makeChangeHelper(n, denoms, index)