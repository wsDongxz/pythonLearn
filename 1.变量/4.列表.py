# -*-  coding = utf-8 -*-
# @Time : 2022/4/18 16:52
# @Autor : wsDongxz
# @File : 4.列表.py
# @Software : PyCharm

# 1. =====================  创建列表  ============================= #
# 创建列表变量
list1 = list()
list2 = []
list3 = [1, 2, 3]
print(type(list1))
print(type(list2))
print(type(list3))

# 2. =====================  访问列表的值  ============================= #
# 索引
list4 = [1, 2, 3, 4]
print(list4[0])  # 1
print(list4[-1])  # 4
# 切片
print(list4[:])  # [1, 2, 3, 4]
print(list4[1:])  # [2, 3, 4]
print(list4[1:3])  # [2, 3]  不包含stop的值
print(list4[::2])  # [1, 3]  不包含stop的值
# 更新列表值  -- 修改原有值
list4[0] = 100  # 列表索引0更新为100
print(list4)

# 更新列表值  -- 删除
del list4[0]
print(list4)
list4.remove(3)
print(list4)
# 删除并返回
a = list4.pop(1)
print('a = ', a)
print('list4', list4)
# 更新列表值  -- 插入
# 尾部插入
list4.append(222)
# 指定位置插入
list4.insert(1, 33)
print(list4)

# 更新列表值  --
print("==================== 操作符 =======================")
list1 = [0, 1, 2, 3]
list2 = [4, 5, 6, 7]
list3 = list1 + list2
print('list3', list3)  # [0, 1, 2, 3, 4, 5, 6, 7]
list4 = [1]
list5 = list4 * 4
print('list5', list5)  # [1, 1, 1, 1]
