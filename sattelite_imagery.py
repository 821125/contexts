import itertools
from collections import deque


class Shot:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


shots_count = int(input())
shots = deque()
stack = deque()
result_image = set()
	
for _ in range(shots_count):
    shots.append(Shot(*tuple(map(int, input().split()))))

for _ in range(shots_count):

    shot = shots.pop()   
    mesh = set(itertools.product(range(shot.x1, shot.x2), range(shot.y1, shot.y2)))

    stack.append(len(mesh - result_image))
    result_image.update(mesh)

for _ in range(shots_count):
    print(stack.pop())
