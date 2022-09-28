import pixie as px
from line import *

PIXEL_SIZE = 15

def draw_line(ctx, points):
    for point in points:
        ctx.fill_rect(point[0] * PIXEL_SIZE, point[1] * PIXEL_SIZE, PIXEL_SIZE-1, PIXEL_SIZE-1)

image = px.Image(600, 600)
image.fill(px.Color(0, 0, 0, 0))

ctx = image.new_context()

#points = bresenham(25, 8, 35, 8)
#draw_line(ctx, points)

paint = px.Paint(px.SOLID_PAINT)
paint.color = px.parse_color("#000000")

ctx.fill_style = paint
#ctx = image.new_context()
ctx.stroke_style = paint
ctx.line_width = 1
for i in range(1,int(600/PIXEL_SIZE)):
    ctx.stroke_segment(0,i*PIXEL_SIZE , 600, i*PIXEL_SIZE)
    ctx.stroke_segment(i*PIXEL_SIZE,0 , i*PIXEL_SIZE, 600)


paint = px.Paint(px.SOLID_PAINT)
paint.color = px.Color(1, 0, 0, 1)
ctx.fill_style = paint

points = bresenham(0, 0, 120, 120)
draw_line(ctx, points)

paint = px.Paint(px.SOLID_PAINT);
paint.color = px.parse_color("#192965")
#points = bresenham(25, 10, 35, 18)
#draw_line(ctx, points)

ctx.fill_style = paint
points = line_equation_fx(6, 9, 25, 34)
draw_line(ctx, points)
image.write_file("bresenham.png")
