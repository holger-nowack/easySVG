import xml.etree.ElementTree as ET
import collections
from io import BytesIO as SVGIO
import xml.dom.minidom

serialize_xml = ET._serialize_xml
def SVG_serialize_xml(write, elem, *args, **kwargs):
    if isinstance(elem, CDATA):
        write('<{}{}]]>'.format(elem.tag, elem.text))
        return
    return serialize_xml(write, elem, *args, **kwargs)
ET._serialize_xml = SVG_serialize_xml
ET._serialize['xml'] = SVG_serialize_xml

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

class SVGElement(ET.Element):
    
    def __init__(self, tag, attrib={}, **extra):
        att = parse_attribs(attrib)
        super(self.__class__, self).__init__(tag, att, **extra)

class CDATA(ET.Element):

    def __init__(self, parent, text):
        element = ET.Element('![CDATA[')
        super(self.__class__, self).__init__('![CDATA[')
        self.text = text
        parent.append(self)

def SVGSubElement(parent, tag, attrib={}, **extra):
    att = parse_attribs(attrib)
    svge = SVGElement(tag, att, **extra)
    parent.append(svge)
    return svge

def write(elem, filename, encoding='utf-8', indent='    '):
    tree = ET.ElementTree(elem)
    io = SVGIO()
    tree.write(io, encoding=encoding, xml_declaration=True, method='xml')

    dom = xml.dom.minidom.parseString(io.getvalue())
    pretty_str = dom.toprettyxml(indent=indent,
                                 encoding=encoding).decode(encoding)
    with open(filename, 'w') as f:
        f.write((pretty_str))
