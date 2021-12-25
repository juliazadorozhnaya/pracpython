from collections import defaultdict

w = int(input())
freq = defaultdict(int)
string = input()

while string != "":
    new_string = ""
    for v in string:
        if v.isalpha():
            new_string += v.lower()
        else:
            new_string += ' '
    for word in new_string.split():
        freq[word] += 1
    string = input()

mx = 0
words = []
for k, v in freq.items():
    if len(k) == w:
        if v == mx:
            words.append(k)
        elif v > mx:
            words = [k]
            mx = v

print(*words)
