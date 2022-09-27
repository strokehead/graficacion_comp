def bresenham(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    m = dy / dx
    dx = abs(dx)
    dy = abs(dy)
    if m <= 1:
        if x1 > x2:
            x = x2
            y = y2
            xf = x1
        else:
            x = x1
            y = y1
            xf = x2
        p = 2 * dy - dx
        a = 2 * dy
        b = 2 * (dy - dx)
        points = bresenham1(x, y, xf, p, a, b)
    else:
        if y1 > y2:
            x = x2
            y = x2
            yf = y1
        else:
            x = x1
            y = y1
            yf = y2
        p = 2 * dx - dy
        a = 2 * dx
        b = 2 * (dx - dy)
        points = bresenham2(x, y, yf, p, a, b)
    return points

def bresenham1(x, y, xf, p, a, b):
    points = list(())
    while x <= xf:
        points.append((x, y))
        x += 1
        if p < 0:
            p += a
        else:
            p += b
            y += 1
    return points

def bresenham2(x, y, yf, p, a, b):
    points = list(())
    while y <= yf:
        points.append((x, y))
        y += 1
        if p < 0:
            p += a
        else:
            p += b
            x += 1
    return points

