import re
with open('inputs/input-04.txt') as file:
    raw = file.read()

part1 = 0
part2 = 0
for fields in raw.split('\n\n'):
    fields = dict(i.split(':') for i in fields.split())
    if len(fields) == 7+('cid' in fields):
        part1 += 1
        part2 += (
            1920 <= int(fields['byr']) <= 2002 and
            2010 <= int(fields['iyr']) <= 2020 and
            2020 <= int(fields['eyr']) <= 2030 and
            (
                fields['hgt'][-2:] == 'cm' and 150 <= int(fields['hgt'][:-2]) <= 193 or
                fields['hgt'][-2:] == 'in' and 59 <= int(
                    fields['hgt'][:-2]) <= 76
            ) and
            bool(re.fullmatch(r'#[0-9a-f]{6}', fields['hcl'])) and
            fields['ecl'] in 'amb blu brn gry grn hzl oth'.split() and
            len(fields['pid']) == 9 and fields['pid'].isdigit()
        )

print(part1)
print(part2)
