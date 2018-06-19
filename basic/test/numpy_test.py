import numpy as np

# 生成对角矩阵
print(np.eye(6))

# 创建label数组
arr = [3,4,2,1,1,1]
print(np.eye(len(arr))[arr])
print(np.eye(len(arr))[arr][np.newaxis, :])