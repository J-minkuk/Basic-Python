i = 0
while i < 10:
    print("개구리 %d마리" %(i + 1))
    i += 1


for x in range(0, 10, 2):
    print(x)

for x in range(4, 8):
    print("<%d>" %x)


temp_list = [1, 3, 5, 7, 9]
for x in range(len(temp_list)):
    print(temp_list[x])