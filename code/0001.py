# -*- coding: utf-8 -*-
# 200组apple store应用的随机激活码

'''
python 随机数生成 (random模块)

1. random.seed() #给定随机数种子，若种子相同，生成的随机数队列是一样的，缺省参数则是系统时间

2. random.random() #生成指定范围内的随机浮点数，[0, 1]

3. random.randint(a, b) #指定范围内的随机整数, 包含上下限

4. random.uniform(a, b) #均匀分布, random也可以产生正态分布，指数分布等

5. random.randrange(start,stop,step) #按步长随机在上下限范围内曲一个随机数

6. random.sample(list, n) #从list中选取n个元素, 生成是列表list， 输入是sequence (list、str、tuple)

7. random.choice(list) # 从list中选取一个元素, 输入是sequence

8. random.shuffle #洗牌, 即打乱顺序，输入是list

wiki: http://python.usyiyi.cn/translate/python_278/library/random.html
'''

'''
UUID: 通用唯一标识符 (Universally Unique Identifier), 一般形式为: 1e7cfd0e-a728-495e-bb83-b06a681714a7 (http://www.uuid.online/)
通过MAC地址, 时间戳, 命名空间, 随机数, 伪随机数来保证生成ID的唯一性, 有着固定的大小(128 bit).  
uuid主要有5种算法(python中没有uuid2)

1. uuid1() — 基于时间戳 
由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
python中调用原型: uuid.uuid1([node[, clock_seq]]) 
如果 node 参数未指定, 系统将会自动调用 getnode() 函数来获取主机的硬件地址. 如果 clock_seq  参数未指定系统会使用一个随机产生的14位序列号来代替. 

2. uuid2() - 基于分布式计算环境DCE（Python中没有这个函数）
算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。实际中很少用到该方法。

3. uuid3() - 基于名字的MD5散列值
通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
python调用原型: uuid.uuid3(namespace, name), 下uuid5相同

4. uuid4() - 基于随机数
由伪随机数得到，有一定的重复概率，该概率可以计算出来, 一般不用

5. uuid5() - 基于名字的SHA-1散列值
算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法

使用注意:
首先，Python中没有基于DCE的，所以uuid2可以忽略
其次，uuid4存在概率性重复，由无映射性，最好不用；
再次，若在Global的分布式计算环境下，最好用uuid1；
最后，若有名字的唯一性要求，最好用uuid3或uuid5。

uuid3和uuid5需要提供参数(命名空间和名字)
'''

# 方法1: 随机数方式
import random
import string

def random_activation_code_1(num = 200):
	field = string.letters + string.digits
	def single_part(n = 4):
		return ''.join(random.sample(field, n))
	def concatenate(group = 5):
		return '-'.join([single_part() for i in range(group)])

	activation_codes = []
	while num >  0:
		code = concatenate()
		if code not in activation_codes:
			activation_codes.append(code)
			num -= 1
	return activation_codes

# 方法2: uuid模块的使用
import uuid 
import time
def random_activation_code_2(num = 200):
	activation_codes = []
	while num > 0:
		code = str(uuid.uuid3(uuid.NAMESPACE_DNS, ''.join(random.sample(string.letters, 4))))
		if code not in activation_codes:
			activation_codes.append(code)
			num -= 1
	return activation_codes

if __name__ == '__main__':
	activation_codes = random_activation_code_1()
	print '\n'.join(activation_codes[0:5])

	activation_codes = random_activation_code_2()
	print '\n'.join(activation_codes[0:5])
