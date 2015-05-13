# -*- coding: utf-8 -*-

from easySVG.core import SVGElement, SVGSubElement, set_precision, write, CDATA
from easySVG.shapes import rect, circle, ellipse, polygon

from xml.etree.ElementTree import ElementTree, tostring
import math
from os.path import join

set_precision(5)

width = 1600

dist = 1600 / 4

colors = ['green', 'red', 'blue', 'yellow', 'white']
# dist = width / len(colors)

vb = '{} {} {} {}'.format(0, 0, width, dist)
svg_attribs = {'xmlns': 'http://www.w3.org/2000/svg',
               'version': '1.1',
               'xmlns:xlink': 'http://www.w3.org/1999/xlink',
               'viewBox': vb}
svg = SVGElement('svg', svg_attribs)

circ_attribs = {'id': 'circ'}
circ = circle((dist/2, dist/2), dist/2, circ_attribs, parent = svg)

rect_attribs = {'id': 'rect'}
rect((dist, 0), dist, dist, rect_attribs, parent=svg)

ellipse_attribs = {'id': 'ellipse'}
ellipse = ellipse((2*dist+dist/2, dist/2),
                   dist/2, dist/4, ellipse_attribs, parent = svg)

polygon_attribs = {'id': 'polygon'}
polygon = polygon(((3*dist, dist/2), (3*dist+dist/2, 0), (4*dist, dist/2), (3*dist+dist/2, dist)),
                    polygon_attribs, parent = svg)

tsize = dist/5

for i, elem in enumerate(list(svg)):
    print(i, colors[i])
    elem.set('fill', colors[i])
    attrib = {'x': i * dist + dist / 2,
              'y': (dist) / 2,
              'fill': colors[(i+1) % len(colors)],
              'font-size': '{}px'.format(tsize),
              'text-anchor': 'middle',
              'dominant-baseline': 'middle'
             }
    print((i+1) % len(colors))
    t = SVGSubElement(svg, 'text', attrib)
    t.text = elem.get('id')
    attrib = {'x1': i * dist + dist / 4,
              'y1': (dist) / 2 + tsize / 2,
              'x2': i * dist + dist * 3 / 4,
              'y2': (dist) / 2 + tsize / 2,
              'stroke': 'black',
             }
    l1 = SVGSubElement(svg, 'line', attrib)
    attrib = {'x1': i * dist + dist / 4,
              'y1': (dist) / 2 - tsize / 2,
              'x2': i * dist + dist * 3 / 4,
              'y2': (dist) / 2 - tsize / 2,
              'stroke': 'black',
             }
    l2 = SVGSubElement(svg, 'line', attrib)

print(len(svg))
print(svg[-1], svg[-2])

write(svg, join('shapes.svg'))
