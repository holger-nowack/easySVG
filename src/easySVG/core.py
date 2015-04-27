from xml.etree.ElementTree import Element, ElementTree, SubElement, tostring

_precision = 3

def set_precision(n=3):
    global _precision
    _precision = n
 
def parse_attribs(attrib):
    att = {}
    for key in attrib:
        if isinstance(attrib[key], type(1)):
            att[key] = str(attrib[key])
        elif isinstance(attrib[key], type(1.)):
            att[key] = str(round(attrib[key], _precision))
        else:
            att[key] = attrib[key]
    return att

class SVGElement(Element):
    
    def __init__(self, tag, attrib={}, **extra):
        att = parse_attribs(attrib)
        super(self.__class__, self).__init__(tag, att, **extra)
        
        
def SVGSubElement(parent, tag, attrib={}, **extra):
    att = parse_attribs(attrib)
    return SubElement(parent, tag, att, **extra)