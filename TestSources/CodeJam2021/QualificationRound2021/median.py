if __name__ == '__main__':
	ln = input().split()
	T, N, Q = int(ln[0]), int(ln[1]), int(ln[2])
	for _ in range(T):
		a = []
		print("1 2 3")
		size = 3
		p = int(input())
		if p == 2:
			a.append(1)
			a.append(2)
			a.append(3)
		elif p == 3:
			a.append(1)
			a.append(3)
			a.append(2)
		else:
			a.append(2)
			a.append(1)
			a.append(3)
		for i in range(4, N + 1):
			u = 0
			v = size - 1
			while u < v:
				mid = u + ((v - u) // 2)
				print(f'{a[mid]} {a[mid + 1]} {i}')
				p = int(input())
				if p == a[mid]:
					v = mid
				elif p == a[mid + 1]:
					u = mid + 1
				else:
					a.insert(mid + 1, i)
					size += 1
					break

			if size != i:
				if u == 0:
					a.insert(0, i)
				else:
					a.append(i)
				size += 1
		res = ''
		for x in a:
			res += str(x)
			res += ' '
		print(res)

		if int(input()) == -1:
			break