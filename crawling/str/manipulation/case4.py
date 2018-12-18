sentence1 = "오늘은 날씨가 좋네요."
sentence2 = "서울에 날씨가 좋네요."
sentence3 = "부산에 날씨가 나쁘네요."

print(sentence1.split(" ")[1])
print(sentence2.replace("날씨", "공기"))
print(sentence3.replace(" ", "\n"))

print(sentence1.split()[0] + " 서울에 " + sentence1.split()[1] + " 나쁘네요.")
