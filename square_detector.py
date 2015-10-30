#!/usr/bin/python
def solve():
    n = int(raw_input().strip())
    b = [raw_input().strip() for i in range(n)]
    black = 0
    minX, maxX, minY, maxY = n, 0, n, 0
    for x in range(0, n) :
        for y in range(0, n) :
            if b[x][y] == '#':
                minX, minY  = min(minX, x), min(minY, y)
                maxX, maxY = max(maxX, x), max(maxY, y)
                black += 1
    dx = maxX - minX + 1
    dy = maxY - minY + 1
    return dx == dy and dx * dy == black

if __name__ == '__main__':
    t = int(raw_input().strip())
    for i in range(1, t+1):
        res = solve()
        print 'Case #%d: %s' % (i, 'YES' if res else 'NO')