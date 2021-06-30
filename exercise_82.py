import numpy as np

Z = np.array([("Hello", 2.5, 3),
("World", 3.6, 2)])
R = np.core.records.fromarrays(Z.T,
names='col1, col2, col3',
formats = 'S8, f8, i8')