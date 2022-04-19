# 创建空的字符串
str1 = ''
str2 = str()

# 拼接
str3 = 'hello'
str4 = ' world'
print("str3 + str4 = ", str3 + str4)
# 复制
str5 = "hello"
print(str5 * 3)

# 索引
str6 = "ABCDEFG"
print("First element: ", str6[0])
print("Last element: ", str6[-1])
# 切片
print(str6[0:2])  # AB
print(str6[0::2])  # ACEG
print(str6[::])  # ABCDEFG
print(str6[-3:])  # EFG

# 逆向切片
# 从左向右截取，step应为正数
print(str6[-5:-1])  # CDEF
# 从右向左截取，step应为正数
print(str6[-1:-5:-2])  # GE
print(str6[-1:-5:-1])  # GFED

# 遍历
str7 = 'ABCDEFG'
for i in str6:
    print(i)

# format()函数
# 默认顺序
print("{} {}".format('hello', 'world'))
# 指定顺序
print("{0} {1}".format('hello', 'world'))
print("{1} {0}".format('hello', 'world'))

# 指定键值
print("{A} is a good {B}".format(A="dxz", B="man"))
print("{A} is a good {B}".format(A="xy", B="girl"))

# 字典
lol = {'s2': 'we', 's3': 'edg', 's4': 'ig', 's5': 'RNG'}
print('s3 is {s3}, s5 is {s5}, s2 is {s2}'.format(**lol))

# 列表
dnf = ['guiqi', 'heiwu']
print("鬼泣 is {data[0]}, 黑暗武士 is {data[1]}".format(data=dnf))


# print() 函数
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
# sep -- 用来间隔多个对象，默认值是一个空格。
# end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
# file -- 要写入的文件对象。
# flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。
print('AA''BB')  # AABB
print('AA', 'BB')  # AA BB
print('AA', 'BB', sep='-')  # AA-BB
print('AA', 'BB', sep='-', end='%%')  # AA-BB%%
print()

# input([prompt])
'''
a = input("请输入：")
print(type(a))
print(a)
'''

# 5 ================== 编码 ======================
import chardet
str8 = "python is a good language"
str9 = "python is a good language".encode('utf-8')
det = chardet.universaldetector.UniversalDetector()
det.feed(str9)
det.close()
print(det.result)


# ====== eval() ==== 函数
# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
print(eval("1+1"))
# ====== find()===
str10 = "ABCDEFGABCDEFG"
print(str10.find('C'))  # 2
print(str10.find('I'))  # -1
print(str10.rfind('A'))  # -1
print(str10.rfind('I'))  # -1