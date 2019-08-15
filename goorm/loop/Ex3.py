dic = {
    "human": "사람",
    "dog": "강아지",
    "carrot": "당근"
}

odd_nums = (1, 3, 5, 7, 9)
even_nums = [6, 8, 10, 22, 50]
temp_str = "Hello GROOT"

for i in odd_nums:
    print(i, end=' ')
print()

for i in even_nums:
    print(i, end=' ')
print()

for i in temp_str:
    print(i, end=' ')
print()

for key, value in dic.items():
    print(key, value, end=' ')
