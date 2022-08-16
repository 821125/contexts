acid_tanks_count = int(input())
acid_tanks = list(map(int, input().split()))


def count_number(acid_tanks_count, acid_tanks):

    counter = 0
    max_num = acid_tanks[-1]
    min_num = acid_tanks[-1]

    for i in range(acid_tanks_count - 1):

        current_colb = acid_tanks[i]
        next_colb = acid_tanks[i + 1]

        if current_colb > next_colb:
            return -1

        if current_colb > max_num:
            max_num = current_colb
        elif current_colb < min_num:
            min_num = current_colb

    result = max_num - min_num

    return result


print(count_number(acid_tanks_count, acid_tanks))

