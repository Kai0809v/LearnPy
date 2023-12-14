"""
  可以将print函数的内容输出到文件。首先，你需要打开文件，然后将文件对象传递给print函数。
    打开一个文件用于写入
  file = open(r"I:\PYTHON\2\output.txt", "w")
    输出到文件
  print("这些文字将被写入文件", file=file)
    关闭文件
  file.close()
      
  你也可以使用正斜杠或双反斜杠来表示文件路径，这样可以避免转义问题：
    使用正斜杠
  file = open("I:/PYTHON/2/output.txt", "w")
    或者使用双反斜杠
  file = open("I:\\PYTHON\\2\\output.txt", "w")
"""
file = open(r"C:\Users\Administrator\Desktop\我的答辩python文件\测试.txt","w")
print("我想应该是允许内容和路径是中文的", file=file)
file.close()
#open函数在使用过后需要一个.close()来关闭文件，而with open不需要，这个在打开过后会自动关闭文件
