info = {'name': '班长',
        'age': 18
        }
print(info)
print(info['age'])

print(info.get('sex'))
print(info.get('sex', '男'))
print(info)

print()

info = {'name': '班长', 'id': 100}
print(info)
info['id'] = 200
print(info)

info = {'name': '班长'}
info['id'] = '01'
print(info)

info = {'name': '班长', 'id': '100'}
del info['name']
print(info)

info = {'name': '班长', 'id': '100'}
print(info)


