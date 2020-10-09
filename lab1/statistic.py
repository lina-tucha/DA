from matplotlib import pyplot

count_of_elements = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
time_of_stable_sort = [1, 6, 16, 31, 86, 152, 318, 605, 3372, 6645]
time_of_radix_sort = [1, 2, 6, 13, 38, 75, 162, 336, 913, 1978]

fig = pyplot.figure(figsize=(15, 10))
grid = pyplot.grid(True)

pyplot.plot(count_of_elements, time_of_stable_sort)
pyplot.plot(count_of_elements, time_of_radix_sort)
pyplot.legend(['stable_sort','radix sort'])
pyplot.show()