
import re

# 原生正则表达式：r"<reg_expression>"

# 例1-2 用正则表达式判断是否包含数字字符
# print(re.search(r"[0123456789]", "Hello 123 World!") is not None)

# 例1-4 使用^和$进行全匹配
# print(re.search(r"[0123456789]", "123") is not None)
# print(re.search(r"^[0123456789]$", "123") is not None)

# print(re.search(r"[0123456789]", "3") is not None)
# print(re.search(r"^[0123456789]$", "3") is not None)

# 简析：
# ^：匹配开始，$：匹配结束，中间只有一个单字符匹配（即只有一对方括号[]），所以首先可以确定这个
# 正则匹配出来的字符串长度是1，长度超过1或空字符串都是无法匹配的，接着看正则来确定具体匹配的内容。
# 所以r"^[0123456789]$"对"3"可以匹配，但是对"123"就无法匹配了。

# 范围表示符：-
# 例1-5 [0-9]是合法的，[9-0]会报错
# print(re.search(r"^[0-9]$", "2") is not None)
# print(re.search(r"^[9-0]$", "2") is not None)
# 测试 \u 和 \x 转移序列匹配
# print(re.search(r"^[\x30-\x45]$", "2") is not None)
# print(re.search(r"[\u5B66][\u0031]", "qwer学123") is not None)
# print(re.search(r"[\u5B66][\x31]", "qwer学123") is not None)

# 例1-9 使用转义字符 匹配 元字符
# print(re.search(r"[\-]", "214-10058741") is not None)

# 例1-13 使用脱字符 ^ 进行互补匹配
# 匹配一个0、1、2之外的字符
# print(re.search(r"^[^012]$", "^") is not None)
# 匹配四个字符0、^、1、2
# print(re.search(r"^[0^12]$", "^") is not None)
# ^紧跟在[之后但是使用转义
# print(re.search(r"^[\^012]$", "^") is not None)


# 例1-17 字符组简记法\d \w \s
# print(re.search(r"\d", "Beijing 2008 Olympic") is not None)
# print(re.search(r"\d", "Beijing Olympic") is not None)
# print()
# print(re.search(r"\w", "%$#@!+") is not None)
# print(re.search(r"\w", "%$#_@!+") is not None)
# print(re.search(r"\w", "Beijing 2008 Olympic") is not None)
# print()
# print(re.search(r"\s", "Beijing2008Olympic") is not None)
# print(re.search(r"\s", "Beijing 2008 Olympic") is not None)
# print(re.search(r"\s", "\t") is not None)
# print(re.search(r"\s", "\r") is not None)
# print(re.search(r"\s", "\n") is not None)
# print(re.search(r"\s", "\v") is not None)
# print(re.search(r"\s", "\f") is not None)

# 测试 \r(Carriage Return) & \n(Line Feed)
# print("Beijing\r2008 Olympic")
# print("Beijing\n2008 Olympic")
# print("Beijing\r\n2008 Olympic")

# 例2-3 长度限定符：{m,n} {0,n} {n,} *({0,}) +({1,}) ?({0,1})
print(re.search(r"^\d{4,6}$", "123") is not None)
print(re.search(r"^\d{4,6}$", "1234") is not None)
print(re.search(r"^\d{4,6}$", "123456") is not None)
print(re.search(r"^\d{4,6}$", "1234567") is not None)
print()
print(re.search(r"^\d{4,}$", "123") is not None)
print(re.search(r"^\d{4,}$", "1234") is not None)
print(re.search(r"^\d{4,}$", "1234567") is not None)
print()
print(re.search(r"^\d{0,6}$", "") is not None)
print(re.search(r"^\d{0,6}$", "123") is not None)
print(re.search(r"^\d{0,6}$", "1234567") is not None)
print()

# 例2-4 长度限定符?的应用
print(re.search(r"^colou?r$", "color") is not None, end=", This is American English\n")
print(re.search(r"^colou?r$", "colour") is not None, end=", This is British English\n")
print()

# 例2-5 长度限定符+的应用
print(re.search(r"^<[^>]+>$", "<div>") is not None)
print(re.search(r"^<[^>]+>$", "</div>") is not None)
print(re.search(r"^<[^>]+>$", "<>") is not None)
print()

# 例2-5 长度限定符*的应用
print(re.search(r"^<[^>]*>$", "<div>") is not None)
print(re.search(r"^<[^>]*>$", "</div>") is not None)
print(re.search(r"^<[^>]*>$", "<>") is not None)