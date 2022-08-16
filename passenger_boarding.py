count_of_rows = int(input())

scheme = [input() for _ in range(count_of_rows)]

count_of_groups = int(input())

groups_data = [input() for _ in range(count_of_groups)]

seats_scheme = 'ABC_DEF'


def get_groups_mask(groups):

    groups_data_list = [line.split() for line in groups]
    scheme_list = []
    result = ''
    seat_group = ''

    for line in groups_data_list:

        count = int(line[0])
        empty = 3 - count

        if line[1] == 'left' and line[2] == 'aisle':
            result = '_' * empty + '.' * count + '____'
        elif line[1] == 'left' and line[2] == 'window':
            result = '.' * count + '_' * empty + '____'
        elif line[1] == 'right' and line[2] == 'aisle':
            result = '____' + '.' * count + '_' * empty
        else:
            result = '____' + '_' * empty + '.' * count

        scheme_list.append(result)

    return scheme_list



groups_mask = get_groups_mask(groups_data)



def get_seat(scheme, groups_mask):

    for group in groups_mask:

        for i in range(count_of_rows):
            result = ['?'] * 7
            counter = group.count('.')
            seats = ''

            for j in range(7):
                wish = group[j]
                reality = scheme[i][j]
                if wish == '.' and reality == '.':
                    counter -= 1
                    result[j] = 'X'
                    seats = f'{seats} {i + 1}{seats_scheme[j]}'
                else:
                    result[j] = reality
            if counter == 0:
                scheme[i] = ''.join(result)
                print(f'Passengers can take seats:{seats}')
                [print(i) for i in scheme]
                scheme[i] = scheme[i].replace('X', '#')
                break

        if counter != 0:
            print(f'Cannot fulfill passengers requirements')



get_seat(scheme, groups_mask)

