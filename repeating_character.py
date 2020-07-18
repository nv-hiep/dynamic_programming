'''
Find the repeating characters in a string

input: ABCA -> output: A
input: BCABA -> output: [ A, B ]
input: ABC -> output: None
'''

'''
1. Naive solution:
Loop over the whole string and compare each pair of characters


2. Another solution
Loop the string from left to right, and count the frequency of each character
e.g:
DBCABCA

dict: D -> 1, B -> 2, C -> 2, A -> 2
'''

def count_char(string):
	counts = {}
	ret    = []
	for char in string:
		if char in counts:
			# return char
			counts[char] += 1
			ret.append(char)
		else:
			counts[char] = 1

	return counts, ret


# Example:
s = "ABCDECBDA"
print('String: ', s)
res, chars = count_char(s)
print('The characters with frequencies are: ')
print(res)

print('The recurring characters are: ')
print(chars)


print()
print("================")
'''
For finding the FIRST recurring Character
'''
def first_recurring_char(string):
	counts = {}
	for char in string:
		if char in counts:
			return char
		counts[char] = 1

	return None


# Example:
s = "ABCDECBDA"
print('String: ', s)
res = first_recurring_char(s)

print('The first recurring character is: ')
print(res)