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

def contains_bag(bag: str, target='shiny gold') ->  bool:
    return target in data[bag] or any(contains_bag(i) for i in data[bag])

amount = 0
for bag in data:
    amount += contains_bag(bag)
print(amount)