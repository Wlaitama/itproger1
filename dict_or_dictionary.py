country = {'code': 'U', 'name': 'USA', 'population': 143}  # Списки тут использовать нельзя, а кортежи можно
print(country['name'])
print(country.get('name'))
print(country.items())
print(country.keys())
print(country.values())
country.pop('name')
print(country)
country.popitem()
print(country)
print("------------------------------")

for key, volue in country.items():
    print(key, " - ", volue)

print("------------------------------")

country1 = dict(code='U', name='USA')
print(country1['name'])
print("------------------------------")

person = {
    'user_1': {
        'first_name': 'John',
        'last_name': 'Smit',
        'age': 45,
        'address': ('g. Moskow', 'str. Karla_maks', 'h. 45')
    },
    'user_2': {

    }
}

print(person['user_1']['address'][1])