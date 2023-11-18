# 注释
import operator

print('demo2')
# 多行注释
'''
a = 's'
'''
#isinstance(a,int)
#print(str(a))

var1 = 1
var2 = 3

#del var1, 从内存中清除变量var1的引用地址

print(var1)

# 字符串格式化
var3 = 'mike %s age is %d' % ('and to',2)
print(var3)
var3+='aaa'
print(var3)
var3 = 'ddd'
print(var3)

# 列表
l1 =[1,'22',2.3]
# 列表中的下标可以从负数开始，表示从列表末尾开始计算的索引位置。-1 表示列表中的最后一个元素，-2 表示倒数第二个
print(l1[-1])
# 更新列表中的元素，可以和原值的数据类型不一致
l1[0] = 'abc'
print(l1[0])
# append
l1.append('baidu')
print(l1)
# del，删除列表的元素
del l1[0]
print(l1[0])

lt1 = [1,3,4,5]
lt2 = [3,23]
lt3 = lt1 + lt2
lt4 = lt1 - lt2
print(lt3)
print(lt4)

# in 
print(3 in [1,2,4,3])
# 迭代
for x in [1, 2, 3]: print(x)
# 比较
a=[1,3]
b=[2,4]
print(operator.eq(a,b))	

#字典
tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print(tinydict)

# set
sa = set('abracadabra')
print(sa)
sa.update(['b','c',2])
print(sa)
# sa.pop()
print(sa)

# for
for t_sa in sa:
    print(t_sa)

wd1 = 'helloworld'
for t_wd in wd1:
    print(t_wd)

ti = 2*2
print('ti的值:',ti)

# 斐波拉契
fa,fb = 0,1
while fb <10:
    print(fb)
    fa,fb = fb, fa+ fb

# 推导式
mi = [i for i in range(20) if i%3 ==0]
print(mi)

# 输入、输出
# v_input = input()
# print(v_input)

# 字符串 单引号,单引号 内的内容原样输出
print('hello " python" ')

# 字符串变量
x = "123f"
print(f"x的值是:{x}")
