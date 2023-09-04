import pandas as pd

mydataset = {
 'sites': ["Google", "Runoob", "Wiki"],
 'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

# print(myvar)
# 输出版本号
a = pd.__version__
# print(a)

# Series
s1 = [1,3,5,44]
myvar = pd.Series(s1)
# print(myvar)

q = [{'a':1,'b':2},{'a':11,'b':23}]
q2 = pd.DataFrame(q)
# DataFrame: 筛选，~ 取反
q1 = q2[(q2['a'] == 1)]
print(q1)