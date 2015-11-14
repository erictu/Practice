def staircase(n, listin):
	if n == 0:
		return 1
	if n < 0:
		return 0
	if n in listin.keys():
		return listin[n]
	else:
		listin[n] = staircase(n-1, listin) + staircase(n-2, listin) + staircase(n-3, listin)
		return listin[n] 

	# staircase(n-1) + staircase(n-2) + staircase(n-3)

def staircasehelp(n):
	listin = {}
	return staircase(n, listin)
