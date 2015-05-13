from easySVG.core import SVGElement, SVGSubElement, parse_attribs

def createElement(name, parent, attrib={}, **extra):
    if parent == None:
        sgve = SVGElement(name, parse_attribs(attrib), **extra)
    else:
        svge = SVGSubElement(parent, name, parse_attribs(attrib), **extra)
    return svge

def rect(P_ul, width, height, attrib={}, parent=None, **extra):
    att = {'x': P_ul[0],
           'y': P_ul[1],
           'width': width,
           'height': height,
          }
    att.update(attrib)
    return createElement('rect', parent, att, **extra)

def circle(P_0, r, attrib={}, parent=None, **extra):
    att = {'cx': P_0[0],
           'cy': P_0[1],
           'r': r,
          }
    att.update(attrib)
    return createElement('circle', parent, att, **extra)

def ellipse(P_0, rx, ry, attrib={}, parent=None, **extra):
    att = {'cx': P_0[0],
           'cy': P_0[1],
           'rx': rx,
           'ry': ry,
          }
    att.update(attrib)
    return createElement('ellipse', parent, att, **extra)

def polygon(points, attrib={}, parent=None, **extra):
    pstring = ''
    for p in points:
        pstring += '{},{} '.format(p[0], p[1])
    pstring.strip()
    att = {'points': pstring,
          }
    att.update(attrib)
    return createElement('polygon', parent, att, **extra)

