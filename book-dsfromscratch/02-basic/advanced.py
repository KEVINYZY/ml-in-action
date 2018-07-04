import random
import re

# 2.2.1 排序
x = [4, 3, 2, 1]
y = sorted(x)
print(y)
y = sorted(x, reverse=True)
print(y)

# 2.2.2 列表解析
even_numbers = [x for x in range(5) if x%2 == 0]
print(even_numbers)
squares = [x*x for x in range(5)]
print(squares)
square_dict = {x: x*x for x in range(5)}
print(square_dict)
square_set = {x*x for x in [1, -1 , 1, -1]}
print(square_set)
zeroes = [0 for _ in even_numbers]
print(zeroes)
pairs = [(x,y) for x in range(2) for y in range(2)]
print(pairs)

# 2.2.3 生成器和迭代器
# genrator生成器可以延迟按需生成
def lazy_range(n):
    """ a lazy version"""
    i = 0
    while i < n:
        yield  i
        i += 1

for i in lazy_range(5):
    print(i)

# 2.2.4 随机性
four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)

random.seed(10)
print(random.random())
random.seed(10)
print(random.random())

up_to_ten = [4,3,2,1]
random.shuffle(up_to_ten)
print(up_to_ten)

print(random.choice(up_to_ten))
print(random.sample(up_to_ten,2))

# 2.2.5 正则表达式
print(all([not re.match("a","cat")]))

# 2.2.6 面向对象编程

# 2.2.7 函数式编程
def exp(base, power):
    return base ** power
print(exp(2,2))

# 2.2.8 枚举
for i,d in enumerate(['a','b','c']):
    print(str(i)+" -> "+d)

# 2.2.9 压缩
list1 = ['a','b','c']
list2 = [1,2,3]
list3 = zip(list1,list2)
print(list3)

# 2.2.10 args和kargs
def g(*args, **kwargs):
    print(*args)
    print(**kwargs)
print(g(1,2,3,4))