'''
Find the intersection between arrays

An example:
2 or more arrays, find the common elements of the arrays.

A = [2,6,9,11,13,17]
B = [3,6,7,10,13,18]
C = [4,5,6,9,11,13]

-> Output = [6,13]
'''

A = [2,6,9,11,13,17, 20, 26, 22]
B = [3,6, 22, 7,10,18,13, 16, 23]
C = [4,22, 5,6,9,11,13, 30, 27]

A = sorted(A)
B = sorted(B)
C = sorted(C)

print('Sorted_A: ', A)
print('Sorted_B: ', B)
print('Sorted_C: ', C)

# print()
# print('===============')
# print('For 2 Arrays: ')

def stop_cond(i, j, NA, NB):
	return (i >= NA) or (j>= NB)

def find_intersection(A, B):
	NA = len(A)
	NB = len(B)

	i = 0
	j = 0

	ret = []
	while not stop_cond(i, j, NA, NB):
		if( A[i] == B[j] ):
			# print(i,j,A[i],B[j])
			ret.append(A[i])
			i += 1
			j += 1
		elif( A[i] < B[j] ):
			i += 1
		else:
			j += 1
	return ret




def stop_cond3(i, j, k, NA, NB, NC):
	return (i >= NA) or (j >= NB) or (k >= NC)

def find_intersection3(A, B, C):
	NA = len(A)
	NB = len(B)
	NC = len(C)

	i = 0
	j = 0
	k = 0

	ret = []
	while not stop_cond3(i, j, k, NA, NB, NC):
		if( (A[i] == B[j]) and (B[j] == C[k]) ):
			# print(i,j,k,A[i],B[j],C[k])
			ret.append(A[i])
			i += 1
			j += 1
			k += 1
		elif( A[i] < B[j] ):
			i += 1
		elif( B[j] < C[k] ):
			j += 1
		else:
			k += 1

	return ret






if __name__ == '__main__':
	print()
	print('===============')
	print('For 2 Arrays A, B: ')
	res  = find_intersection(A, B)
	print(res)
	

	res3 = find_intersection3(A, B, C)

	print()
	print('===============')
	print('For 3 Arrays A, B, C: ')
	print(res3)