from collections import Counter
colors = ['red', 'blue', 'yellow', 'blue', 'red', 'blue']
counter = Counter(colors)
print(counter)# Counter({'blue': 3, 'red': 2, 'yellow': 1})
print(counter.most_common()[0]) # ('blue', 3)