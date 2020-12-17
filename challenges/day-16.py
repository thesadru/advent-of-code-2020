with open('inputs/input-16.txt') as file:
    raw = file.read()

bounds,myticket,tickets = raw.split('\n\n')
tickets += '\n'+myticket.splitlines()[1]
names = [i.split(': ')[0] for i in bounds.splitlines()]
bounds = [[j.split('-') for j in i.split(': ')[1].split(' or ')] for i in bounds.splitlines()]
bounds  = [[(int(a),int(b)) for a,b in i] for i in bounds]
tickets = [list(map(int,ticket.split(','))) for ticket in tickets.splitlines()[1:]]

def part1():
    all_bounds = sum(bounds,[])
    error_rate = 0
    for val in sum(tickets,[]): # iterate over ALL the values
        if not any(a<=val<=b for a,b in all_bounds):
            error_rate += val
    return error_rate

def part2():
    myticket = tickets.pop(-1)
    
    # remove all unwanted
    all_bounds = sum(bounds,[])
    for i in range(len(tickets)-1,-1,-1):
        if not any(a<=val<=b for a,b in all_bounds for val in tickets[i]):
            tickets.pop(i)
    
    # get all possibilities
    possible = [set(range(len(bounds))) for _ in range(len(bounds))]
    for i,((a1,a2),(b1,b2)) in enumerate(bounds):
        for ticket in tickets:
            for field,val in enumerate(ticket):
                if not (a1<=val<=a2 or b1<=val<=b2):
                    if field in possible[i]: possible[i].remove(field)

    real = {}
    while len(real)!=len(bounds): # while haven't gotten answers
        for i in range(len(possible)):
            if len(possible[i])==1:
                field = possible[i].pop()
                real[names[field]] = i
                for j in range(len(possible)): # remove all times where it appears
                    if field in possible[j]:
                        possible[j].remove(field)
                break
    
    return 

print(part1())
print(part2())