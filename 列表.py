# 列表可以包含任意类型的对象
# 列表是一个有序序列
# 列表是可变的
# 列表的基本操作
# 1、创建列表
x = [1,2,3]
y = ['a','b','c']
z = list('def')
print(x,'\n',y,'\n',z,'\n')
# 2、求长度
print(len(x),len(y),len(z),'\n')
# 3、合并 加法运算符可用于合并列表
a = x+y
print(a)
print(y+z,'\n')
# 4、重复 乘法运算符可创建具有重复值的列表
a = x*2
print(a)
print(y*2,'\n')
# 5、迭代 遍历列表元素
for i in x:
    print(i,end=' ')
for i in y:
    print(i,end=' ')
print('\n')
# 6、关系判断 用in可以判断对象是否属于列表
print(1 in x)
print(a in x,'\n')
# 7、索引（即脚标）
print(x[0])
print(x[1])
print(x[2])
print(y[1])
print('\n')
# 8、分片
x = list(range(90,101))
print(x)
print(x[0:11:2])
print('\n')
# 9、添加单个数据  append
x.append('abc')
print(x,'\n')
# 10、添加多个数据 extend
x.extend(['d','e','f'])
print(x,'\n')
# 11、插入数据 insert
x = [1,2,4]
x.insert(2,3)
print(x,'\n')
# 12、按值删除数据 remove
x.remove(2)
print(x,'\n')
# 13、按位置删除 pop
x.pop(2)
print(x,'\n')
# 14、删除指定数据或分片删除 del
x = list(range(1,11))
del x[0]
print(x)
del x[0:-1:2]
print(x,'\n')
# 15、删除全部数据 clear
x.clear()
print(x,'\n')
# 16、复制列表 copy
print(x)
x = y.copy()
print(x,'\n')
# 17、列表排序 可对同种类型的数据排序，对多种数据类型排序时报错  sort默认从小到大  sort(reverse = Trur)从大到小
x = [1,15,785,454,25,45,65]
x.sort()
print(x)
y = list('adsfjhkhgcmjiedjckadf')
print(y)
y.sort()
print(y,'\n')
# 18、反转排序 reverse
x = [5,9,2,4,1]
y = ['a','c','d',1,2,5,3]
print(x)
print(y)
y.reverse()
x.reverse()
print(y)
print(x)