if __name__ == '__main__':
	T = int(input())

	for j in range(T):
		ln = input().split()
		x, y, s = int(ln[0]), int(ln[1]), ln[2]
		ans = 0
		n = len(s)
		prev = 'I'
		for i in range(n):
			if s[i] == 'C':
				if prev == 'J':
					ans += y
				prev = 'C'
			elif s[i] == 'J':
				if prev == 'C':
					ans += x
				prev = 'J'
		print(f'Case #{j + 1}: {ans}')