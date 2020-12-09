with open('inputs/input-07.txt') as file:
    raw = file.read().splitlines()

data = {}
for bag in raw:
    main, inside = bag.split(' contain ')
    main = main.replace(' bags', '')  # remove 'bag'

    if inside == 'no other bags.':
        inside = {}
    else:
        # split into amount,color
        inside = [i.split(maxsplit=1) for i in inside[:-1].split(', ')]
        inside = {b.split(' bag')[0]: int(n) for n, b in inside}  # make into color:amount

    data[main] = inside


def contains_bag(bag: str, target: str = 'shiny gold') -> bool:
    return target in data[bag] or any(contains_bag(i) for i in data[bag])


def count_bags(bag: str) -> int:
    if data[bag]:
        contains = 0
        for color, amount in data[bag].items():
            contains += (count_bags(color)+1)*amount
        return contains
    else:
        return 0


part1 = sum(contains_bag(bag) for bag in data)
part2 = count_bags('shiny gold')

print(part1)
print(part2)
