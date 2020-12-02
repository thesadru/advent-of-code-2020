with open('challenges/input-02.txt') as file:
    raw = file.readlines()

n = 0
for line in raw:
    line,char,password = line.split()
    a,b = [int(i)-1 for i in line.split('-')]
    char = char[0]
    
    n += (password[a]==char)^(password[b]==char)

print(n)