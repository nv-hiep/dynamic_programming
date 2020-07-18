# Staircase
# https://www.geeksforgeeks.org/count-ways-reach-nth-stair/

'''
Count ways to reach the n’th stair
There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb either 1 stair or 2 stairs at a time.
Count the number of ways, the person can reach the top.

Examples:
Input: n = 0
Output: 1
There is only one way to from 0 to 0 :)

Input: n = 1
Output: 1
There is only one way to climb 1 stair

Input: n = 2
Output: 3
There are three ways: (1, 1) and (2)

Input: n = 3
Output: 2
There are two ways: (1, 1, 1) and (2, 1), (1,2)

Input: n = 4
Output: 5
(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)


num_ways(n) = num_ways(n-1) + num_ways(n-1)
-> this is a Fibonacci problem
'''
def num_ways(n):
	memo    = [None]*3
	memo[0] = 1
	memo[1] = 1
	for i in range(2, n+1):
		memo[2] = memo[1] + memo[0]
		memo[0] = memo[1]
		memo[1] = memo[2]

	return memo[2]

res = num_ways(11)
print(res)

'''
1 1 2 3 5 8 13 21 34 55 89 144 ...
'''



'''
Now extend this problem:

Staircase has N steps, 
The person can climb Xi stairs at a time with Xi in a set of X, e.g X = {1,2,3}, X={1,3,5}


For example, X = {1, 3, 4}:

Check:
n = 0 -> num_ways = 1
n = 1 -> num_ways = 1

Input: n = 2
Output: 1
There are three ways: (1, 1)

Input: n = 3
Output: 2
There are two ways: (1, 1, 1) and (3)

Input: n = 4
Output: 4
(1, 1, 1, 1), (1, 3), (1,2,1), (1,1,2)

Input: n = 5
Output: 6
(1, 1, 1, 1, 1), (1, 3, 1), (1, 4), (1, 1, 3)
(3, 1, 1),
(4, 1)


Input: n = 6
Output: 5
(1, 1, 1, 1, 1, 1), (1, 1, 3, 1), (1, 3, 1, 1), (1, 4, 1), (1,1,4)
(1,1,1,3)
(3, 1, 1, 1), (3, 3)
(4, 1, 1)

So,

0 -> 1
1 -> 1
2 -> 1 = numways(1) + 0
3 -> 2 = numways(2) + numways(1)
4 -> 4 = numways(3) + numways(1) + numways(0)
5 -> 6 = numways(4) + numways(2) + numways(1)
6 -> 9 = numways(5) + numways(3) + numways(2)

numways(n) = numways(n-1) + numways(n-3) + numways(n-4)
note: X = {1, 3, 4}

'''

def num_ways_X(n):
	'''With X = [1, 3, 4] '''
	X = [1, 3, 4]
	if(n == 0):
		return 1

	total = 0
	for xi in X:
		if (n-xi >= 0):
			total += num_ways_X(n-xi)
	return total


# Result
X = [1, 3, 4]
print('With X = ', X)
for N in range(10):
	res = num_ways_X(N)
	print('num_ways_X({}): {}'.format(N, res) )




'''
For any set of X
'''	
print()
print('===============')

def num_ways_X(n, X):
	if(n == 0):
		return 1

	total = 0
	for xi in X:
		if (n-xi >= 0):
			total += num_ways_X(n-xi, X)
	return total


# Result
X = [1, 3, 5]
print('With X = ', X)
for N in range(10):
	res = num_ways_X(N, X)
	print('num_ways_X({}): {}'.format(N, res) )

print()
print('=========')
X = [1, 3, 6]
print('With X = ', X)
for N in range(10):
	res = num_ways_X(N, X)
	print('num_ways_X({}): {}'.format(N, res) )








'''
With Dynamic Programming
'''	
print()
print('===============')
print('With Dynamic Programming')

def num_ways_X_dp(n, X):
	memo    = [None]*(n+1)
	memo[0] = 1

	for i in range(1,n+1):
		total = 0
		for xi in X:
			if (i-xi >= 0):
				total += num_ways_X_dp(i-xi, X)
		memo[i] = total
	return memo[n]


# Result
X = [1, 3, 4]
print('With X = ', X)
for N in range(10):
	res = num_ways_X_dp(N, X)
	print('num_ways_X_dp({}): {}'.format(N, res) )

print('But here, you have to store all memo values')
print('What we need to store is 4 values: memo[n], memo[n-1], memo[n-3] and memo[n-4]')
print('But that\'s ok, Will think more later.)