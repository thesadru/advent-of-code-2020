with open('challenges/input-07.txt') as file:
    raw = file.read().splitlines()

# parse data (fuck me)
data = {}
for bag in raw:
    main,inside = bag.split(' contain ')
    
    main = main.replace(' bags','') # remove 'bag'
    
    if inside=='no other bags.':
        inside = {}
    else:
        inside = [i.split(maxsplit=1) for i in inside[:-1].split(', ')] # split into amount,color
        inside = {b.split(' bag')[0]:int(n) for n,b in inside} # make into color:amount
    
    data[main] = inside

def count_bags(bag: str='shiny gold') -> int:
    if data[bag]:
        contains = 0
        for color,amount in data[bag].items():
            contains += (count_bags(color)+1)*amount
        return contains
    else:
        return 0

print(count_bags())