with open('inputs/input-12.txt') as file:
    raw = file.read()

data = [(i[0],int(i[1:])) for i in raw.splitlines()]

def part1():
    rot = 1 # rotation 90 / 90 clockwise == east
    x,y = 0,0 # a right,up direction (maths and shit)
    
    for c,a in data:
        if   c=='N': y += a
        elif c=='S': y -= a
        elif c=='E': x += a
        elif c=='W': x -= a
        
        elif c=='L': rot -= a//90; rot %= 4
        elif c=='R': rot += a//90; rot %= 4
        elif c=='F':
            if   rot==0: y += a
            elif rot==1: x += a
            elif rot==2: y -= a
            elif rot==3: x -= a
    
    return abs(x)+abs(y)

def rotate(x,y,rot):
    """
    Rotates a point around 0,0.
    """
    if   rot==0:   return  x, y
    elif rot==90:  return  y,-x
    elif rot==180: return -x,-y
    elif rot==270: return -y, x

def part2():
    sx,sy = 0,0 # ship x and y
    wx,wy = 10,1 # relative waypoint x and y
    
    for c,a in data:
        if   c=='N': wy += a
        elif c=='S': wy -= a
        elif c=='E': wx += a
        elif c=='W': wx -= a
        
        elif c=='L': wx,wy = rotate(wx,wy,360-a)
        elif c=='R': wx,wy = rotate(wx,wy,a)
        elif c=='F': sx += wx*a; sy += wy*a
    
    return abs(sx)+abs(sy)

print(part1())
print(part2())
