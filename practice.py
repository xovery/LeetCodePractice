print('1-----------------------------------------------')
myList = ['A','B','A','A','B','B','A','C','C','C']
count = {} #{}表示一個空字典
for element in myList:
    if element not in count:
        count[element] = 1
    else:
        count[element] += 1
print(count)

print('2-----------------------------------------------')

from collections import defaultdict
myList = ['A','B','A','A','B','B','A','C','C','C']
count = defaultdict(lambda: 0)
for element in myList:
    count[element] += 1
print(count)
