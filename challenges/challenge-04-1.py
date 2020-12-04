with open('challenges/input-04.txt') as file:
    raw = file.read()

valid = 0
for fields in raw.split('\n\n'):
    fields = dict(i.split(':') for i in fields.split())
    valid +=  len(fields)==7+('cid' in fields)
print(valid)