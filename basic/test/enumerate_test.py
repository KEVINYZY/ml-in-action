arr = ['a', 'b', 'c', 'd', 'e', 'f']
print(arr)
print("---------------")
print(enumerate(arr))

# enumerate 可以追加index信息，如

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(seasons)
print(list(enumerate(seasons)))

# 遍历的时候获得index

for index, value in enumerate(seasons):
    print(index)
    print(value)