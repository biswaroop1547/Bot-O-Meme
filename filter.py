with open("list.txt", "r") as p:
    lines = p.readlines()

print(lines)

with open("hindi-bad-words.txt", "r") as p:
    lines = p.readlines()
lines = [line.split(":")[0].strip() + "\n" for line in lines if len(line.split(":")[0].strip().split(" ")) < 2]

print(lines)

with open("hi_en_bad_words.txt", "a") as f:
    f.writelines(lines)