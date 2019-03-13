
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
# print(re.search(r"^\d{4,6}$", "123") is not None)
# print(re.search(r"^\d{4,6}$", "1234") is not None)
# print(re.search(r"^\d{4,6}$", "123456") is not None)
# print(re.search(r"^\d{4,6}$", "1234567") is not None)
# print()
# print(re.search(r"^\d{4,}$", "123") is not None)
# print(re.search(r"^\d{4,}$", "1234") is not None)
# print(re.search(r"^\d{4,}$", "1234567") is not None)
# print()
# print(re.search(r"^\d{0,6}$", "") is not None)
# print(re.search(r"^\d{0,6}$", "123") is not None)
# print(re.search(r"^\d{0,6}$", "1234567") is not None)
# print()

# 例2-4 长度限定符?的应用
# print(re.search(r"^colou?r$", "color") is not None, end=", This is American English\n")
# print(re.search(r"^colou?r$", "colour") is not None, end=", This is British English\n")
# print()

# 例2-5 长度限定符+的应用
# print(re.search(r"^<[^>]+>$", "<div>") is not None)
# print(re.search(r"^<[^>]+>$", "</div>") is not None)
# print(re.search(r"^<[^>]+>$", "<>") is not None)
# print()

# 例2-5 长度限定符*的应用
# print(re.search(r"^<[^>]*>$", "<div>") is not None)
# print(re.search(r"^<[^>]*>$", "</div>") is not None)
# print(re.search(r"^<[^>]*>$", "<>") is not None)

# 例2-7 通过re.search()返回的MatchObject提取数据
# print(type(re.search(r"\d{3}", "ab123cd").group(0)))
# print(re.search(r">[\w]+<", "<span>HelloWorld</span><em>test</em>").group(0))
# print()

# 例2-8 使用re.findall()提取数据
# print(type(re.findall(r">[\w]+<", "<span>HelloWorld</span><em>test</em>")))
# 可以遍历输出
# for match_text in re.findall(r">[\w]+<", "<span>HelloWorld</span><em>test</em>"):
#     match_text = match_text.replace("o", "a")
#     print(match_text[1:-1])
# 从上面可以看出re.search提取的数据是按就近原则匹配出的第一个，re.findall则是找出所有符合的数据

# 例2-10 单行匹配符.
# print(re.search(r"^[^\n]*$", "a12s3d4*(f&^%") is not None)
# print(re.search(r"^.*$", "a12s3d4*(f&^%") is not None)
# print(re.search(r"^.*$", "a12s3d4\n*(f&^%") is not None)

# 例2-11 单行模式下.可以匹配任意字符
# print(re.search(r"(?s)^.*$", "a12s3d4\n*(f&^%") is not None)

# 测试 贪婪/懒惰匹配：
# print(re.search(r"'.*'", "'quoted string' and another'").group(0))
# print(re.search(r"'.*?'", "'quoted string' and another'").group(0))

# html_source = '''
# <script type="text/javascript">
# alert("make a post request");
# </script>
#
# <script>
# alert("your request has been handled successfully");
# </script>'''

# js_regex = r"<script[\s>][\s\S]*?</script>"
# for match_text in re.findall(js_regex, html_source):
#     print(match_text + "\n")

# 例2-18 使用正则表达式拆解Windows的路径
# 注意：Windows下的路径分隔符为\，而\在正则表达式中是转移符，所以，使用两个\来表示\自身
# windows_url = "D:\\CloudMusic\\Local\\Loop\\The xx - Intro.mp3"
# print("file dir: " + re.search(r"^.*\\", windows_url).group(0))
# print("file name: " + re.search(r"[^\\]*$", windows_url).group(0))

# 例3-4 使用分组符(括号)改变量词(长度限定符)的作用元素
# print(re.search(r"^ab+$", "ab") is not None)        # True
# print(re.search(r"^ab+$", "abb") is not None)       # True
# print(re.search(r"^ab+$", "abab") is not None)      # False
# print()
# print(re.search(r"^(ab)+$", "ab") is not None)      # True
# print(re.search(r"^(ab)+$", "abb") is not None)     # False
# print(re.search(r"^(ab)+$", "abab") is not None)    # True

# 例3-5 使用分组符精确匹配open tag
# open_tag_regex = r"^<[^/]([^>]*[^/])?>$"
# print(re.search(open_tag_regex, "<u>") is not None)
# print(re.search(open_tag_regex, "<tr>") is not None)
# print(re.search(open_tag_regex, "<table>") is not None)
# print(re.search(open_tag_regex, "<input >") is not None)
# print(re.search(open_tag_regex, "<input />") is not None)
# print(re.search(open_tag_regex, "</u>") is not None)

# 例3-8 完整匹配电子邮箱地址的正则表达式
# email_regex = r"^[-.\w]{1,64}@([0-9a-zA-Z-]{1,63}\.)*[0-9a-zA-Z-]{1,63}$"
# print(re.search(email_regex, "Louis.Fan@qq.com") is not None)
# print(re.search(email_regex, "Flouis@mail.google.com") is not None)
# print(re.search(email_regex, "Flouis@.somewhere.host.com") is not None)

# 例3-10 使用多选结构匹配时分秒（HH:mm:ss）
# time_regex = r"^([01]\d|2[0-4]):[0-5]\d:[0-5]\d$"
# print(re.search(time_regex, "00:00:00") is not None)
# print(re.search(time_regex, "09:50:03") is not None)
# print(re.search(time_regex, "25:00:09") is not None)

# 使用多选结构匹配日期时间（yyyy-MM-dd HH:mm:ss）
# datetime_regex = r"^[12]\d{3}-(0[1-9]|1[012])-(0[1-9]|[12]\d|3[01]) ([01]\d|2[0-4]):[0-5]\d:[0-5]\d$"
# print(re.search(datetime_regex, "2019-03-13 22:34:56") is not None)
# print(re.search(datetime_regex, "2019-00-13 22:34:56") is not None)


