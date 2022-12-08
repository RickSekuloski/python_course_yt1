# Break, Continue and Pass statements

car_brands = ['BMW', 'Tesla', 'Audi', 'Mercedes', 'Volvo']
print('---------- Break --------------')
for brand in car_brands:
    if(brand == 'Audi'):
        break
    print(brand)

print('Outside the loop')

print('---------- Continue --------------')
for brand in car_brands:
    if(brand == 'Audi'):
        continue
    print(brand)

print('Outside the loop')

print('---------- Pass --------------')
is_old = True
if is_old:
    pass

print('Outside the if statement')