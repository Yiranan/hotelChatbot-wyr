import re

response="xxxxxxxxxxxxxxxAnswer:SSSSSSSSSSSSSSSSSSS-cssssss"
match = re.search(r'Answer:(.*)', response)
print(match)


text = "xxxxxxanswer:zzzzzz"
answer_part = text.split("Answer:")[1]  # 分割字符串并取answer:后面的部分
print(answer_part)
