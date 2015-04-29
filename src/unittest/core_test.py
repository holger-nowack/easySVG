import unittest
import easySVG.core
import numpy as np
import numbers
import collections
import sys

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
if __name__ == "__main__":
    print(sys.version)
    unittest.main()
        