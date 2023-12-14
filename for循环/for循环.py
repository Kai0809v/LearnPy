shuzi=[1,12,123,1234,12345,6]
for a in shuzi:
#in表示循环的范围，可以是表，也可以用其他函数，结尾也要用冒号，范围也可以剖析
     print(a)
#依次打印出范围内的数字
Min=int(input("输入范围下限："))
Max=int(input("输入范围上限："))
if Max >= Min:
     print("这个闭区间内包含的整数有：")
     for b in range(Min,Max+1):#python中括号内表示左闭右开区间
          print("%x"%(b),end="、")
          print("\n")
else:
     print("输入有误")


"""
range()函数三种写法
"""


print("---range(a)类型：")
print("当range()内只有一个数字时，如只有a，那么范围就是0到a-1")
print("for c in range(6):")
for c in range(6):
     print(f"C={c}")

print("---range(a,b)类型：")
print("当range()内有两个数字时，不必多说")
print("for d in range(0,7):")
for d in range(0,7):
     print(f"D={d}")

print("---range(a,b,c)类型：")
print("当range()内有三个数字时，前两个表示范围，第三个表示间隔")
print("for e in range(6,80,4):")
for e in range(6,80,4):
     print(f"E={e}")
