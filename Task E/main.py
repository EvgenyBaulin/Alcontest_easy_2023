n = int(input())
shots = list(map(int, input().split()))
ans = len(shots)
count = 0

for j in range(len(shots) - 1):
	if shots[j] == shots[j + 1]:
		count += 1
	else:
		for i in range(1, count + 1):
			ans += 1
		count = 0

for i in range(1, count + 1):
	ans += 1

print(ans)
