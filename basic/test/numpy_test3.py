import numpy as np

width = 3
height = 4
_feat_stride = 2

shift_x = np.arange(0, width) * _feat_stride
print(shift_x)
shift_y = np.arange(0, height) * _feat_stride
print(shift_y)
shift_x, shift_y = np.meshgrid(shift_x, shift_y)
print(shift_x)
print(shift_y)
shifts = np.vstack((shift_x.ravel(), shift_y.ravel(),
                        shift_x.ravel(), shift_y.ravel())).transpose()
print(shifts)