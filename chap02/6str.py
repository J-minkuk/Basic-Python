greeting = '''첫 번째 줄
두 번째 줄
세 번째 줄'''
print(greeting)

msg1 = 'doesn\'t'
print(msg1)

msg2 = "\"Yes\", he said."
print(msg2)

# 문자열 앞에 r을 붙이면 특수문자로 해석하지 않는다.
print('C:\some\name')
print(r'C:\some\name')

print(len(msg2))

# 문자열의 출력
price = 10000
print("%s" % price)

msg = "%s월 %s일"
print(msg % (10, 10))

