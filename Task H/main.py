name = input()
sur = input()
res = input()

full = name + sur
if len(full) == len(res):
	ok = True
	for let in full:
		if let in res:
			res = res.replace(let, "", 1)
		else:
			ok = False
else:
	ok = False

if ok:
	print("YES")
else:
	print("NO")
