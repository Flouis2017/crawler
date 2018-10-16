

# 控制流(control flow)
'''
def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(str(i) + "*" + str(j) + "=" + str(i * j), end="\t")
        print()
'''

# print_multiplication_table()

'''
def print_mutiplication_table_():
    for i in range(9, 0, -1):
        for j in range(i, 0, -1):
            print(str(i) + "*" + str(j) + "=" + str(i * j), end="\t")
        print()
'''

# print_mutiplication_table_()

# 作用域(scope)
'''
global tempArg
tempArg = 1

def func(arg):
    arg += 2
    j = 123

func(tempArg)
print(tempArg)
'''

# 模块(module)
# import <moduel_name>
# from <moduel_name> import <sub_module_name>
'''
import urllib
from urllib.request import urlopen
data = urllib.request.urlopen("http://www.baidu.com").read()
print( len(data) )
data = urlopen("https://fanyi.baidu.com/").read()
print( len(data) )
'''

'''
from urllib import request
data = request.urlopen("http://www.baidu.com").read()
print( len(data) )
'''

'''
from myModule import mylib
mylib.print_mutiplication_table_()
'''

# 文件操作(file operations)
import os
'''
fh = open("C:/Users/Administrator/Desktop/temporary/Flouis/test.txt", "r")
data = fh.read()
print(data)
fh.close()

url = "D:/Crawler/temp/File.txt"
# fileName = os.path.basename(url)
# print(url[url.rindex("/")+1:len(url)])
dirPath = url[0:url.rindex("/")]
# print( url )

flag = os.path.exists(dirPath)
if flag == False:
    os.makedirs(dirPath)

fh = open(url, "w")
fh.write('<contents>')
fh.close()

fh = open(url, "r")
# data = fh.read()
# print(data)
print("========================")
while True:
    line = fh.readline()
    if len(line) == 0:
        break
    print(line)

fh.close()
'''
# 异常处理(Exception handling)
try:
    print("asdf")
    url = "C:/temp/asdfasdfasfd"
    print(os.path.basename(url))

    print( 1 / 0 )
except Exception as e:
    print(e)
    print("hello!")





