def string_perm(str_in):
	perm = []
	if (len(str_in)== 1):
		return str_in
	for i, elem in enumerate(str_in):
		print elem
		print i
		elemlist = string_perm(str_in.replace(elem, "", 1))
		for i in elemlist:
			perm.append(elem + i)
	return perm