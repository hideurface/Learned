"""
51900;83000;158000;367500;250000;59200;128500;1304000
"""
text = input()
table = text.split(';')
num_table = list(map(int, table))
sort_table = sorted(num_table)

for i in reversed(sort_table):
  print('{0:9,}'.format(i))
