import numpy as np
print('\n100 EXERCISE NUMPY')
print('\n\tExercise 30')

def generate():
    for x in range(10):
        yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
print('\t',Z)

print('\n\tExercise 32')
A=np.random.random(10)
A.sort()
print('\t',A)