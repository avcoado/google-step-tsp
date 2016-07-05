#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input

def distance(city1, city2):
	return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def read_coords(filename):
	coords = []
	with open(filename, 'r') as f:
		next(f)
		for line in f:
			x, y = line.strip().split(',')
			coords.append([float(x), float(y)])
		return coords


def tour_length(matrix, tour):
	total = 0
	num_cities = len(tour)
	for i in range(num_cities):
		j = (i + 1) % num_cities
		city_i = tour[i]
		city_j = tour[j]
		total += matrix[city_i, city_j]
	return total


def all_pairs(size, shuffle=random.shuffle):
	r1 = range(size)
	r2 = range(size)
	if shuffle:
		shuffle(r1)
		shuffle(r2)
	for i in r1:
		for j in r2:
			yield (i, j)


def swapped_cities(tour):
	'''generator to create all possible variations
      where two cities have been swapped'''
	for i, j in all_pairs(len(tour)):
		if i < j:
			copy = tour[:]
			copy[i], copy[j] = tour[j], tour[i]
			yield copy


def reversed_sections(tour):
	'''generator to return all possible variations
      where the section between two cities are swapped'''
	for i, j in all_pairs(len(tour)):
		if i != j:
			copy = tour[:]
			if i < j:
				copy[i:j + 1] = reversed(tour[i:j + 1])
			else:
				copy[i + 1:] = reversed(tour[:j])
				copy[:j] = reversed(tour[i + 1:])
			if copy != tour:  # no point returning the same tour
				yield copy


def write_tour_to_img(coords, tour, img_file):
	padding = 20
	# shift all coords in a bit
	coords = [(x + padding, y + padding) for (x, y) in coords]
	maxx, maxy = 0, 0
	for x, y in coords:
		maxx = max(x, maxx)
		maxy = max(y, maxy)
	maxx += padding
	maxy += padding
	img = Image.new("RGB", (int(maxx), int(maxy)), color=(255, 255, 255))

	font = ImageFont.load_default()
	d = ImageDraw.Draw(img);
	num_cities = len(tour)
	for i in range(num_cities):
		j = (i + 1) % num_cities
		city_i = tour[i]
		city_j = tour[j]
		x1, y1 = coords[city_i]
		x2, y2 = coords[city_j]
		d.line((int(x1), int(y1), int(x2), int(y2)), fill=(0, 0, 0))
		d.text((int(x1) + 7, int(y1) - 5), str(i), font=font, fill=(32, 32, 32))

	for x, y in coords:
		x, y = int(x), int(y)
		d.ellipse((x - 5, y - 5, x + 5, y + 5), outline=(0, 0, 0), fill=(196, 196, 196))
	del d
	img.save(img_file, "PNG")

# def solve(cities):
# 	N = len(cities)
#
# 	dist = [[0] * N for i in range(N)]
# 	for i in range(N):
# 		for j in range(N):
# 			dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
#
# 	current_city = 0
# 	unvisited_cities = set(range(1, N))
# 	solution = [current_city]
#
# 	def distance_from_current_city(to):
# 		return dist[current_city][to]
#
# 	while unvisited_cities:
# 		next_city = min(unvisited_cities, key=distance_from_current_city)
# 		unvisited_cities.remove(next_city)
# 		solution.append(next_city)
# 		current_city = next_city
# 	return solution


def main():
	coords = read_coords('input_0.csv')


if __name__ == '__main__':
	main()
