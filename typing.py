def diff(str1, str2):
    result = 0
    index = 0
    while index < len(str1) and index < len(str2):
        if str1[index] != str2[index]:
            result += 1
    if len(str1) < len(str2):
        return result + len(str2) - len(str1)
    if len(str1) < len(str2):
        return result + len(str1) - len(str2)
    return result

print("어떤 노래로 타자 연습을 진행하고 싶으신가요?")
sss = input()
song = open(sss, "r",encoding="UTF-8")
lyrics = song.readline()
while lyrics:
    print(lyrics)
    ss = input()
    lyrics = song.readline()
