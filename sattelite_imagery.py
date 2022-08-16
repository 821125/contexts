import numpy as np

shots_count = 3
shots = (
        (-1, -1, 1, 1),
        (-1, 0, 1, 1),
        (-1, -1, 0, 1)
    )

# shots_count = 4
# shots = (
#         (-3, -3, 3, 3),
#         (0, 0, 0, 0),
#         (-5, 0, 4, 0),
#         (-1, -4, 1, 3)
#     )

shots_data = {}


class Shot():

    def __init__(self, coordinates: tuple):
        self.x1, self.y1, self.x2, self.y2 = coordinates

    @property
    def grid(self):
        return np.mgrid[self.x1:self.x2:1,self.y1:self.y2:1]

    def __repr__(self):
        return f'({self.x1}, {self.y1}, {self.x2}, {self.y2})'


for i in range(shots_count):
    shots_data[i + 1] = Shot(shots[i])

print(shots_data)

shot1 = shots_data[1].grid
shot2 = shots_data[2].grid

print('shot1', shot1, sep='\n')
print('shot2', shot2, sep='\n')
print(f'result: {shot1 - shot2}')

