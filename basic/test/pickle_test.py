import pickle

# 初始化
data = ['a', 'b', 'c']

# 序列化成字符串
p_str = pickle.dumps(data)
print(p_str)

# 反序列化为对象
mes = pickle.loads(p_str)
print(mes)

# 保存成文件
with open('test.pkl', 'wb+') as f:
    pickle.dump(data, f, 0)

with open('test.pkl', 'rb+') as f:
    t = pickle.load(f)
    print(t)