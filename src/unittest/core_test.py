# -*- coding: utf-8 -*-

import unittest
import easySVG.core
import numpy as np
import numbers
import collections
import sys

from easySVG.core import SVGElement, SVGSubElement, set_precision, write, CDATA
import xml.etree.ElementTree as ET
import collections
from io import BytesIO as SVGIO
import xml.dom.minidom

class coreTest(unittest.TestCase):
    
    def test_parse_attribs(self):
    

        #na = np.array([[6., 7.3, 9.e-5], [9., 8.3, 7.e-5]])
##        na = (6., 7.3, 9.e-5)
        #print('__getitem__' in dir(na))
        #print('__contains__' in dir(na))
        #print('__iter__' in dir(na))
        #print('__len__' in dir(na))
        #print('')
    
        #print(isinstance(na, numbers.Number))
        #print(dir(collections))
        #print(collections.Sized)
        #print(isinstance(na, collections.Sized))
        #print(isinstance(na[0], numbers.Real))
        #print(type(na), type(na[0]))
        #print(len(na))
        #print(iter(na))
    
        attribs = {'1': 1,
                   '2': 2.0,
                   '3': 3.3e0,
                   '4': 4.e-8,
                   '5': '5',
#                   '6': na[0],
#                   '7': na[1],
#                   '7': na,
                  }
        sollution = {'1': '1',
                     '2': '2',
                     '3': '3.3',
                     '4': '4e-08',
                     '5': '5',
#                   '6': na[0],
#                   '7': na[1],
#                   '7': na,
                  }
    
    
        pas = easySVG.core.parse_attribs(attribs)           
        for k in pas:
            self.assertEqual(sollution[k], pas[k])
            
    def test_umlaute(self):
        encoding='utf-8'
        indent='    '
        
        svg = SVGElement('svg')
        t = SVGSubElement(svg, 'text')
        t.add_text('äöüß', encoding)

        tree = ET.ElementTree(svg)
        io = SVGIO()
        tree.write(io, encoding=encoding, xml_declaration=None, method='xml')

        dom = xml.dom.minidom.parseString(io.getvalue())
        pretty_str = dom.toprettyxml(indent=indent,
                                 encoding=encoding)
        io2 = SVGIO(pretty_str)
        test_tree = ET.parse(io2)
        for txt in test_tree.iter('text'):
            if sys.version_info >= (3,0,0):
                self.assertEqual('äöüß', txt.text)
            else:
                self.assertEqual('äöüß'.decode(encoding), txt.text)

if __name__ == "__main__":
    print(sys.version)
    unittest.main()
        