from xml.etree.ElementTree import Element, ElementTree, SubElement, tostring
 
class SVGElement(Element):
    
    def __init__(self, tag, attrib={}, **extra):
        super(self.__class__, self).__init__(tag, attrib, **extra)
        
        
def SVGSubElement(parent, tag, attrib={}, **extra):
    return SubElement(parent, tag, attrib, **extra)