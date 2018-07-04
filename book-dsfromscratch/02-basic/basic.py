import this
import re
from collections import defaultdict
from collections import Counter

'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# 2.1.3
for i in [1,2,3,4,5]:
    print(i)
    for j in [1,2,3,4,5]:
        print(j)
        print(i+j)
    print(i)
print("done looping")

# 2.1.4
my_regex = re.compile("[0-9]+",re.I)

# 2.1.8
try:
    print(1/0)
except ZeroDivisionError:
    print("connot divide by zero")

# 2.1.9 列表

integer_list = [1,2,3]
# 切片
x = range(10)
first_three = x[:3]
copy_of_x = x[:]
print(first_three)
x, y = [1, 2] # 1给x 2给y
_, y = [1, 2] # 忽略1

# 2.1.11 字典

word_counts = defaultdict(lambda : [0,0])
word_counts[0][1] = 1
print(word_counts[0])

c = Counter([1,2,1,1,2])
print(c.most_common(1))

# 2.1.12 集合
item_list = [1,2,3,4,1,2,3]
item_set = set(item_list)
print(item_set)

# 2.1.13 控制流
if 1>2:
    print("111")
elif 1>3:
    print("222")
else:
    print("333")

# 2.1.14 假
print(False)
print(None)
print([])
print({})
print("")
print(set())
print(0)
print(0.0)