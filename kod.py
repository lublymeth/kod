fruits = []
f = input('Enter your fruit (not)')
while f != 'not':
    if f in fruits:
        print('This fruit in list')
    else:
        fruits.append(f)
    f = input('Enter your fruit (not)')

print(fruits)
input()
