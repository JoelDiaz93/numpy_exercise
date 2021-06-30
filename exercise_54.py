import numpy as np
print('\n\tExercise 54')
class ArrayFuntion (np.ndarray) :
    def __new__(cls, array, name="no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__ (self, obj):
        if obj is None: return
        self.info = getattr(obj, 'name', "no name")
print('\t',ArrayFuntion(11))