def create_city(population, size):
    return { 'population': population,
              'size': size}
    
def create_region(names, cities):
    d = {}
    for name,city in zip(names,cities):
        d[name] = city
    return d
names = ['Sochi', 'Krasnodar']
cities = [{'population': 10, 'size': 3}, {'population': 100, 'size': 10}]
print(create_region(names, cities))

