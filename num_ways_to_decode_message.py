'''
We have a mapping from characters to integers:
a -> 1
b -> 2
c -> 3
...
l -> 12
...
z -> 26

So,

ab -> 12
l  -> 12

if the input is: 12
How many possible messages can be encoded from 12?

For this case: we have 2 ways: ab and l (because 12 -> ab, and 12 -> l)

If your input is 01 -> should return 0, because cannot create any messages from 01

Daily Coding problem

'''

'''
# 3 -> c        => fcn("3") = 1
# '' -> ''       => fcn("") also = 1

#"12345"
case 1:
1 + "2345"    -> 'a' + decode('2345')
case 2
12 + '345'     -> 'l' + decode('345')
So,
num_ways("12345") = num_ways(2345) + num_ways("345")

# "27345"
2 + 7345    -> b + decode(7345)

But no: 27 + 345 because maximum number is 26 <-> z
So, 
num_ways("27345") = num_ways("7345")


# 011
num_ways("011") -> return 0
No character starts with 0 or 01
'''

def helper(data, k):
	'''
	k : last k characters e.g: abcd with k=3 -> bcd
	'''
	if( k == 0 ):
		return 1

	s = len(data) - k
	if( data[s] == "0" ):
		return 0

	result = helper(data, k-1)

	# Check the int(2 first letters) <= 26
	if( (k >= 2) and (int(data[s:s+2]) <= 26) ):
		result += helper(data, k-2)

	return result


def num_ways(data):
	print( len(data) )
	return helper(data, len(data))


res = num_ways("12345")
print(res)



print()
print("================")
'''
if string is "111111"
So,
num_ways("111111") = helper("111111", 6)
= helper("111111", 5) + helper("111111", 4)

           h(6)
		   /  \
         h(5)  h(4)
        /  \
      h(4)  h(3)
      
Need to calculate and store same things over and over again

=> To fix this:
use: Dynamic programming and memoization
'''


def helper_dp(data, k, memo):
	'''
	k : last k characters e.g: abcd with k=3 -> bcd
	'''
	if( k == 0 ):
		return 1

	s = len(data) - k
	if( data[s] == "0" ):
		return 0

	if( memo[k] != None):
		return memo[k]

	result = helper_dp(data, k-1, memo)

	# Check the int(2 first letters) <= 26
	if( (k >= 2) and (int(data[s:s+2]) <= 26) ):
		result += helper_dp(data, k-2, memo)

	memo[k] = result
	return result


def num_ways_dp(data):
	print( len(data) )
	memo = [None]*(len(data) + 1)
	return helper_dp(data, len(data), memo)


res = num_ways_dp("12345")
print(res)