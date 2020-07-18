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

	print('arr_left: ', arr_left)
	print('arr_right: ', arr_right)

	i = j = k = 0

	ret = []
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


# Input list 
a = [12, 11, 13, 5, 6, 7] 
print("Given array is: ") 
print(a) 
print(*a)

print()
print("Process: ") 
res = merge_sort(a)

print()
print("Result: ") 
print(*res)

