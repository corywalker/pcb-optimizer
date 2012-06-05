from spaces import Space
from parts import Part

# Only populated on two edges
def gen_dip_space(width, height):
    points = []
    for i in range(0, height):
        row = [None]*width
        row[0] = i + 1
        row[-1] = 2*height - i
        points.append(row)
    return Space(points, width, height)

# Completely filled with pins
def gen_header_space(width, height):
    points = []
    for i in range(0, height):
        row = [None]*width
        for j in range(0, width):
            row[j] = width*i + j + 1
        points.append(row)
    return Space(points, width, height)

# headers
for width in range(1, 6+1):
    for height in range(width, 12+1):
        header_space = gen_header_space(width, height)
        header = Part("head_%dx%d" % (width, height), header_space)
        print header.name
        header.save()

# DIP skinny
for i in range(1, 13+1):
    dip_s_space = gen_dip_space(4, i)
    dip_s = Part("dip%d" % (2*i), dip_s_space)
    print dip_s.name
    dip_s.save()

# DIP wide
for i in range(8, 25+1):
    dip_w_space = gen_dip_space(7, i)
    dip_w = Part("dip%d_w" % (2*i), dip_w_space)
    print dip_w.name
    dip_w.save()
