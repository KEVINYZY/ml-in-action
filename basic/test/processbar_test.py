import progressbar

arr = ['a', 'b', 'c', 'd', 'e', 'f']

bar = progressbar.ProgressBar(max_value = len(arr))
for index, value in bar(enumerate(arr)):
    print( str(index) + " -> " + value)