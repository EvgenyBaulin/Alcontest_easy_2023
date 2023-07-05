n = int(input())
s = input()
cnt1, cnt2, cnt3 = 0, 0, 0
s = s[::-1]

for el in s:
	if el == 'E':
		cnt1 += 1
	if el == 'S':
		cnt2 += cnt1
	if el == "H":
		cnt3 += cnt2

print(cnt3)
