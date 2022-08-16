shots_count = int(input())
shots = tuple(tuple(map(int, input().split())) for _ in range(shots_count))

shots_data = {}
sequence = [0] * shots_count

for i in range(shots_count):
    shots_data[i + 1] = tuple(shots[i])

result_image = set()

for i in range(shots_count, 0, -1):

    x1, y1, x2, y2 = shots_data[i]
    mesh = set()

    for x in range(x1, x2):
        for y in range(y1, y2):
            mesh.add((x, y))

    result = len(mesh - result_image)
    sequence[i * -1] = result
    result_image.update(mesh)


for i in sequence[::-1]:
    print(i)

