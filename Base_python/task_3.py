world_champions = {
    2002: 'Бразилия',2006: 'Италия',
    2010: 'Испания',2014: 'Германия',2018: 'Франция'
}

world_champions[2022] = 'Аргентина'
for year, count in world_champions.items():
    print(year, '-', count)

country = 'Италия'

if 'Италия' in world_champions.keys() or 'Италия' in world_champions.values():
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
