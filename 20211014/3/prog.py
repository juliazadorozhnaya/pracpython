def input_container():
    wall = input()
    gas = 0
    liquid = 0
    count = 2
    while (temp := input()) != wall:
        gas += sum(1 for sym in temp if sym == '.')
        liquid += sum(1 for sym in temp if sym == '~')
        count += 1
    return len(wall) - 2, gas, liquid, count


def print_container(wall, liquid, count):
    liquid_rows = (liquid + count - 3) // (count - 2)
    gas_rows = wall - liquid_rows
    print('#' * count)
    for i in range(gas_rows):
        print('#' + '.' * (count - 2) + '#')
    for i in range(liquid_rows):
        print('#' + '~' * (count - 2) + '#')
    print('#' * count)


def print_diagram(gas, liquid):
    if gas < liquid:
        len_row = round(gas / liquid * 20)
        print('.' * len_row + ' ' + f'{gas:>{len(str(liquid)) + 20 - len_row}}' + '/' + str(gas + liquid))
        print('~' * 20 + ' ' + str(liquid) + '/' + str(gas + liquid))
    else:
        len_row = round(liquid / gas * 20)
        print('.' * 20 + ' ' + str(gas) + '/' + str(gas + liquid))
        print('~' * len_row + ' ' + f'{liquid:>{len(str(gas)) + 20 - len_row}}' + '/' + str(gas + liquid))


wall, gas, liquid, count = input_container()
print_container(wall, liquid, count)
print_diagram(gas, liquid)
