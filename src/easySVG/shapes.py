from easySVG.core import SVGElement, SVGSubElement, parse_attribs

def rect(P_ul, width, height, attrib={}, parent=None, **extra):
    att = {'x': P_ul[0],
           'y': P_ul[1],
           'width': width,
           'height': height,
          }
    att.update(attrib)
    if parent == None:
        sgve = SVGElement('rect', parse_attribs(att), **extra)
    else:
        svge = SVGSubElement(parent, 'rect', parse_attribs(att), **extra)
    return svge

def circle(P_0, r, attrib={}, parent=None, **extra):
    att = {'x': P_0[0],
           'y': P_0[1],
           'r': r,
          }
    att.update(attrib)
    if parent == None:
        sgve = SVGElement('circle', parse_attribs(att), **extra)
    else:
        svge = SVGSubElement(parent, 'circle', parse_attribs(att), **extra)
    return svge
