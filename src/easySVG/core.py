from xml.etree.ElementTree import Element, ElementTree, tostring
import collections

_precision = 9

def set_precision(n=3):
    global _precision
    _precision = n
 
def parse_attribs(attrib):
    att = {}
    for key in attrib:
        value = attrib[key]
        if isinstance(value, float):
            if abs(value - round(value)) < 10.**(-_precision):
                value = int(value)
        elif isinstance(value, collections.Sized):
            s = ''
            for i in range(len(value)):
                s += str(i)
        att[key] = str(value)
    return att

class SVGElement(Element):
    
    def __init__(self, tag, attrib={}, **extra):
        att = parse_attribs(attrib)
        super(self.__class__, self).__init__(tag, att, **extra)
        
        
def SVGSubElement(parent, tag, attrib={}, **extra):
    att = parse_attribs(attrib)
    svge = SVGElement(tag, att, **extra)
    parent.append(svge)
    return svge
    