'''
The purpose of dynamic programming is to not calculate the same thing twice.
'''

def Fibonacci(n):
	if ( (n ==0) or (n==1) ):
		return n

	return Fibonacci(n-1) + Fibonacci(n-2)



n   = 10
res = Fibonacci(n)
print('Fibonacci ({}) = {}'.format(n, res))


'''
For Fibonacci(4), let's take a look:

                      4
                     /  \

                   3      2
                  / \     / \
                1    2    0   1
                     / \
                    1   0

We calculate F(2) twice. On bigger inputs (such as F(10)) the repetition builds up.
The purpose of dynamic programming is to not calculate the same thing twice.

Instead of calculating F(2) twice, we store the solution somewhere and only calculate it once.

We'll store the solution in an array. F[2] = 1.

Below is some Python code to calculate the Fibonacci sequence using Dynamic Programming.
'''

def Fibonacci_dp(n, memo):
	memo[0] = 0
	memo[1] = 1

	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]

	print(memo)
	return memo[n]



n    = 10
memo = [None] * (n+1)
res  = Fibonacci_dp(n, memo)
print('Fibonacci ({}) = {}'.format(n, res))