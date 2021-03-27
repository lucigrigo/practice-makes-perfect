def operationL(n, c):
	if c < n - 1:
		return []
	l = []
	t = 0
	cc = 1
	for i in range(n - 1, 0, -1):
		cc += 1
		if t + cc + i - 1 >= c:
			r = c - t - i + 1
			l.append(r)
			for k in range(i - 1):
				l.append(1)
			t = c
			break
		t += cc
		l.append(cc)
	if t < c:
		return []
	return l

def operate(l, opeL):
	ln = len(opeL)
	for i in range(ln):
		t = len(l)-(i + 2)
		sp = t + opeL[i]
		l = l[:t] + list(reversed(l[t:sp])) + l[sp:]
	return l

def solve(caseno, n, c):
	l = [i for i in range(1, n + 1)]
	opeL = operationL(n, c)
	l = operate(l, opeL)
	res = " "
	if opeL:
		for x in l:
			res += str(x) + " "
	else:
		res += "IMPOSSIBLE"
	print(f'Case #{caseno + 1}: {res}')

if __name__ == '__main__':
	T = int(input())

	for i in range(T):
		ln = input().split(' ')
		solve(i, int(ln[0]), int(ln[1]))