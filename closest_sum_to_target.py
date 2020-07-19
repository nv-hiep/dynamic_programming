'''
2 arrays and a target

A = [-1, 3, 8, 2, 9, 5]
B = [4, 1, 3, 10, 6, 20]

Find the pairs of numbers from A and B,
SO that their sums are closest to the target.
'''




'''
Method 1:
Brute-force solution:

Loop through all numbers in A and B and find their sum,
and then compare with the target

If len(A) = len(B) = n

We have n^2 pairs, so the time complexity is O(n^2)
'''


A = [-1, 3, 8, 2, 9, 5]
B = [4, 1, 3, 10, 6, 20]

target = 24
result = []
thresh = 3
for ai in A:
	for bi in B:
		if( abs(ai + bi - target) < thresh ):
			result.append( [ai,bi] )

print('result: ', result)
print('with threshold = ', thresh, '; abs(ai+bi - target) < threshold')


'''
With very large lists of A and B, this method is not efficient

Method 2:
Consider A is a set of numbers

Loop through B, for each number in B, find a number in A,
so that their sum = target,
or find a number in A so that their sum = target+/-threshold

e.g: for number 4 in B, check if number 20 is in A
with threshold = 1, check if number 21 or number 19 is in A
'''
print()
print('================')

A = [-1, 3, 8, 2, 9, 5]
B = [4, 1, 3, 10, 6, 20]

target = 24
thresh = 3
range_target = list( range(target - thresh, target + thresh, 1) )
print('Range of targets: ', range_target)


result = []
for bi in B:
	for target_i in range_target:
		if( (target_i-bi) in A ):
			result.append( [target_i-bi, bi] )

print('result: ', result)
print('With threshold = ', thresh, '; abs(ai+bi - target) < threshold')

'''
If len(A) = len(B) = n
so the time complexity is O(x * n)
where x is the len(range_target)
'''




print()
print('================')
print('OK!')


'''
Method 3:

Use a table of sum

e.g:
A = [7, 4, 1, 10]
B = [4, 5, 8, 7]

target = 13

Sort the arrays and arrange on a table:

     4   5   7   8
---|---|---|---|---|
1    5   6   8   9
---|---|---|---|---|
4    8   9   11 *12
---|---|---|---|---|
7    11 *12 *14  15
---|---|---|---|---|
10  *14  15  17  18
---|---|---|---|---|

The numbers with "*" are our result.


You should NOT calculate all the cells, just select a random cell,
for example, the cell (1,1) = 9 (4 + 5).
because 9 < 13, so the cells on its left, and the cells above it are not our answers (cells (0,0)=5, (0,1)=6, (1,0)=8 ), we can ignore them
Similarly, you can find the answers.


Try with bigger arrays A, B, sort the arrays and arrange them on a table...

THe answers' range we should find that it would go cross the table from bottom-left to upper-right.




So, instead of selecting cells randomly, we can select the first cell on top-right,
then check the sum, if the sum < targer, the first line will be ignored

Then go down to the second row, if the sum < target, the second row will be ignored

Then go down to the third row, if the sum > target, the remaining elements of the column will be ignored

Keep searching.... we will see the answer.

Time: O(n logn)
Space: O(n)
'''


# a and b are lists, and target is the target sum.
# The output should be a tuple of two integers, one from each array.
def closest_sum_pair(a, b, target, thresh = 3):
	n = len(a)

	a_sorted = sorted(a)
	b_sorted = sorted(b)

	print('a_sorted: ', a_sorted)
	print('b_sorted: ', b_sorted)
	print('target: ', target)
	print('threshold: ', thresh)
	print()

	# Starting at the upper-right corner
	i = n-1
	j = 0
	result = []
	while ( (i < n) and (j >= 0) and (j < n) ):
		xsum = a_sorted[i] + b_sorted[j]
		print( 'i,j: a[i] + b[j] = sum --- ', i,j,':', a_sorted[i], ' + ', b_sorted[j], ' = ', xsum)

		if( abs(xsum - target) < thresh ):
			result.append( (a_sorted[i], b_sorted[j]) )

		if( xsum < target ):
			j += 1
		else:
			i -= 1

	return result


a      = [-1, 3, 8, 2,  9, 5,  3,  6, 13]
b      = [4,  1, 2, 10, 5, 20, 15, 7,  9 ]
target = 24

res = closest_sum_pair(a, b, target)
print()
print('Result: ', res)