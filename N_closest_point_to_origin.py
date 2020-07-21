'''
Find N closest points to the origin
'''
data = [(-2, -4), (0, -2), (-1, 0), (3, -5), (-2, -3), (3, 2)]

def cal_distance(points):
	ret = []
	for (x,y) in points:
		ret.append(
			       {'coords': (x,y),
			         'distance': (x**2 + y**2)**0.5
			        })
	return ret


def find_max_heap(heap):
	imax = 0
	max_dist = heap[0]['distance']
	for i in range(1, len(heap)):
		if(max_dist < heap[i]['distance']):
			imax = i
			max_dist = heap[i]['distance']
	
	return imax, max_dist


def N_closest_points( data, N):
	length = len(data)
	dist_info = cal_distance(data)
	
	maxheap = dist_info[:N]
	# print(maxheap)

	for point in dist_info[N : length-1]:
		imax, max_dist = find_max_heap(maxheap)
		if(point['distance'] < max_dist):
			maxheap[imax]['distance'] = point['distance']
			maxheap[imax]['coords']   = point['coords']

	return maxheap


if __name__ == '__main__':
	N   = 3
	res = N_closest_points(data, 3)
	print('{} points closest to the origin:\n {}'.format(N, res))