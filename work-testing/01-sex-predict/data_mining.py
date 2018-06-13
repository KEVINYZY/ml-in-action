__author__ = 'xingoo'
import json
import numpy as np

list = []

# 读取文件
with open("data.tg",'r') as load_f:
    for line in load_f.readlines():
        # json.dumps 是把json编程字符串
        # json.loads 是把字符串编程json
        line_json = json.loads(line.strip())
        # print(line_json)
        list.append([int(line_json['b1']),int(line_json['b2']),int(line_json['c1']),int(line_json['c2']),int(line_json['member_id']),int(line_json['sex'])])

for l in list:
    print(l)

np_arr = np.array(list)



# todo 拿到第一列和第二列融合起来，训练onehot
# todo 第三列和第四列，训练onehot
# todo 训练好后与第六列sex拼接在一起
