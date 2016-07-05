from itertools import permutations
import math
#import time


def read_coords(filename):
	coords = []
	with open(filename, 'r') as f:
		next(f)
		for line in f:
			x, y = line.strip().split(',')
			coords.append([float(x), float(y)])
		return coords


def distance(city1, city2):
	return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


#calculates the total distance between the cities
def total_distance(cities):
	return sum([distance(city, cities[index + 1]) for index, city in enumerate(cities[:-1])])


#for longer inputs
def ts(cities):
	start = cities[0]
	to_visit = cities
	route = [start]
	to_visit.remove(start)
	while to_visit:
		nearest = min(to_visit, key=lambda x: distance(route[-1], x))
		route.append(nearest)
		to_visit.remove(nearest)
	return route


def main():
	#begin = time.time()
	points = read_coords('input_6.csv')
	print '\nlength: %s' % (total_distance(ts(points)))
	total_distance(ts_short(points))
	#end = time.time()
	#print "time: %.6f sec" % (end - begin)
	#time: 1.343409 sec

if __name__ == "__main__":
	main()
