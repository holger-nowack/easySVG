'''
This module provides the core functionalities of the easySVG library.

'''

import sys
import xml.etree.ElementTree as ET
import collections
from io import BytesIO as SVGIO
import xml.dom.minidom

serialize_xml = ET._serialize_xml
def SVG_serialize_xml(write, elem, *args, **kwargs):
    '''
    Serialize a XML element. A special method is needed, because
    :py:mod:`xml.etree.ElementTree` doesn't support serialization of
    CDATA elements. XML special characters like <, >, " etc. are replaced
    with XML substituions. This is not wanted in CDATA block.
    
    :param write: The write function of original
        :func:`xml.etree.ElementTree._serialize_xml`
    :param elem: The element of :class:`xml.etree.ElementTree.Element` to
        serialize.
    :param args: List of optional arguments.
    :param kwargs: List of keyword arguments.
        
    '''

    if isinstance(elem, CDATA):
        write('<{}{}]]>'.format(elem.tag, elem.text))
        return
    return serialize_xml(write, elem, *args, **kwargs)
ET._serialize_xml = SVG_serialize_xml
ET._serialize['xml'] = SVG_serialize_xml

_precision = 9

def set_precision():
    '''
    Sets the precision to be used for floating point values of SVG attributes.
    
    :param n: Negative exponent that is used for rounding. Values are rounded
        if they are < :math:`10^{-n}`.
        
    '''

    global _precision
    _precision = n

def parse_attribs(attrib):
    '''
    Tries to parse all attributes given from their arbitrary type to a proper
    string. Usually floating points and lists are convereted to a string
    representation usable in SVG documents. This function is used in the 
    __init__() routine of :class:`SVGElement` objects.
    
    :param attrib: The unformated attributes.
        
    '''

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
    '''
    Class representing an element used in SVG documents.
    
    :param tag: The tag name describing the SVG element.
    :param attrib: Attributes of the SVG element.
    :param extra: Extra keyword arguments passed to the SVG element.

    '''
   
    def __init__(self, tag, attrib={}, **extra):
        att = parse_attribs(attrib)
        super(self.__class__, self).__init__(tag, att, **extra)
        
    def add_text(self, txt, encoding):
        '''
        Adds a text to the element with specified encoding. Handles encoding
        correct for python versions 2 and 3.
        
        :param self: A SVG element.
        :param txt: The txt to add to the SVG element.
        :param encoding: The encoding of txt.

        '''
        if sys.version_info >= (3,0,0):
            # for Python 3
            if isinstance(txt, bytes):
                s = txt.decode(encoding)  # or  s = str(s)[2:-1]
            else:
                s = txt
        else:
            # for Python 2
            if isinstance(txt, unicode):
                s = txt
            else:
                s = txt.decode(encoding)
        self.text = s

class CDATA(ET.Element):
    '''
    Class representing a CDATA block used in SVG documents. CDATA sections are
    not supported by :mod:`xml.etree.ElementTree` module. CDATA elements are
    treated differently in :func:`SVG_serialize_xml`. This way special XML
    characters like <, >, " etc are not converted to XML substitutions.
    This is important to define scripts included in the SVG document.
    
    :param parent: The parent element of the CDATA block
    :param text: The text that should be included in the CDATA block.

    '''
   

    def __init__(self, parent, text):
        element = ET.Element('![CDATA[')
        super(self.__class__, self).__init__('![CDATA[')
        self.text = text
        parent.append(self)

def SVGSubElement(parent, tag, attrib={}, **extra):
    '''
    Returns an :class:`SVGElement` that is included in *parent* SVGElement.
    
    :param parent: The parent SVG element contains this new element.
    :param tag: The tag name describing the new SVG sub element.
    :param attrib: Attributes of the SVG sub element.
    :param extra: Extra keyword arguments passed to the SVG sub element.

    '''

    svge = SVGElement(tag, attrib, **extra)
    parent.append(svge)
    return svge

def write(elem, filename, encoding='utf-8', indent='    '):
    '''
    Functions that writes an element to a file. Usually the root svg element
    is given to the file as the outer element containing the whole structure
    of the SVG document.
    
    :param elem: The root element that defines the document to be written.
        Usually this is the outer *svg* element. Sub elements are also
        serialized.
    :param filename: The filename to write to.
    :param encoding: The encoding used for the output file.
    :param indent: Indentation string used for pretty printing of the document.

    '''

    tree = ET.ElementTree(elem)
    io = SVGIO()
    tree.write(io, encoding=encoding, xml_declaration=True, method='xml')

    dom = xml.dom.minidom.parseString(io.getvalue())
    pretty_str = dom.toprettyxml(indent=indent,
                                 encoding=encoding).decode(encoding)
    with open(filename, 'w') as f:
        f.write((pretty_str))
