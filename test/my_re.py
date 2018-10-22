
import re

pat  = "ais"
string = "You raise me ais up"

# search(re, str)：搜索匹配str中re首次出现的下标元组
rst = re.search(pat, string)
print(rst) # <_sre.SRE_Match object; span=(5, 8), match='ais'>

pat = "Ame"
rst = re.search(pat, string)
print(rst) # None (空指针)

pat = "\t"
string = '''asdf
qw	er'''
rst = re.search(pat, string)
print(rst) # <_sre.SRE_Match object; span=(7, 8), match='\t'>

# 通用字符匹配：
# pat = "\w" # 匹配任意一个字母、数字和下划线，\W则相反匹配
# pat = "\d" # 匹配任意一个十进制数，\D则相反匹配
# pat = "\s" # 匹配任意一个空白字符，\S则相反匹配
pat = "\w\dpython\w"
string = "asdf3python_zxcv"
rst = re.search(pat, string)
print(rst) # <_sre.SRE_Match object; span=(3, 12), match='f3python_'>

# 原子表 —— 平等匹配
pat = "a[bcd]e"
string = "wersacej"
rst = re.search(pat, string)
print(rst) # <_sre.SRE_Match object; span=(4, 7), match='ace'>

# 元字符(正则表达式中具有特殊含义的字符，如果要匹配本身需进行转义)：\ . ^ $ * ? + {}
'''
\: 转义字符
.: 匹配任意字符
^: 匹配字符串开始的位置
$: 匹配字符串结束的位置
*: 匹配之前字符出现任意次
?: 匹配之前字符出现或不出现
+: 匹配之前字符至少出现一次
{}:限定符，里面是自然数n或区间[n, m](m>=n)，含义：匹配之前字符出现n次或n~m次，
写成{n,}表示匹配之前字符至少出现n次
'''
pat = "a{1,2}"
string = "aab"
rst = re.search(pat, string)
print(rst)








