def oneEdit(w1, w2):
	if (len(w1) == len(w2)):
		return checkReplace(w1, w2)
	elif ((len(w1)-len(w2)) == 1):
		return checkIndel(w1, w2)
	elif ((len(w2)-len(w1)) == 1):
		return checkIndel(w2, w1)
	else:
		return False

def checkReplace(w1, w2):
	edits = 0
	for i in range(0, len(w1)):
		if (w1[i] != w2[i]):
			edits +=1
	if (edits >1):
		return False
	else:
		return True

def checkIndel(w1, w2): #where w1 is longer
	w1idx = 0
	w2idx = 0
	edits = 0
	for i in range(0, len(w2)):
		if (w1[w1idx] != w2[w2idx]):
			w1idx += 1
			edits += 1
		else:
			w1idx += 1
			w2idx += 1
	if (edits > 1):
		return False
	else:
		return True