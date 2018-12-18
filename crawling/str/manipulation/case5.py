import re

sentence = "앨리스 : 01012341234,홍길동 01011112222, 박보검 01088885555"

compile_text = re.compile(r"010\d\d\d\d\d\d\d\d")
match_text = compile_text.findall(sentence)
print(match_text)

numbers = [match_text[0][3:11], match_text[1][3:11], match_text[2][3:11]]

print(numbers)
