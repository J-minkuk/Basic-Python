# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

S1 = {1, 3, 5, 7}
S2 = {5, 6, 7, 8, 9}

print(S1 & S2, S1 | S2, S1 - S2)

S1.add("GROOT")
print(S1)

S2.remove(9)
print(S2)

temp_list = [1, "1", "abc", 4]
S2.update(temp_list)
print(S2)

tuple1 = ('a', 13, 'python', 1, [1, 2, 3])
print(tuple1[2:4])


