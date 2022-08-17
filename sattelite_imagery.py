shots_count = 3
shots = ((-1, -1, 1, 1), (-1, 0, 1, 1), (-1, -1, 0, 1))

sequence = [0] * shots_count

result_image = set()

for i in range(-1, -shots_count - 1, -1):

    x1, y1, x2, y2 = shots[i]
    mesh = set()
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            mesh.add((x, y))

    result = len(mesh - result_image)
    sequence[i] = result
    result_image.update(mesh)


for i in range(-shots_count, 0, 1):
    print(sequence[i])
