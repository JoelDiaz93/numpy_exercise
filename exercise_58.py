import numpy as np

print('\n\tExercise 58')
B=np.random.randint(0,10,(3,4,3,4))
sum=B.reshape(B.shape[:-2]+(-1,)).sum(axis=-1)
print(sum)