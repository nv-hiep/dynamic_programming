'''
Find all subsets of a given set
[1,2]
-> [], [1], [2], [1,2] -> 4 subsets = 2^2

[1,2,3]
[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] -> 8 = 2^3


        -[1]
   [1]-|
    |   -[1,2]
[]- 
    |  - [2]
   []-|
       - []
So, set of N elements has 2^N subsets.

How to find all of them?
And just print them
'''

def get_subsets(a):
	# Create a Null subset with len = len(a)
	# [None, NOne, None] = []
	# [None, None, 3]    = [3]
	# [None, 2, 3]       = [2,3]
	subset = [None]*len(a)
	helper(a, subset, 0)

def helper(a, subset, i):
	if( i == len(a)):
		print(subset)
	else:
		subset[i] = None           # Without a[i] in the subset
		helper(a, subset, i+1)
		subset[i] = a[i]           # With a[i] in the subset
		helper(a, subset, i+1)


if __name__ == '__main__':
	a = [1,2,3]
	print('Result - {} subsets are: '.format(2**len(a)))
	get_subsets(a)