line = eval(input())
line = list(line)
for i in range(len(line)-1):
    for j in range(len(line) - i - 1):
        if (line[j]**2 % 100) > (line[j+1]**2 % 100):
            line[j+1], line[j] = line[j], line[j+1]

print(line)
