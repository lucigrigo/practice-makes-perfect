def solve(caseno, S, X, Y):
	cost = 0

	# backtracking

	print(f'Case #{caseno + 1}: {cost}')

if __name__ == '__main__':
	T = int(input())

	for i in range(T):
		line = input().split(' ')
		X, Y, S = line[0], line[1], line[2]
		solve(i, S, X, Y)
