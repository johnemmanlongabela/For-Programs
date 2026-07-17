title = (' "UNIT CONVERTER" ').upper()
print(title)
conversion_title = ('Conversions Available: ').upper()
print(conversion_title)

conversion_list = [
    (1, 'km', 'mi'),
    (2, 'mi', 'km'),
    (3, 'kg', 'lbs'),
    (4, 'lbs', 'kg'),
    (5, '℃', '℉'),
    (6, '℉', '℃')
]

print(conversion_list)

for conversion_number, from_unit, to_unit in conversion_list:
    print(f'{conversion_number} -> {from_unit} -> {to_unit}')

conversion = input('Enter the number: ')
conversion_index = int(conversion) - 1

conversion_number, from_unit, to_unit = conversion_list[conversion_index]

from_value = float(input(f'{from_unit} -->'))

if conversion_number == 1:
    to_value = from_value * 0.62
    print(f'{from_value} {from_unit} -> {to_value}{to_unit}')

if conversion_number == 2:
    to_value = from_value * 1.61
    print(f'{from_value} {from_unit} -> {to_value}{to_unit}')

if conversion_number == 3:
    to_value = from_value * 2.20462
    print(f'{from_value} {from_unit} -> {to_value}{to_unit}')

if conversion_number == 4:
    to_value = from_value * 0.453592
    print(f'{from_value} {from_unit} -> {to_value}{to_unit}')

if conversion_number == 5:
    to_value = (from_value * 9/5) + 32
    print(f'{from_value} {from_unit} -> {to_value}{to_unit}')

if conversion_number == 6:
    to_value = (from_value - 32) * 5/9
    print(f'{from_value} {from_unit} -> {to_value}{to_unit}')
