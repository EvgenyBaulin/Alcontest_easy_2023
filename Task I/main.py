n = int(input())

boy, girl = [], []
for i in range(n):
	b, g = map(int, input().split())
	boy.append(b)
	girl.append(g)

cnt1 = 0
for i in range(n):
	b, g = boy[i], girl[i]
	if b == 1 and g == 2:
		cnt1 += 1
	if b == 2 and g == 3:
		cnt1 += 1
	if b == 3 and g == 1:
		cnt1 += 1

cnt2 = 0
for i in range(n):
	b, g = boy[i], girl[i]
	if b == 1 and g == 3:
		cnt2 += 1
	if b == 2 and g == 1:
		cnt2 += 1
	if b == 3 and g == 2:
		cnt2 += 1

cnt3 = 0
for i in range(n):
	b, g = boy[i], girl[i]
	if b == 1 and g == 3:
		cnt3 += 1
	if b == 2 and g == 1:
		cnt3 += 1
	if b == 3 and g == 2:
		cnt3 += 1

cnt4 = 0
for i in range(n):
	b, g = boy[i], girl[i]
	if b == 1 and g == 2:
		cnt4 += 1
	if b == 2 and g == 3:
		cnt4 += 1
	if b == 3 and g == 1:
		cnt4 += 1

cnt5 = 0
for i in range(n):
	b, g = boy[i], girl[i]
	if b == 1 and g == 2:
		cnt5 += 1
	if b == 2 and g == 3:
		cnt5 += 1
	if b == 3 and g == 1:
		cnt5 += 1

cnt6 = 0
for i in range(n):
	b, g = boy[i], girl[i]
	if b == 3 and g == 2:
		cnt6 += 1
	if b == 2 and g == 1:
		cnt6 += 1
	if b == 1 and g == 3:
		cnt6 += 1

print(max(cnt1, cnt2, cnt3, cnt4, cnt5, cnt6))

