import re

num = raw_input()
k = re.findall(r"1{6}|0{6}", num)
print bool(k)
