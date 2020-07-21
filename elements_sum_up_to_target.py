def merge_sort(arr):
	len_arr = len(arr)
	if( len_arr <= 1 ):
		return arr
	
	# Middle
	idm = len_arr//2

	# Left and right parts
	arr_left  = arr[:idm]
	arr_right = arr[idm:]

	merge_sort(arr_left)
	merge_sort(arr_right)

	i = j = k = 0

	while ( (i < len(arr_left)) and (j < len(arr_right)) ):
		if( arr_left[i] < arr_right[j] ):
			arr[k] = arr_left[i]
			i += 1
		else:
			arr[k] = arr_right[j]
			j += 1
		k += 1
	# End - while

	# Checking if any element was left 
	while (i < len(arr_left)):
		arr[k] = arr_left[i]
		i += 1
		k += 1

	while (j < len(arr_right)):
		arr[k] = arr_right[j]
		j += 1
		k += 1

	return arr



'''
A list of integer, no deplicates:
A = [2, 4, 10, 5, 1, 16, 24]

Find the elements in A that add up to 16
'''

A     = [2, 4, 10, 5, 1, 16, 24]
total = 17
N     = len(A) - 1

# A = sorted(A)      # Python built-in function
A = merge_sort(A)    # User mergre_sort function defined above
print('Sorted Array: ', A)

def find_num_sets(a, total, n):
	if len(a) == 0:
		return 0

	elif total < 0:
		return 0
	
	elif total == 0:
		return 1        # empty list
	
	elif n < 0:
		return 0

	elif total < a[n]:
		return find_num_sets(a, total, n-1)

	else:
		return find_num_sets(a, total-a[n], n-1) + find_num_sets(a, total, n-1)


res = find_num_sets(A, total, N)
print('total: ', total)
print('numbers of element sets with the sum = {} is: {}'.format(total, res))


print()
print('==============')
def find_num_sets_dp(a, total, n, memo):
	key = str(total) + '_' + str(n)

	if key in memo:
		return memo[key]

	if len(a) == 0:
		return 0

	elif total < 0:
		return 0
	
	elif total == 0:
		return 1        # empty list
	
	elif n < 0:
		return 0

	elif total < a[n]:
		ret = find_num_sets_dp(a, total, n-1, memo)

	else:
		ret = find_num_sets_dp(a, total-a[n], n-1, memo) +\
		      find_num_sets_dp(a, total, n-1, memo)

	memo[key] = ret
	return ret


memo = {}
res = find_num_sets_dp(A, total, N, memo)
print('total: ', total)
print('numbers of element sets with the sum = {} is: {}'.format(total, res))