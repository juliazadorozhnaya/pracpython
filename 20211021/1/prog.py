text = input().lower()

D = {}

for i,letter in enumerate(text):
     if (i < len(text)-1):
         pair = letter + text[i+1] if letter.isalpha() and (text[i+1]).isalpha() and (i < len(text)) else ""
         if pair:
             D[pair] = D.get(pair,0) + 1
print(len(sorted(D)))
