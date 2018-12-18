import re

sentence = "제보는 032-232-3245 또는 010-222-2233 으로 연락주시기 바랍니다."

compile_text = re.compile(r"010-\d\d\d-\d\d\d\d")
match_text = compile_text.findall(sentence)
print(match_text)

email = ["mingood@gmail.com", "kbs@bbb", "AWS@AWs.com", "gitflow.org"]

compile_text = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

for e in email:
    print(compile_text.match(e) != None)
