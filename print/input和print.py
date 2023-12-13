TIME=int(input("输入次数:"))##int函数用来规定input输入的只能是数字
i=0
while i < TIME: 
  i=i+1
  print("第",i,"次测试")
  ##同类表达1：
  ##print(f"第{i}次测试")##  f"{}"格式化字符串
  ##同类表达2:
  ##print("第%a次测试"%(i))##  "%字母"%()占字符
else:
  print("结束了", end="")