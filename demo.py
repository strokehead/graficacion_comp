import pixie as px
from line import *

PIXEL_SIZE = 5

def draw_line(ctx, points):
    for point in points:
        ctx.fill_rect(point[0] * PIXEL_SIZE, point[1] * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)

image = px.Image(600, 600)
image.fill(px.Color(255, 255, 255, 255))

paint = px.Paint(px.SOLID_PAINT)
paint.color = px.Color(1, 0, 0, 1)

ctx = image.new_context()
ctx.fill_style = paint

points = bresenham(25, 8, 35, 8)
draw_line(ctx, points)

points = bresenham(0, 0, 120, 120)
draw_line(ctx, points)

points = bresenham(25, 10, 35, 18)
draw_line(ctx, points)

points = bresenham(0, 0, 25, 34)
draw_line(ctx, points)

image.write_file("bresenham.png")
