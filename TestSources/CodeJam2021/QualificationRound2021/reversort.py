def f_index(n, lst, i):
	mini = lst[i]
	index = i

	for j in range(i, n):
		if lst[j] < mini:
			index = j
			mini = lst[j]

	return index

def solve(caseno, n, lst):
	cost = 0

	for i in range(n - 1):
		j = f_index(n, lst, i)
		head = lst[:i]
		tail = lst[j + 1:]
		middle = lst[i:j + 1]
		middle.reverse()
		head.extend(middle)
		head.extend(tail)
		lst = head
		cost += j - i + 1

	print(f'Case #{caseno + 1}: {cost}')

if __name__ == '__main__':
	T = int(input())
	
	for i in range(T):
		n = int(input())
		L = input().split(' ')
		L = [int(x) for x in L]
		
		solve(i, n, L)

