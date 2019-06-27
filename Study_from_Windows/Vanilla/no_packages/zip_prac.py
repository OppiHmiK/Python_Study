names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Tony Stark']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Ironman']
universe = ['Marvel', 'DC', 'Marvel', 'Marvel']

for index, name in enumerate(names):
    hero = heroes[index]
    print(name + ' is actually ' + hero)

print('\n')

for name, hero in zip(names, heroes):
    print(name + ' is actually ' + hero)

print('\n')

for name, hero, univer in zip(names, heroes, universe):
    print(name + ' is actually ' + hero + ' in ' + univer)

print('\n')

for val in zip(names, heroes, universe):
    print(val[0] + ' is actually ' + val[1] + ' in ' + val[2])


